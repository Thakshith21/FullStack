from PIL import Image, ImageDraw, ImageFont
import sys

title = sys.argv[1]
subtitle = sys.argv[2]
logo = sys.argv[3]
facimg1 = sys.argv[4]
facimg2 = sys.argv[5]
facname1 = sys.argv[6]
facname2 = sys.argv[7]
facdes1 = sys.argv[8]
facdes2 = sys.argv[9]
date = sys.argv[10]
time = sys.argv[11]
reg = sys.argv[12]

# Open base image
base = Image.open("../inputimg/desktop.png").convert("RGBA")

# Load overlay images
logo = Image.open(f"../examlogos/{logo}-60.png").convert("RGBA")
himanshu = Image.open(f"../facimg/{facimg1}-110.png").convert("RGBA")
sanyam = Image.open(f"../facimg/{facimg2}-110.png").convert("RGBA")

# Paste images onto base
base.paste(logo, (110, 3), logo)           # +110+3
base.paste(himanshu, (420, 25), himanshu)  # +420+25
base.paste(sanyam, (540, 25), sanyam)      # +540+25

# Create draw context
draw = ImageDraw.Draw(base)

# Define font paths
bold_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Regular.ttf"

# Load fonts
font_title = ImageFont.truetype(bold_font_path, 25)
font_subtitle = ImageFont.truetype(bold_font_path, 15)
font_name_large = ImageFont.truetype(bold_font_path, 15)
font_name_small = ImageFont.truetype(bold_font_path, 13)
font_designation = ImageFont.truetype(regular_font_path, 9)
font_date = ImageFont.truetype(bold_font_path, 14)
font_time = ImageFont.truetype(bold_font_path, 15)
font_register = ImageFont.truetype(bold_font_path, 24)


# Function to simulate stroke by drawing multiple times
def draw_text_with_stroke(position, text, font, fill, stroke_color="black", stroke_width=1):
    x, y = position
    for dx in range(-stroke_width, stroke_width + 2):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    draw.text(position, text, font=font, fill=fill)


# Title with stroke
draw_text_with_stroke(
    position=(37, 90),
    text=title,
    font=font_title,
    fill="black",
    stroke_color="black",
    stroke_width=0
)


# Subtitle with dynamic wrapping and positioning
def draw_responsive_subtitle(draw, base_position, text, font, fill, max_width=200, max_lines=2):
    default_x, default_y = base_position
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

        if len(lines) <= max_lines or current_font.size <= 8:
            break

        current_font = ImageFont.truetype(font.path, current_font.size - 1)

    # Set X/Y based on number of lines
    if len(lines) == 1:
        x = 30   # single-line: more centered or spaced
        y = 155  # lower position for single line
    else:
        x = 30   # multi-line: more left-aligned
        y = 140  # higher position for multiple lines

    # Draw each line
    for line in lines:
        draw.text((x, y), line, font=current_font, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=current_font)
        h = bbox[3] - bbox[1]
        y += h + 2  # move down for next line

    return current_font.size
# Use the responsive subtitle function
draw_responsive_subtitle(
    draw,
    base_position=(20, 155),  # will auto-adjust y
    text=subtitle,
    #text="5-Month Success RoadMap",
    font=font_subtitle,
    fill="black",
    max_width=200,
    max_lines=3
)


# Names
draw.text((430, 140), facname1, font=font_name_large, fill="white")
draw.text((560, 140), facname2, font=font_name_small, fill="white")


# Designations
draw.text((435, 155), facdes1, font=font_designation, fill="white")
draw.text((555, 155), facdes2, font=font_designation, fill="white")


# Date and Time
draw.text((715, 70), date, font=font_date, fill="black")
draw.text((835, 70), time, font=font_time, fill="black")


# Register Now button (no stroke)
draw.text((705, 115), reg, font=font_register, fill="white")


# Save final output
base.save("../output/desktop.png")
