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
    # Draw outline
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    # Draw main text
    draw.text(position, text, font=font, fill=fill)


def draw_wrapped_text_with_resize(draw, position, text, font, fill,
                                   max_chars_per_line=20, max_lines=2, min_font_size=20,
                                   width_shift_threshold=400):
    x, y = position
    current_font = font
    words = text.split()
# Step 1: Wrap text strictly by 20 chars per line
    lines = []
    current_line = ""

    for word in words:
        # If adding this word keeps us under limit, add it
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            # Else, push current line and start new one
            lines.append(current_line)
            current_line = word

    # Add the last line
    if current_line:
        lines.append(current_line)

    # Limit to max_lines
    if len(lines) > max_lines:
        lines = lines[:max_lines]

    # Step 2: Reduce font size if needed
    while True:
        # --- MODIFIED LINE FOR PILLOW 8.4.0 COMPATIBILITY ---
        _, line_height = draw.textsize("A", font=current_font)
        # --- END MODIFICATION ---
        total_height = len(lines) * line_height + (len(lines) - 1) * 3

        if total_height > 80 or len(lines) > max_lines:
            if current_font.size <= min_font_size:
                break
            current_font = ImageFont.truetype(font.path, current_font.size - 2)

            # Recalculate lines with new font
            lines = []
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 <= max_chars_per_line:
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            if len(lines) > max_lines:
                lines = lines[:max_lines]
        else:
            break

    # Step 3: Estimate width and shift if needed
    estimated_total_width = max_chars_per_line * len(lines) * 6
    if estimated_total_width > width_shift_threshold:
        x, y = (x + 20, y - 5)
    elif len(lines) > 1:
        x, y = (x + 10, y + 5)
    else:
        x, y = position

    # Step 4: Center vertically around adjusted y
    # --- MODIFIED LINE FOR PILLOW 8.4.0 COMPATIBILITY ---
    _, line_height = draw.textsize("A", font=current_font)
    # --- END MODIFICATION ---
    total_height = len(lines) * line_height + (len(lines) - 1) * 3
    start_y = y - total_height // 2

    # Step 5: Draw each line
    for line in lines:
        draw.text((x, start_y), line, font=current_font, fill=fill)
        # --- MODIFIED LINES FOR PILLOW 8.4.0 COMPATIBILITY ---
        _, h = draw.textsize(line, font=current_font)
        start_y += h + 3
        # --- END MODIFICATION ---

    return current_font.size
# --- MAIN SCRIPT ---
base = Image.open(f"/var/www/html/thakshith/templatetool1/inputimg/popup/popup-{template}.png").convert("RGBA")

# Load images
logo = Image.open(f"/var/www/html/thakshith/templatetool1/examlogos/{logo}-60.png").convert("RGBA")
himanshu = Image.open(f"/var/www/html/thakshith/templatetool1/facimg/{facimg1}-110.png").convert("RGBA")
sanyam = Image.open(f"/var/www/html/thakshith/templatetool1/facimg/{facimg2}-110.png").convert("RGBA")

# Paste overlays
base.paste(logo, (160, 40), logo)
base.paste(himanshu, (360, 130), himanshu)
base.paste(sanyam, (480, 130), sanyam)

draw = ImageDraw.Draw(base)

# Font paths
bold_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Regular.ttf"
# Load fonts
font_title = ImageFont.truetype(bold_font_path, 28)
font_subtitle = ImageFont.truetype(bold_font_path, 25)
font_name = ImageFont.truetype(bold_font_path, 12)
font_designation = ImageFont.truetype(regular_font_path, 10)
font_date_time = ImageFont.truetype(bold_font_path, 13)
font_register = ImageFont.truetype(bold_font_path, 20)

# Title with stroke
draw_text_with_stroke(
    draw=draw,
    position=(75, 155),
    text=title,
    font=font_title,
    fill="black",
    stroke_color="black",
    stroke_width=0
)
# Subtitle lines
subtitle_text = subtitle

draw_wrapped_text_with_resize(
    draw,
    position=(50, 255),
    text=subtitle_text,
    font=font_subtitle,
    fill="black",
    max_chars_per_line=20,    # <-- This ensures each line has max 20 characters
    max_lines=3,
    min_font_size=20
)
#  draw.text((65, 285), "Roadmap", font=font_subtitle, fill="black")

# Names
draw.text((375, 245), facname1, font=font_name, fill="white")
draw.text((490, 245), facname2, font=font_name, fill="white")
# Designations
draw.text((370, 260), facdesc1, font=font_designation, fill="white")
draw.text((500, 260), facdesc2, font=font_designation, fill="white")

# Date and Time
draw.text((410, 290), date, font=font_date_time, fill="black")
draw.text((530, 290), time, font=font_date_time, fill="black")

# Register Now button
draw.text((437, 340), reg, font=font_register, fill="white")
# Save final image
base.save("/var/www/html/thakshith/templatetool1/output/popup.png")
