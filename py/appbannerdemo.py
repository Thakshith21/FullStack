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
base = Image.open(f"/var/www/html/thakshith/templatetool1/inputimg/appbanner/appbanner-{template}.png").convert("RGBA")
#base = Image.open(f"/var/www/html/thakshith/templatetool1/inputimg/appbanner/appbanner-greenishyellow.png").convert("RGBA")

logo_img_path = f"/var/www/html/thakshith/templatetool1/examlogos/{logo}-130.png" # Assuming this is the correct path for the logo
himanshu_img_path = f"/var/www/html/thakshith/templatetool1/facimg/{facimg1}-170.png" # Assuming this is the correct path for facimg1
sanyam_img_path = f"/var/www/html/thakshith/templatetool1/facimg/{facimg2}-170.png" # Assuming this is the correct path for facimg2


logo = Image.open(logo_img_path).convert("RGBA")
himanshu = Image.open(himanshu_img_path).convert("RGBA")
sanyam = Image.open(sanyam_img_path).convert("RGBA")

# Paste images onto base
base.paste(logo, (260, 70), logo)
base.paste(himanshu, (630, 147), himanshu)
base.paste(sanyam, (825, 148), sanyam)

# Create draw context
draw = ImageDraw.Draw(base)

# Define font paths - IMPORTANT: Ensure these paths are correct and fonts exist
bold_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool1/fonts/Gilroy-Regular.ttf"

# Load fonts
font_title = ImageFont.truetype(bold_font_path, 50)
font_subtitle = ImageFont.truetype(bold_font_path, 40)
font_name = ImageFont.truetype(bold_font_path, 20)
font_designation = ImageFont.truetype(regular_font_path, 14)
font_date = ImageFont.truetype(bold_font_path, 20)
font_time = ImageFont.truetype(bold_font_path, 24)
font_register = ImageFont.truetype(bold_font_path, 26)


# Function to add stroke effect to text
def draw_text_with_stroke(position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    # Draw outline
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 2):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    # Draw main text
    draw.text(position, text, font=font, fill=fill)

# Dynamic wrapped text with smart positioning
def draw_wrapped_text_with_resize(draw, position, text, font, fill,
                                   max_chars_per_line=30, max_lines=3, min_font_size=30,
                                   width_shift_threshold=600):
    x, y = position
    current_font = font
    words = text.split()

    # Step 1: Wrap by char limit
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
    # Limit to max_lines
    if len(lines) > max_lines:
        lines = lines[:max_lines]

    # Step 2: Reduce font if too tall or too many lines
    while True:
        # --- MODIFIED LINE FOR PILLOW 8.4.0 COMPATIBILITY ---
        # Using textsize instead of textbbox
        line_height = draw.textsize("A", font=current_font)[1] # Get height from textsize
        # --- END MODIFICATION ---

        total_height = len(lines) * line_height + (len(lines) - 1) * 5

        if total_height > 100 or len(lines) > max_lines:
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
                    current_line = word # This line was indented incorrectly in your original code
            # Fixing the indentation for the last line of the loop
            if current_line:
                lines.append(current_line)
            if len(lines) > max_lines:
                lines = lines[:max_lines]
        else:
            break
    # Step 3: Estimate width and shift if needed
    estimated_total_width = max_chars_per_line * len(lines) * 7  # rough pixel estimate
    if estimated_total_width > width_shift_threshold:
        x, y = (x + 40, y - 10)  # extra shift
    elif len(lines) > 1:
        x, y = (x + 20, y - 10)  # default multi-line shift
    else:
        x, y = position  # keep original

    # Step 4: Center vertically around adjusted y
    # --- MODIFIED LINE FOR PILLOW 8.4.0 COMPATIBILITY ---
    # Using textsize again for line_height calculation
    line_height = draw.textsize("A", font=current_font)[1] # Get height from textsize
    # --- END MODIFICATION ---
    total_height = len(lines) * line_height + (len(lines) - 1) * 5
    start_y = y - total_height // 2

    # Step 5: Draw each line
    for line in lines:
        draw.text((x, start_y), line, font=current_font, fill=fill)
        start_y += line_height + 5

    return current_font.size

# Title with stroke
"""
draw_text_with_stroke((100, 260), title, font=font_title, fill="black",stroke_color="black", stroke_width=0)
image_width, _ = base.size
title_width, title_height = draw.textsize(title, font=font_title)

title_x = (image_width - title_width) // 2
title_y = 260 - (title_height // 2)  # Optional: vertically center around 260

draw_text_with_stroke((title_x, title_y), title, font=font_title, fill="black", stroke_color="black", stroke_width=0)
"""
# --- Center-align title around custom X (e.g., 480) ---
custom_center_x = 315
custom_center_y = 285

title_width, title_height = draw.textsize(title, font=font_title)
x = custom_center_x - (title_width // 2)
y = custom_center_y - (title_height // 2)

draw_text_with_stroke((x, y), title, font=font_title, fill="black", stroke_color="black", stroke_width=0)


# Subtitle with dynamic wrapping and positioning
subtitle_text = subtitle

draw_wrapped_text_with_resize(
    draw,
    position=(60, 400),
    text=subtitle_text,
    font=font_subtitle,
    fill="#000"
)

"""
# Names
draw.text((655, 326), facname1, font=font_name, fill="white")
draw.text((835, 326), facname2, font=font_name, fill="white")

# Designations
draw.text((654, 350), facdesc1, font=font_designation, fill="white")
draw.text((855, 350), facdesc2, font=font_designation, fill="white")
"""
# --- Center-aligned Faculty Names and Designations ---
fac1_center_x = 630 + 170 // 2  # = 715
fac2_center_x = 825 + 170 // 2  # = 910

# Name 1
name1_width, _ = draw.textsize(facname1, font=font_name)
draw.text((fac1_center_x - name1_width // 2, 326), facname1, font=font_name, fill="white")

# Name 2
name2_width, _ = draw.textsize(facname2, font=font_name)
draw.text((fac2_center_x - name2_width // 2, 326), facname2, font=font_name, fill="white")

# Designation 1
desc1_width, _ = draw.textsize(facdesc1, font=font_designation)
draw.text((fac1_center_x - desc1_width // 2, 350), facdesc1, font=font_designation, fill="white")

# Designation 2
desc2_width, _ = draw.textsize(facdesc2, font=font_designation)
draw.text((fac2_center_x - desc2_width // 2, 350), facdesc2, font=font_designation, fill="white")


# Date and Time
draw.text((710, 400), date, font=font_date, fill="black")
draw.text((910, 400), time, font=font_time, fill="black")

# Register Now button
draw.text((770, 480), reg, font=font_register, fill="white")

# Save final output
base.save("/var/www/html/thakshith/templatetool1/output/appbanner.png")

