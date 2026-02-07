#!/usr/bin/python3

import sys
import dbhelper
import urllib.parse


print("Content-Type: application/json")
print()

# Get form data
vals = cgi.FieldStorage()

name = vals.getvalue('name', '').strip()
desc1 = vals.getvalue('desc1', '').strip()

name = urllib.parse.quote(name)
desc1 = urllib.parse.quote(desc1)

response = {}

[conn, cursor] = dbhelper.dbget("liveclasses")

cursor.execute("insert into faculty (name, desc1) values (%s, %s)" , (name, desc1))

conn,commit()

response["status"] = 1 if cursor.rowcount > 0 else 0
response["cid"] = cursor.lastrowid  # Return the inserted record's ID

# Close the database connection
dbhelper.dbclose(conn, cursor)

# Return the JSON response
print(json.dumps(response))
