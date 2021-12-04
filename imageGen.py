import os
import random

import textwrap

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font = ImageFont.truetype("assets/fonts/monbaiti.ttf", 60)

textColor = 'white'
outlineColor = 'black'


def generate_image(advice):
    image = Image.open("assets/backgrounds/" + random.choice(os.listdir("assets/backgrounds")))
    draw = ImageDraw.Draw(image)
    lines = textwrap.wrap(advice, width=25)
    y = 300 - (len(lines) * 15);
    for line in lines:
        width, height = font.getsize(line)
        x = (800 - width) / 2
        for i in range(-2, 3):
            for j in range(-2, 3):
                draw.text((x + i, y + j), line, font=font, fill=outlineColor)
        draw.text(((800 - width) / 2, y), line, font=font, fill=textColor)
        y += height
    rgb_image = image.convert("RGB")
    rgb_image.save('result.jpg', quality=random.randint(20, 70))
    return 'result.jpg'
