#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    
                     user="root",       
                     passwd="",
                     db="testdata")      

cur = db.cursor()


#My table looks like this:
#mysql> desc UserList;
#+----------+------+------+-----+---------+-------+
#| Field    | Type | Null | Key | Default | Extra |
#+----------+------+------+-----+---------+-------+
#| Username | text | YES  |     | NULL    |       |
#| Info     | text | YES  |     | NULL    |       |
#+----------+------+------+-----+---------+-------+
#2 rows in set (0.00 sec)

#mysql> select * from UserList;
#+-----------+-----------------+
#| Username  | Info            |
#+-----------+-----------------+
#| TestUser1 | First test user |
#+-----------+-----------------+

cur.execute("SELECT * FROM UserList")

for row in cur.fetchall():
    print row[0],row[1]

# This will print:
# TestUser1 First test user
db.close()
