'''
This piece of code is used for generating new image from medicine info
'''

from PIL import Image, ImageFont, ImageDraw

import numpy as np
import textwrap as tw


BG_COLOR = (10, 10, 10)
TEXT_COLOR = (255, 255, 255)
SUBHEADING_COLOR = (100, 100, 255)

W, H = 1920, 1080
TEMPLATE_IMG = Image.new('RGB', (W, H), color=BG_COLOR)
TEMPLATE_NP_IMG = np.zeros([H, W, 3], dtype=np.uint8)
TEMPLATE_NP_IMG.fill(BG_COLOR[0])

HEADING_SIZE = 50
SUBHEADING_SIZE = 30
TEXT_SIZE = 25

FONT_HEADING = ImageFont.truetype('lib/fonts/PTM55F.ttf', HEADING_SIZE)
FONT_SUBHEADING = ImageFont.truetype('lib/fonts/PTM55F.ttf', SUBHEADING_SIZE)
FONT_TEXT = ImageFont.truetype('lib/fonts/PTM55F.ttf', TEXT_SIZE)

FONT_TEXT_W, FONT_TEXT_H = FONT_TEXT.getsize('a')
FONT_SUBHEADING_W, FONT_SUBHEADING_H = FONT_SUBHEADING.getsize('a')
FONT_HEADING_W, FONT_HEADING_H = FONT_HEADING.getsize('a')

X_INDENT = 40

Y_INDENT = 20
DY_HEADING = FONT_HEADING_H + 20
DY_SUBHEADING = FONT_SUBHEADING_H + 10
DY_TEXT = FONT_TEXT_H + 5

MAX_CHARS = (W - 2*X_INDENT) // FONT_TEXT_W


def text_to_img(info):
    if info['name'] == '': return TEMPLATE_NP_IMG
    y = Y_INDENT
    img = TEMPLATE_IMG.copy()

    for key, value in info.items():
        if key == 'name':
            ImageDraw.Draw(img).text((X_INDENT, y), value, font=FONT_HEADING, fill=TEXT_COLOR)
            y += DY_HEADING
        else:
            ImageDraw.Draw(img).text((X_INDENT, y), key, font=FONT_SUBHEADING, fill=SUBHEADING_COLOR)
            lines = tw.wrap(value, width=MAX_CHARS)

            for line in lines:
                y += DY_TEXT
                ImageDraw.Draw(img).text((X_INDENT, y), line, font=FONT_TEXT, fill=TEXT_COLOR)
            y += DY_SUBHEADING

    open_cv_image = np.array(img)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image