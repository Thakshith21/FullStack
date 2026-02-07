#!/usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
import sys

template = sys.argv[1]
title = sys.argv[2]
subtitle = sys.argv[3]
logo = sys.argv[4]
facimg1 = sys.argv[5]
facimg2 = sys.argv[6]
facname1 = sys.argv[7]
facname2 = sys.argv[8]
facdesc1 = sys.argv[9]
facdesc2 = sys.argv[10]
date = sys.argv[11]
time = sys.argv[12]
reg = sys.argv[13]

# Function to add stroke effect to text
def draw_text_with_stroke(draw, position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    draw.text(position, text, font=font, fill=fill)

def draw_wrapped_text_with_resize(draw, position, text, font, fill,
                                   max_chars_per_line=20, max_lines=2, min_font_size=20,
                                   width_shift_threshold=400):
    x, y = position
    current_font = font
    words = text.split()

    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            current_line = current_line + " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    if len(lines) > max_lines:
        lines = lines[:max_lines]

    while True:
        _, line_height = draw.textsize("A", font=current_font)
        total_height = len(lines) * line_height + (len(lines) - 1) * 3

        if total_height > 80 or len(lines) > max_lines:
            if current_font.size <= min_font_size:
                break
            current_font = ImageFont.truetype(font.path, current_font.size - 2)
            lines = []
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 <= max_chars_per_line:
                    current_line = current_line + " " + word if current_line else word
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            if len(lines) > max_lines:
                lines = lines[:max_lines]
        else:
            break

    _, line_height = draw.textsize("A", font=current_font)
    total_height = len(lines) * line_height + (len(lines) - 1) * 3
    start_y = y - total_height // 2

    for line in lines:
        draw.text((x, start_y), line, font=current_font, fill=fill)
        _, h = draw.textsize(line, font=current_font)
        start_y += h + 3

    return current_font.size

# Load image
base = Image.open(f"/var/www/html/thakshith/templatetool1/inputimg/popup/popup-{template}.png").convert("RGBA")
logo = Image.open(f"/var/www/html/thakshith/templatetool1/examlogos/{logo}-60.png").convert("RGBA")
himanshu = Image.open(f"/var/www/html/thakshith/templatetool1/facimg/{facimg1}-110.png").convert("RGBA")
sanyam = Image.open(f"/var/www/html/thakshith/templatetool1/facimg/{facimg2}-110.png").convert("RGBA")

base.paste(logo, (160, 40), logo)
base.paste(himanshu, (360, 130), himanshu)
base.paste(sanyam, (480, 130), sanyam)

draw = ImageDraw.Draw(base)

# Fonts
bold_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Regular.ttf"

font_title = ImageFont.truetype(bold_font_path, 28)
font_subtitle = ImageFont.truetype(bold_font_path, 25)
font_name = ImageFont.truetype(bold_font_path, 12)
font_designation = ImageFont.truetype(regular_font_path, 10)
font_date_time = ImageFont.truetype(bold_font_path, 13)
font_register = ImageFont.truetype(bold_font_path, 20)
"""
# Centered Title
image_width = base.size[0]
title_width, title_height = draw.textsize(title, font=font_title)
title_x = (image_width - title_width) // 2
draw_text_with_stroke(draw=draw, position=(title_x, 155), text=title, font=font_title, fill="black")
"""

custom_center_x = 200
custom_center_y = 170

title_width, title_height = draw.textsize(title, font=font_title)
x = custom_center_x - (title_width // 2)
y = custom_center_y - (title_height // 2)

# Now pass the `draw` object properly
draw_text_with_stroke(
    draw,
    position=(x, y),
    text=title,
    font=font_title,
    fill="black",
    stroke_color="black",
    stroke_width=0
)


# Subtitle (fixed position)
draw_wrapped_text_with_resize(draw, position=(50, 255), text=subtitle, font=font_subtitle, fill="black")

# Centered Faculty Names
name1_w, _ = draw.textsize(facname1, font=font_name)
name2_w, _ = draw.textsize(facname2, font=font_name)
draw.text((360 + (110 - name1_w)//2, 245), facname1, font=font_name, fill="white")
draw.text((480 + (110 - name2_w)//2, 245), facname2, font=font_name, fill="white")

# Centered Designations
desc1_w, _ = draw.textsize(facdesc1, font=font_designation)
desc2_w, _ = draw.textsize(facdesc2, font=font_designation)
draw.text((360 + (110 - desc1_w)//2, 260), facdesc1, font=font_designation, fill="white")
draw.text((480 + (110 - desc2_w)//2, 260), facdesc2, font=font_designation, fill="white")

# Date & Time
draw.text((410, 290), date, font=font_date_time, fill="black")
draw.text((530, 290), time, font=font_date_time, fill="black")

# Register Button
draw.text((437, 340), reg, font=font_register, fill="white")

# Save
base.save("/var/www/html/thakshith/templatetool1/output/popup.png")

