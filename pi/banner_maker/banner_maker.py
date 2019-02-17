from PIL import Image, ImageFont, ImageDraw, ImageEnhance

FONTS_PATH = 'banner_maker/fonts/led.ttf'
GEN_DIR = 'banner_maker/generated/'
DISPLAY = 'display'
LED_OUPUT_PATH = GEN_DIR + DISPLAY + '.ppm'
WEB_OUPUT_PATH = GEN_DIR + DISPLAY + '.jpg'
BANNER_HEIGHT = 16
VERTICAL_OFFSET = 4


class BannerMaker:

    @staticmethod
    def replace_color_banner(display_data):

        print(display_data)
        if not display_data:
            print('no display data')
            return

        font_size_in_points = 9
        font = ImageFont.truetype(FONTS_PATH, font_size_in_points)

        text_size = font.getsize(''.join([text for _, text in display_data]))

        image = Image.new('RGB', text_size)
        image_draw = ImageDraw.Draw(image)

        horizontal_offset = 0

        for color, text in display_data:
            image_draw.text(
                (horizontal_offset, 0),
                text,
                font=font,
                fill=color
            )
            width, _ = font.getsize(text)
            horizontal_offset += width

        image = ImageEnhance.Contrast(image)
        image.enhance(1.99).save(LED_OUPUT_PATH)

        image = Image.open(LED_OUPUT_PATH)

        banner = Image.new('RGB', (image.width, BANNER_HEIGHT))
        banner.paste(image, (0, VERTICAL_OFFSET))

        banner.save(LED_OUPUT_PATH)
        banner.save(WEB_OUPUT_PATH)
