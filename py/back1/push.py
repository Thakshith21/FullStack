from PIL import Image, ImageDraw, ImageFont
import sys

title = sys.argv[1]
subtitle = sys.argv[2]
logo = sys.argv[3]
facimg1 = sys.argv[4]
facimg2 = sys.argv[5]
facname1 = sys.argv[6]
facname2 = sys.argv[7]
facdesig1 = sys.argv[8]
facdesig2 = sys.argv[9]
date = sys.argv[10]
time = sys.argv[11]
reg = sys.argv[12]

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


# Function to wrap text strictly by character limit and draw all lines
def draw_wrapped_text_with_resize(draw, position, text, font, fill,
                                  max_chars_per_line=20, min_font_size=10,
                                  width_shift_threshold=350):
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
        total_height = len(lines) * line_height + (len(lines) - 1) * 2

        if total_height > 150:
            if current_font.size <= min_font_size:
                break
            current_font = ImageFont.truetype(font.path, current_font.size - 1)

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
        x, y = (x + 15, y - 3)
    elif len(lines) > 1:
        x, y = (x + 4, y + 5)
    else:
        x, y = position

    # Step 4: Center vertically around adjusted y
    line_height = draw.textbbox((0, 0), "A", font=current_font)[3]
    total_height = len(lines) * line_height + (len(lines) - 1) * 2
    start_y = y - total_height // 2

    # Step 5: Draw each line
    for line in lines:
        draw.text((x, start_y), line, font=current_font, fill=fill)
        start_y += line_height + 2

    return current_font.size


# --- MAIN SCRIPT ---
base = Image.open("../inputimg/push.png").convert("RGBA")

# Load images
logo = Image.open(f"../examlogos/{logo}-60.png").convert("RGBA")
himanshu = Image.open(f"../facimg/{facimg1}-75.png").convert("RGBA")
sanyam = Image.open(f"../facimg/{facimg2}-75.png").convert("RGBA")

# Paste overlays
base.paste(logo, (100, 10), logo)
base.paste(himanshu, (225, 67), himanshu)
base.paste(sanyam, (300, 68), sanyam)

draw = ImageDraw.Draw(base)

# Font paths
bold_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Bold.ttf"
regular_font_path = "/var/www/html/thakshith/templatetool/fonts/Gilroy-Regular.ttf"

# Load fonts
font_title = ImageFont.truetype(bold_font_path, 20)
font_subtitle = ImageFont.truetype(bold_font_path, 18)
font_name = ImageFont.truetype(bold_font_path, 8)
font_designation = ImageFont.truetype(regular_font_path, 6)
font_date_time = ImageFont.truetype(bold_font_path, 13)
font_register = ImageFont.truetype(bold_font_path, 13)

# Title with stroke
draw_text_with_stroke(
    draw=draw,
    position=(38, 92),
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
    position=(40, 150),
    text=subtitle_text,
    font=font_subtitle,
    fill="black",
    max_chars_per_line=18  # <-- Now using 18 chars per line
)

# Names
draw.text((235, 145), facname1, font=font_name, fill="white")
draw.text((315, 145), facname2, font=font_name, fill="white")

# Designations
draw.text((238, 155), facdesig1, font=font_designation, fill="white")
draw.text((310, 155), facdesig2, font=font_designation, fill="white")

# Date and Time
draw.text((130, 195), date, font=font_date_time, fill="black")
draw.text((238, 195), time, font=font_date_time, fill="black")

# Register Now button
draw.text((153, 233), reg, font=font_register, fill="white")

# Save final image
base.save("../output/push.png")

#print("Banner generated successfully as '02.png'")
