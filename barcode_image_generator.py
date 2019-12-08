from intelligent_mail_barcode import encode
from PIL import ImageFont, ImageDraw, Image


class BarcodeImageGenerate(object):
    @staticmethod
    def gen_barcode_image(barcode_id, service_type, mailer, serial, delivery, compact=True):
        image = Image.new(mode='RGB', size=(1250, 100))
        draw = ImageDraw.Draw(image)
        draw.rectangle(((0, 00), (1250, 100)), fill="white")

        code = encode(int(barcode_id), int(service_type), int(mailer), int(serial), delivery)
        font = ImageFont.truetype('USPSIMBStandard.ttf', 100)
        draw.text((10, 10), code, fill='black', font=font)
        image.save(f'{serial}.png')

        image = Image.new(mode='RGB', size=(733, 75))
        draw = ImageDraw.Draw(image)
        draw.rectangle(((0, 00), (800, 100)), fill="white")
        font_compact = ImageFont.truetype('USPSIMBCompact.ttf', 50)
        draw.text((10, 10), code, fill='black', font=font_compact)
        image.save(f'{serial}_compact.png')


BarcodeImageGenerate.gen_barcode_image("1", "700", "314159", "000099999", "20500000399")


