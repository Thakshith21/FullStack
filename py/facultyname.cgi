#!/usr/bin/python2

import sys
sys.path.append("/var/www/html/thakshith/obivsinventory/py")
import dbhelper
import urllib
import cgi
import json

print("Content-Type: application/json")
print("")

# Get form data
form = cgi.FieldStorage()
name = form.getvalue('name', '').strip()
desc1 = form.getvalue('desc1', '').strip()

# Encode strings for URL safety
name = urllib.quote_plus(name)
desc1 = urllib.quote_plus(desc1)

response = {}

# Database connection and insert
[conn, cursor] = dbhelper.dbget("liveclasses")

cursor.execute("INSERT INTO faculty (name, desc1) VALUES (%s, %s)", (name, desc1))
conn.commit()

response["status"] = 1 if cursor.rowcount > 0 else 0
response["cid"] = cursor.lastrowid

# Close connection
dbhelper.dbclose(conn, cursor)

# Output JSON response
print(json.dumps(response))

