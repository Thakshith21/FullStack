import MySQLdb

dbpass = "pats2001"
dbuser = "root"
dbhost = "localhost"
domainname = 'dev.oliveboard.in'

domainpre = 'http://dev.oliveboard.in/request-form/'

def dbget(dbname='courserequests'):
    conn = MySQLdb.connect(dbhost, dbuser, dbpass, dbname)
    cursor= conn.cursor()
    return [conn, cursor]

def dbclose(conn, cursor):
    cursor.close()
    conn.close()
