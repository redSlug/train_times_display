import datetime

from PIL import Image, ImageFont, ImageDraw, ImageEnhance

FONTS_PATH = 'banner_maker/fonts/led.ttf'
GEN_DIR = 'banner_maker/generated/'
DISPLAY = 'display'
LED_OUPUT_PATH = GEN_DIR + DISPLAY + '.ppm'
WEB_OUPUT_PATH = GEN_DIR + DISPLAY + '.jpg'
SUMMARY_HEIGHT = 16
VERTICAL_OFFSET = 4


class BannerMaker:
    @staticmethod
    def get_time(text, prepend):
        now = datetime.date.strftime(datetime.datetime.now(), "%-I:%M%p")
        text_with_time = '{} {} '.format(now, text)
        print(text_with_time)
        return text_with_time if prepend else text

    def replace_banner(self, display_text):
        if not display_text:
            print('no display text')
            return

        display_text = self.get_time(display_text, prepend=False)

        font_size_in_points = 9
        font = ImageFont.truetype(FONTS_PATH, font_size_in_points)
        font_size = font.getsize(display_text)

        display_text_img = Image.new('RGB', font_size)
        draw = ImageDraw.Draw(display_text_img)
        draw.text((0, 0), display_text, font=font)

        enhancement = ImageEnhance.Contrast(display_text_img)
        enhancement.enhance(1.99).save(LED_OUPUT_PATH)

        enhanced_display_text = Image.open(LED_OUPUT_PATH)

        size = (enhanced_display_text.width, SUMMARY_HEIGHT)

        banner = Image.new('RGB', size)
        banner.paste(enhanced_display_text, (0, VERTICAL_OFFSET))

        banner.save(LED_OUPUT_PATH)
        banner.save(WEB_OUPUT_PATH)
