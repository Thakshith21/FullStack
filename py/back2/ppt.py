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



# Function to add stroke effect to text
def draw_text_with_stroke(draw, position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    # Draw outline
    for dx in range(-stroke_width, stroke_width + 1):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    # Draw main text
    draw.text(position, text, font=font, fill=fill)


# Function to wrap text strictly by character limit and draw all lines
def draw_wrapped_text_with_resize(draw, position, text, font, fill,
                                  max_chars_per_line=30, min_font_size=20,
                                  width_shift_threshold=700):
    x, y = position
    current_font = font
    words = text.split()

    # Step 1: Wrap by char limit - NO TRUNCATION
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

    # Step 2: Reduce font size if needed
    while True:
        line_height = draw.textbbox((0, 0), "A", font=current_font)[3]
        total_height = len(lines) * line_height + (len(lines) - 1) * 5

        if total_height > 120:
            if current_font.size <= min_font_size:
                break
            current_font = ImageFont.truetype(font.path, current_font.size - 2)

            # Recalculate lines with new font
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
        else:
            break

    # Step 3: Estimate width and shift if needed
    estimated_total_width = max_chars_per_line * len(lines) * 6
    if estimated_total_width > width_shift_threshold:
        x += 20
        y -= 10
    elif len(lines) > 1:
        x += 10
        y -= 5

    # Step 4: Center vertically around adjusted y
    line_height = draw.textbbox((0, 0), "A", font=current_font)[3]
    total_height = len(lines) * line_height + (len(lines) - 1) * 5
    start_y = y - total_height // 2

    # Step 5: Draw each line
    for line in lines:
        draw.text((x, start_y), line, font=current_font, fill=fill)
        start_y += line_height + 5

    return current_font.size


# --- MAIN SCRIPT ---
base = Image.open("../inputimg/ppt.png").convert("RGBA")

# Load images
logo = Image.open(f"../examlogos/{logo}-130.png").convert("RGBA")
himanshu = Image.open(f"../facimg/{facimg1}-200.png").convert("RGBA")
sanyam = Image.open(f"../facimg/{facimg2}-200.png").convert("RGBA")

# Paste overlays
base.paste(logo, (280, 50), logo)
base.paste(himanshu, (715, 185), himanshu)
base.paste(sanyam, (930, 185), sanyam)

draw = ImageDraw.Draw(base)

# Font paths
bold_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Regular.ttf"

# Load fonts
font_title = ImageFont.truetype(bold_font_path, 60)
font_subtitle = ImageFont.truetype(bold_font_path, 40)
font_name = ImageFont.truetype(bold_font_path, 25)
font_designation = ImageFont.truetype(regular_font_path, 18)
font_date = ImageFont.truetype(bold_font_path, 25)
font_time = ImageFont.truetype(bold_font_path, 30)
font_register = ImageFont.truetype(bold_font_path, 34)

# Title with stroke
draw_text_with_stroke(
    draw=draw,
    position=(110, 263),
    text=title,
    font=font_title,
    fill="black",
    stroke_color="black",
    stroke_width=1
)

# Subtitle
subtitle_text = subtitle
draw_wrapped_text_with_resize(
    draw,
    position=(110, 440),
    text=subtitle_text,
    font=font_subtitle,
    fill="black",
    max_chars_per_line=30
)

# Names
draw.text((745, 395), facname1, font=font_name, fill="white")
draw.text((960, 395), facname2, font=font_name, fill="white")

# Designations
draw.text((745, 425), facdesc1, font=font_designation, fill="white")
draw.text((960, 425), facdesc2, font=font_designation, fill="white")

# Date and Time
draw.text((820, 490), date, font=font_date, fill="black")
draw.text((1040, 480), time, font=font_time, fill="black")

# Register Now button
draw.text((837, 575), reg, font=font_register, fill="white")

# Save final image
base.save("../output/ppt.png")

#print("Banner generated successfully as '02.png'")
