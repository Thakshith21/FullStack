#!/usr/bin/env python3


"""
import cgi
import os
import imghdr
import json
import sys
import traceback

def respond(status, message):
    print("Content-Type: application/json\n")
    response = {"status": status, "message": message}
    print(json.dumps(response))
    sys.exit(0)

try:
    form = cgi.FieldStorage()

    if "imageFile" not in form:
        respond("fail", "No file uploaded")

    file_item = form["imageFile"]
    if not (file_item.file and file_item.filename):
        respond("fail", "Invalid file")

    # Read and validate file type
    file_data = file_item.file.read()
    image_type = imghdr.what(None, h=file_data)
    if image_type != "png":
        respond("fail", "Only PNG files are allowed.")

    # Set existing folder path
    upload_folder = "/var/www/html/thakshith/images/"

    # Validate that folder exists
    if not os.path.isdir(upload_folder):
        respond("fail", f"Upload folder does not exist: {upload_folder}")

    filename = os.path.basename(file_item.filename)
    file_path = os.path.join(upload_folder, filename)

    with open(file_path, "wb") as f:
        f.write(file_data)

    respond("success", f"Image '{filename}' uploaded successfully.")

except Exception:
    error_info = traceback.format_exc()
    respond("fail", f"Server error:\n{error_info}")
"""
import cgi
import os
import imghdr
import json
import sys
import traceback

def respond(status, message):
    print("Content-Type: application/json\n")
    response = {"status": status, "message": message}
    print(json.dumps(response))
    sys.exit(0)

try:
    form = cgi.FieldStorage()

    if "imageFile" not in form:
        respond("fail", "No file uploaded")

    file_item = form["imageFile"]
    if not (file_item.file and file_item.filename):
        respond("fail", "Invalid file")

    # Read and validate file type
    file_data = file_item.file.read()
    image_type = imghdr.what(None, h=file_data)
    if image_type != "png":
        respond("fail", "Only PNG files are allowed.")

    # Upload path (must already exist)
    upload_folder = "/var/www/html/thakshith/templatetool1/facimg/"
    if not os.path.isdir(upload_folder):
        respond("fail", f"Upload folder does not exist: {upload_folder}")

    # Convert filename to lowercase
    original_filename = os.path.basename(file_item.filename)
    filename = original_filename.lower()

    file_path = os.path.join(upload_folder, filename)

    with open(file_path, "wb") as f:
        f.write(file_data)

    respond("success", f"Image '{filename}' uploaded successfully.")

except Exception:
    error_info = traceback.format_exc()
    respond("fail", f"Server error:\n{error_info}")

