#!/usr/bin/env python3

import subprocess
import sys
import cgi
import json

print("Content-Type: application/json\n")  # JSON Response

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

#print(facdesc1 + '\n' + facdesc2 + '\n' + dates + '\n' + times )


"""
title = "Mission JAIIB 2025"
subtitle = "Mission JAIIB and CAIIB whith next ultra leel"
logo = "sbi"
facimg1 = "payal"
facimg2 = "himanshu"
facname1 = "Himanshu Sir"
facname2 = "Payal maam"
facdesc1 = "English Faculty"
facdesc2 = "Reasoning Facul;ty"
date = "June 11"
time = "7 PM"
reg = "RegisterNow"
"""

subprocess.run(["python3", "appbanner.py", template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])

subprocess.run(["python3", "push.py", template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])

subprocess.run(["python3", "popup.py", template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])

subprocess.run(["python3", "ppt.py", tmeplate, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])

subprocess.run(["python3", "desktop.py", template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])

subprocess.run(["python3", "social.py", template, title, subtitle, logo, facimg1, facimg2, facname1, facname2, facdesc1, facdesc2, dates, times, reg])

