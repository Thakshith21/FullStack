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
base = Image.open("../inputimg/appbanner.png").convert("RGBA")

# Load overlay images
logo = Image.open(f"/var/www/html/thakshith/templatetool/examlogos/irdai-130.png").convert("RGBA")
himanshu = Image.open(f"/var/www/html/thakshith/templatetool/facimg/payal-170.png").convert("RGBA")
sanyam = Image.open(f"/var/www/html/thakshith/templatetool/facimg/himanshu-170.png").convert("RGBA")

# Paste images onto base
base.paste(logo, (260, 70), logo)
base.paste(himanshu, (630, 147), himanshu)
base.paste(sanyam, (825, 148), sanyam)

# Create draw context
draw = ImageDraw.Draw(base)

# Define font paths
bold_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Regular.ttf"

# Load fonts
font_title = ImageFont.truetype(bold_font_path, 50)
font_subtitle = ImageFont.truetype(bold_font_path, 40)
font_name = ImageFont.truetype(bold_font_path, 20)
font_designation = ImageFont.truetype(regular_font_path, 14)
font_date = ImageFont.truetype(regular_font_path, 20)
font_time = ImageFont.truetype(regular_font_path, 24)
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
                                  max_chars_per_line=26, max_lines=3, min_font_size=30,
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
        line_height = draw.textbbox((0, 0), "A", font=current_font)[3]
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
                    current_line = word
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
    line_height = draw.textbbox((0, 0), "A", font=current_font)[3]
    total_height = len(lines) * line_height + (len(lines) - 1) * 5
    start_y = y - total_height // 2

    # Step 5: Draw each line
    for line in lines:
        draw.text((x, start_y), line, font=current_font, fill=fill)
        start_y += line_height + 5

    return current_font.size


# Title with stroke
draw_text_with_stroke((92, 260), title, font=font_title, fill="black",
                      stroke_color="black", stroke_width=0)

# Subtitle with dynamic wrapping and positioning
subtitle_text = subtitle

draw_wrapped_text_with_resize(
    draw,
    position=(64, 400),
    text=subtitle_text,
    font=font_subtitle,
    fill="black"
)

# Names
draw.text((660, 326), facname1, font=font_name, fill="white")
draw.text((845, 326), facname2, font=font_name, fill="white")

# Designations
draw.text((654, 350), facdesc1, font=font_designation, fill="white")
draw.text((855, 350), facdesc2, font=font_designation, fill="white")

# Date and Time
draw.text((710, 400), date, font=font_date, fill="black")
draw.text((910, 400), time, font=font_time, fill="black")

# Register Now button
draw.text((770, 480), reg, font=font_register, fill="white")

# Save final output
base.save("../output/appbanner.png")

#print("Image generated successfully as '02.png'")
