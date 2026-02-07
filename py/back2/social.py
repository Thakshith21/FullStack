#!/usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
import sys
title = sys.argv[1]
subtitle = sys.argv[2]
logo = sys.argv[3]
facimg1 = sys.argv[4]
facimg2 = sys.argv[5]
facname1 = sys.argv[6]
facname2 = sys.argv[7]
facdesc1 = sys.argv[8]
facdesc2 = sys.argv[9]
date = sys.argv[10]
time = sys.argv[11]
reg = sys.argv[12]



# Open base image
base = Image.open("../inputimg/social.png").convert("RGBA")

# Load overlay images
logo = Image.open(f"../examlogos/{logo}-130.png").convert("RGBA")
himanshu = Image.open(f"../facimg/{facimg1}-280.png").convert("RGBA")
sanyam = Image.open(f"../facimg/{facimg2}-280.png").convert("RGBA")

# Paste images onto base
base.paste(logo, (320, 50), logo)
base.paste(himanshu, (260, 408), himanshu)
base.paste(sanyam, (560, 408), sanyam)

# Create draw context
draw = ImageDraw.Draw(base)

# Define font paths
bold_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Regular.ttf"

# Load fonts
font_big_title = ImageFont.truetype(bold_font_path, 60)
font_sub_title = ImageFont.truetype(bold_font_path, 40)
font_name = ImageFont.truetype(bold_font_path, 30)
font_designation = ImageFont.truetype(regular_font_path, 25)
font_date = ImageFont.truetype(regular_font_path, 25)
font_time = ImageFont.truetype(regular_font_path, 30)
font_register = ImageFont.truetype(bold_font_path, 36)


# Function to add stroke effect to text
def draw_text_with_stroke(position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    # Draw outline
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    # Draw main text
    draw.text(position, text, font=font, fill=fill)


# Updated subtitle function with dynamic positioning
def draw_subtitle(draw, base_position, text, font, fill, max_width=600, max_lines=2):
    x, _ = base_position
    original_font_size = font.size
    words = text.split()
    current_font = font

    # Try wrapping with current font
    while True:
        lines = []
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            w = draw.textbbox((0, 0), test_line, font=current_font)[2]
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

    # Set Y based on line count
    if len(lines) == 1:
        y = 355
    else:
        y = 340

    # Draw each line
    for line in lines:
        draw.text((x, y), line, font=current_font, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=current_font)
        h = bbox[3] - bbox[1]
        y += h + 5  # move down for next line

    return current_font.size


# Title with stroke
draw_text_with_stroke((290, 235), title, font=font_big_title, fill="#000")


# Subtitle with dynamic font and position
draw_subtitle(
    draw,
    base_position=(290, 340),
    text=subtitle,
    font=font_sub_title,
    fill="black",
    max_width=600,
    max_lines=2
)


# Names
draw.text((310, 700), facname1, font=font_name, fill="white")
draw.text((610, 700), facname2, font=font_name, fill="white")


# Designations
draw.text((310, 735), facdesc1, font=font_designation, fill="white")
draw.text((600, 735), facdesc2, font=font_designation, fill="white")


# Date and Time
draw.text((710, 845), date, font=font_date, fill="black")
draw.text((930, 840), time, font=font_time, fill="black")


# Register Now button
draw.text((445, 955), reg, font=font_register, fill="white")


# Save final output
base.save("../output/social.png")
