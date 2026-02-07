#!/usr/bin/env python3

import subprocess
import sys
import cgi
import json

# IMPORTANT: This line must be printed first for CGI to work correctly.
# It tells the web server that the response will be in JSON format.
print("Content-Type: application/json\n")

'''
vals = cgi.FieldStorage()
template = vals.getvalue('template', '').strip()
title = vals.getvalue('title', '').strip()
subtitle = vals.getvalue('subtitle', '').strip()
logo = vals.getvalue('logo', '').strip()
facimg1 = vals.getvalue('facimg1', '').strip()
facimg2 = vals.getvalue('facimg2', '').strip()
facname1 = vals.getvalue('facname1', '').strip()
facname2 = vals.getvalue('facname2', '').strip()
facdesc1 = vals.getvalue('facdesc1', '').strip()
facdesc2 = vals.getvalue('facdesc2', '').strip()
dates = vals.getvalue('dates', '').strip()
times = vals.getvalue('times', '').strip()
reg = vals.getvalue('reg', '').strip()
'''
dates = "15 July"
facdesc1 = "Quant Expert"
#facdesc1 = sys.argv[1]
facdesc2 = "Asst, Manager, BO"
#facdesc2 = sys.argv[2]
facimg1 = "shubham"
facimg2 = "shobhit"
facname1 = "Shubham Sir" 
#facname1 = sys.argv[1] 
facname2 = "Shobhit Mishra"
#facname2 = sys.argv[2]
logo = "ibps"
reg = "Register Now"
subtitle = "Toppers’ Revision Strategy"
template = "yellow"
times = "8 PM"
title = "Target SBI/IBPS 2025"
#title = sys.argv[3]
# List of scripts to run and their arguments
print(subtitle)

"""
scripts_to_run = [
    ("appbanner.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("push.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("popup.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("ppt.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("desktop.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("social.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])
]
"""
scripts_to_run = [
    ("appbannerdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("pushdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("popupdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("pptdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("desktopdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg]),
    ("socialdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])
]

"""
scripts_to_run = [("socialdemo.py", [template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])
        ]
"""
overall_success = True
error_message = ""

for script_name, args in scripts_to_run:
    try:
        # Use check=True to raise CalledProcessError if the command returns a non-zero exit code.
        # For Python versions < 3.7, use stdout=subprocess.PIPE and stderr=subprocess.PIPE
        # instead of capture_output=True or text=True.
        result = subprocess.run(
            ["python3", script_name] + args,
            check=True,
            stdout=subprocess.PIPE, # Capture standard output
            stderr=subprocess.PIPE  # Capture standard error
            # Removed text=True for compatibility with older Python versions
        )
        # If check=True is used, we only reach here if the subprocess was successful.
        # Decode stdout/stderr manually since text=True is removed
        # print(f"Successfully ran {script_name}. Output: {result.stdout.decode('utf-8')}") # For debugging
    except subprocess.CalledProcessError as e:
        overall_success = False
        # Decode stderr manually
        error_message = f"Error running {script_name}: {e.stderr.decode('utf-8')}"
        # print(f"Failed to run {script_name}. Error: {e.stderr.decode('utf-8')}") # For debugging
        break # Stop processing if one script fails
    except FileNotFoundError:
        overall_success = False
        error_message = f"Error: Python interpreter or script '{script_name}' not found."
        break
    except Exception as e:
        overall_success = False
        error_message = f"An unexpected error occurred while running {script_name}: {e}"
        break

response_data = {}
if overall_success:
    response_data['status'] = 1
    response_data['message'] = "All images generated successfully!"
else:
    response_data['status'] = 0
    response_data['message'] = f"Image generation failed: {error_message}"

# Print the JSON response
print(json.dumps(response_data))

# It's good practice to exit explicitly in CGI scripts, though Python will exit anyway.
sys.exit(0)

