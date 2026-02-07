import MySQLdb

dbpass = ""
dbuser = ""
dbhost = "localhost"
domainname = ''

domainpre = ''

def dbget(dbname='courserequests'):
    conn = MySQLdb.connect(dbhost, dbuser, dbpass, dbname)
    cursor= conn.cursor()
    return [conn, cursor]

def dbclose(conn, cursor):
    cursor.close()
    conn.close()
