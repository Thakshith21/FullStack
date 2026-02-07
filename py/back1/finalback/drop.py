import sys
import dbhelper
import urllib

[conn, cursor] = dbhelper.dbget("templatetool")


cursor.execute("select id, name, desc1 from liveclasses.faculty")
res = cursor.fetchall()
html = ''
for row in res:
    [facid, name, desc1] = row
    name = urllib.unquote_plus(name)
    desc1 = urllib.unquote_plus(desc1)
    name1 = name.split(" ")[0].lower()
    html+= '<option value = "%s" data-img="facimg/%s" data-name="%s" data-desc="%s">%s</option>'%(name1, name1, name, desc1, name)
print(html)

"""
cursor.execute("select category_id, name from facimg where status !=0")

res = cursor.fetchall()

html = ''

for row in res:
    [category_id,name] = row
    if category_id == 1:
        name1 = name.capitalize() + " " + "Maam"
        html +='<option value = "%s" data-img="facimg/%s" data-name="%s">%s</option>'%(name, name, name1, name)
    elif category_id ==2:
        name1 = name.capitalize() + " " + "Sir"
        html +='<option value = "%s" data-img="facimg/%s" data-name="%s">%s</option>'%(name, name, name1, name)

"""
cursor.execute("select id, name from examlogos where status !=0")

res1 = cursor.fetchall()

html1 = ''

for row in res1:
    [ids, name] = row
    html1 +='<option value="%s" data-img="examlogos/%s">%s</option>'%(name, name, name)

print(html + '|||' + html1)
dbhelper.dbclose(conn, cursor)
