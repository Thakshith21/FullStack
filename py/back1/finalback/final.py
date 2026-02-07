import sys
import cgi
import json

print("Content-Type: application/json\n")  # JSON Response

vals = cgi.FieldStorage()

title = vals.getvalue('title', '').strip()
subtitle = vals.getvalue('subtitle', '').strip()
facimg1 = vals.getvalue('facimg1', '').strip()
facimg2 = vals.getvalue('facimg2', '').strip()
facname1 = vals.getvalue('facname1', '').strip()
facname2 = vals.getvalue('facname2', '').strip()
facdes1 = vals.getvalue('facdes1', '').strip()
facdes2 = vals.getvalue('facdes2', '').strip()
date = vals.getvalue('date', '').strip()
time = vals.getvalue('time', '').strip()
reg = vals.getvalue('reg', '').strip()

print('data')
