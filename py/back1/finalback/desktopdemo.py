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
base = Image.open(f"/var/www/html/thakshith/templatetool1/inputimg/desktop/desktop-{template}.png").convert("RGBA")
logo_img_path = f"/var/www/html/thakshith/templatetool1/examlogos/{logo}-60.png"
himanshu_img_path = f"/var/www/html/thakshith/templatetool1/facimg/{facimg1}-110.png"
sanyam_img_path = f"/var/www/html/thakshith/templatetool1/facimg/{facimg2}-110.png"

logo = Image.open(logo_img_path).convert("RGBA")
himanshu = Image.open(himanshu_img_path).convert("RGBA")
sanyam = Image.open(sanyam_img_path).convert("RGBA")

# Paste images
base.paste(logo, (110, 3), logo)
base.paste(himanshu, (420, 25), himanshu)
base.paste(sanyam, (540, 25), sanyam)

# Draw context
draw = ImageDraw.Draw(base)

# Fonts
bold_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Regular.ttf"

font_title = ImageFont.truetype(bold_font_path, 25)
font_subtitle = ImageFont.truetype(bold_font_path, 15)
font_name_large = ImageFont.truetype(bold_font_path, 14)
font_name_small = ImageFont.truetype(bold_font_path, 13)
font_designation = ImageFont.truetype(regular_font_path, 9)
font_date = ImageFont.truetype(bold_font_path, 14)
font_time = ImageFont.truetype(bold_font_path, 15)
font_register = ImageFont.truetype(bold_font_path, 24)

# Stroke function
def draw_text_with_stroke(position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    draw.text(position, text, font=font, fill=fill)

# --- Center-aligned Title ---
title_width, title_height = draw.textsize(title, font=font_title)
title_center_x = 145  # desired center point
x = title_center_x - title_width // 2
y = 100 - title_height // 2
draw_text_with_stroke((x, y), title, font=font_title, fill="black", stroke_color="black", stroke_width=0)

# Responsive subtitle
def draw_responsive_subtitle(draw, base_position, text, font, fill, max_width=200, max_lines=2):
    default_x, default_y = base_position
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
        if len(lines) <= max_lines or current_font.size <= 8:
            break
        current_font = ImageFont.truetype(font.path, current_font.size - 1)

    if len(lines) == 1:
        x = 20
        y = 155
    else:
        x = 30
        y = 140

    for line in lines:
        draw.text((x, y), line, font=current_font, fill=fill)
        _, h = draw.textsize(line, font=current_font)
        y += h + 2

    return current_font.size

# Subtitle
draw_responsive_subtitle(
    draw,
    base_position=(20, 155),
    text=subtitle,
    font=font_subtitle,
    fill="black",
    max_width=200,
    max_lines=3
)

# --- Center-align Faculty Names and Designations ---
fac1_center_x = 420 + 110 // 2  # = 475
fac2_center_x = 540 + 110 // 2  # = 595

# Faculty Name 1
name1_width, _ = draw.textsize(facname1, font=font_name_large)
draw.text((fac1_center_x - name1_width // 2, 140), facname1, font=font_name_large, fill="white")

# Faculty Name 2
name2_width, _ = draw.textsize(facname2, font=font_name_small)
draw.text((fac2_center_x - name2_width // 2, 140), facname2, font=font_name_small, fill="white")

# Faculty Designation 1
desc1_width, _ = draw.textsize(facdesc1, font=font_designation)
draw.text((fac1_center_x - desc1_width // 2, 155), facdesc1, font=font_designation, fill="white")

# Faculty Designation 2
desc2_width, _ = draw.textsize(facdesc2, font=font_designation)
draw.text((fac2_center_x - desc2_width // 2, 155), facdesc2, font=font_designation, fill="white")

# Date and Time
draw.text((715, 70), date, font=font_date, fill="black")
draw.text((835, 70), time, font=font_time, fill="black")

# Register Now button
draw.text((705, 115), reg, font=font_register, fill="white")

# Save final image
base.save("/var/www/html/thakshith/templatetool1/output/desktop.png")

