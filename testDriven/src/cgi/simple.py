#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import sys
import MySQLdb
import cgitb # enable cgi debugging
cgitb.enable()

### Classes
class Mysql:

    def __init__(self):
        self

    def sql_print_result(self,host,user,passwd,db,sql):
        try:
            db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        except MySQLdb.Error, e:
            error_message="Error %d : %s" % (e.args[0],e.args[1])
            return error_message
        cur = db.cursor()
	try:
            cur.execute(sql)
            rows = cur.fetchall()
	except:
	    error_message="Error while execute SQL => <i>%s</i>" % str(sql)
	    return error_message
        return rows
        db.close()


### Some default config vars
mysql_host="localhost"
mysql_user="root"
mysql_password=""
mysql_database="cdcol"


### Main
pastday = datetime.datetime.now() - datetime.timedelta(days = 3)
rui_sql_today=datetime.datetime.now().strftime("%Y-%m-%d")
rui_sql_pastday=pastday.strftime("%Y-%m-%d")

# use Mysql class above
domysql=Mysql()
sql_statement="select count(*) from cds"
rows=domysql.sql_print_result(mysql_host,mysql_user,mysql_password,mysql_database,sql_statement)
countresult=rows[-1][-1]

if isinstance(countresult, (int, long, float, complex)):
    if countresult > 0:
	http_header="Status: 200 OK\nContent-type: text/html\n\n"
    else:
 	http_header="Status: 501 Not Implemented\nContent-type: text/html\n\n"
else:
    http_header="Status: 500 Internal Server Error\nContent-type: text/html\n\n"


# initialize html header
print http_header
print "<html><body>"

# gci get example => url?param=mytest
#field = cgi.FieldStorage()
#try:
#    print "Field => param : %s<p>" % field["param"].value
#except KeyError, e:
#    print "KeyError: %s<p>" % e
#
#print "Result : %s<br>" % str(countresult)

if not countresult or isinstance(countresult, str):
    print "ERROR: Result is => %s" % countresult
    sys.exit()

if countresult < 1:
    print "<h3>ERROR: Cannot find any data (result %d) equal or greater then %s.</h3>" % (countresult,rui_sql_pastday)
else:
    print "<h2>Status Okay</h2><b>Find %d rows equal or greater then %s.</b><br><br>" % (countresult,rui_sql_pastday)

print "(Used SQL : <i>%s</i>)" % sql_statement


print "</body></html>"