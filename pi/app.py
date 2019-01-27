import os

from dotenv import load_dotenv, find_dotenv

from banner_maker.banner_maker import BannerMaker
from mta_info.mta_info import MTAInfo

if __name__ == '__main__':
    load_dotenv(find_dotenv())

    MTA_API_KEY = os.environ['MTA_API_KEY']
    FEED_IDS = os.environ['FEED_IDS'].split(',')
    STATIONS = os.environ['STOPS'].split(',')

    mta_info = MTAInfo(
        api_key=MTA_API_KEY,
        feed_id=FEED_IDS[0],
        station=STATIONS[0]
    )

    banner = BannerMaker()
    banner.replace_banner(display_text=mta_info.get_train_text())
