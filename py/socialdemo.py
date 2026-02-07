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

# Open base image
base = Image.open(f"/var/www/html/thakshith/templatetool1/inputimg/social/social-{template}.png").convert("RGBA")
logo_img_path = f"/var/www/html/thakshith/templatetool1/examlogos/{logo}-130.png"
himanshu_img_path = f"/var/www/html/thakshith/templatetool1/facimg/{facimg1}-280.png"
sanyam_img_path = f"/var/www/html/thakshith/templatetool1/facimg/{facimg2}-280.png"

logo = Image.open(logo_img_path).convert("RGBA")
himanshu = Image.open(himanshu_img_path).convert("RGBA")
sanyam = Image.open(sanyam_img_path).convert("RGBA")

# Paste images onto base
base.paste(logo, (320, 50), logo)
base.paste(himanshu, (260, 408), himanshu)
base.paste(sanyam, (570, 408), sanyam)

# Create draw context
draw = ImageDraw.Draw(base)

# Load fonts
bold_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Regular.ttf"

font_big_title = ImageFont.truetype(bold_font_path, 56)
font_sub_title = ImageFont.truetype(bold_font_path, 40)
font_name = ImageFont.truetype(bold_font_path, 30)
font_designation = ImageFont.truetype(regular_font_path, 25)
font_date = ImageFont.truetype(bold_font_path, 25)
font_time = ImageFont.truetype(bold_font_path, 30)
font_register = ImageFont.truetype(bold_font_path, 36)

# Function to add stroke effect to text
def draw_text_with_stroke(position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    draw.text(position, text, font=font, fill=fill)

# Subtitle function with wrapping and vertical positioning
def draw_subtitle(draw, base_position, text, font, fill, max_width=600, max_lines=2):
    x, _ = base_position
    original_font_size = font.size
    words = text.split()
    current_font = font

    while True:
        lines = []
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            w, _ = draw.textsize(test_line, font=current_font)
            if w <= max_width or not line:
                line = test_line
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)

        if len(lines) <= max_lines or current_font.size <= 10:
            break
        current_font = ImageFont.truetype(font.path, current_font.size - 2)

    if len(lines) == 1:
        y = 355
    else:
        y = 330

    for line in lines:
        draw.text((x, y), line, font=current_font, fill=fill)
        _, h = draw.textsize(line, font=current_font)
        y += h + 5

    return current_font.size

# --- Center the title text dynamically ---
image_width, image_height = base.size
title_width, title_height = draw.textsize(title, font=font_big_title)
x = (image_width - title_width) // 2
y = 260 - (title_height // 2)  # keep vertical center the same

draw_text_with_stroke((x, y), title, font=font_big_title, fill="#000")

# Subtitle with wrapping
draw_subtitle(
    draw,
    base_position=(290, 360),
    text=subtitle,
    font=font_sub_title,
    fill="black",
    max_width=600,
    max_lines=2
)

"""
# --- Center-aligned Faculty Name 1 & Designation 1 ---
fac1_center_x = 260 + 280 // 2  # X = 400 (center of facimg1)
name1_width, _ = draw.textsize(facname1, font=font_name)
desc1_width, _ = draw.textsize(facdesc1, font=font_designation)

draw.text((fac1_center_x - name1_width // 2, 700), facname1, font=font_name, fill="white")
draw.text((fac1_center_x - desc1_width // 2, 735), facdesc1, font=font_designation, fill="white")

# Names
#draw.text((305, 700), facname1, font=font_name, fill="white")
draw.text((605, 700), facname2, font=font_name, fill="white")

# Designations
#draw.text((305, 735), facdesc1, font=font_designation, fill="white")
draw.text((605, 735), facdesc2, font=font_designation, fill="white")
"""

# --- Center-aligned Faculty Name 1 & Designation 1 ---
fac1_center_x = 260 + 280 // 2  # X = 400
name1_width, _ = draw.textsize(facname1, font=font_name)
desc1_width, _ = draw.textsize(facdesc1, font=font_designation)
draw.text((fac1_center_x - name1_width // 2, 700), facname1, font=font_name, fill="white")
draw.text((fac1_center_x - desc1_width // 2, 735), facdesc1, font=font_designation, fill="white")

# --- Center-aligned Faculty Name 2 & Designation 2 ---
fac2_center_x = 560 + 280 // 2  # X = 700
name2_width, _ = draw.textsize(facname2, font=font_name)
desc2_width, _ = draw.textsize(facdesc2, font=font_designation)
draw.text((fac2_center_x - name2_width // 2, 700), facname2, font=font_name, fill="white")
draw.text((fac2_center_x - desc2_width // 2, 735), facdesc2, font=font_designation, fill="white")


# Date and Time
draw.text((710, 845), date, font=font_date, fill="black")
draw.text((930, 840), time, font=font_time, fill="black")

# Register Now button
draw.text((445, 955), reg, font=font_register, fill="white")

# Save output image
base.save("/var/www/html/thakshith/templatetool1/output/social.png")

