from collections import defaultdict
import requests
import time

from google.protobuf.message import DecodeError
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict

MTA_URL = 'http://datamine.mta.info/mta_esi.php'
TIMES_TO_GET = 6
MIN_MINUTES_TO_SHOW = 3

TRAIN_COLORS = {'1': 'red',
                '2': 'red',
                '3': 'red',
                '4': 'green',
                '5': 'green'}


class MTAInfo:
    def __init__(self, api_key, feed_id, station):
        self.api_key = api_key
        self.feed_id = feed_id
        self.station = station
        self.feed_message = gtfs_realtime_pb2.FeedMessage()
        self.now = time.time()

    def get_minutes(self, train_time):
        return (train_time - int(self.now)) // 60

    def enough_time(self, train_time):
        return self.get_minutes(train_time) >= MIN_MINUTES_TO_SHOW

    def get_train_times(self, feed):
        train_time_data = list()
        for trains in feed:
            try:
                trip_update = trains.get('trip_update')
                if not trip_update:
                    continue

                route_id = trip_update['trip']['route_id']

                stop_time_update = trip_update['stop_time_update']
                for stop_info in stop_time_update:
                    if stop_info.get('stop_id') == self.station:
                        arrival = stop_info.get('arrival')
                        if not arrival:
                            continue
                        train_time_data.append((route_id, arrival['time']))
            except Exception as e:
                print(e)
                continue
        return train_time_data

    def get_minutes_til_train_with_color(self):
        feed = self.get_feed()
        if not feed:
            print('no feed')
            return
        train_times = self.get_train_times(feed)

        train_colors = defaultdict(lambda: 'white')

        for train, color in TRAIN_COLORS.items():
            train_colors[train] = color

        return [(train_colors[num], ' {}'.format(self.get_minutes(t)))
                for (num, t) in train_times if self.enough_time(t)]

    def get_feed(self, feed_id=None):
        feed_id = feed_id or self.feed_id
        query_str = '?key={}&feed_id={}'.format(
            self.api_key, feed_id
        )
        response = requests.get(MTA_URL + query_str)

        try:
            self.feed_message.ParseFromString(response.content)
            subway_feed = protobuf_to_dict(self.feed_message)
            return subway_feed['entity']
        except DecodeError as e:
            print('Unable to decode: {}'.format(e))
        except Exception as e:
            print(e)
            return "could not parse feed"
