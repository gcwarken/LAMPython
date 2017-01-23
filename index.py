#!/usr/bin/python

# Turno on debug mode
import cgitb
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html")
print() # This blank line is ABSOLUTELY necessary. The page will not load correctly without it
print('<head><link rel="stylesheet" href=styles.css></head>')
print("<h1>Python test</h1>")
print('<a href="test.jpg">space</a><br/>')
print('<a href="test.html">html</a><br/>')

# Connect to the database
import pymysql
conn = pymysql.connect(
	db='example',
	user='root',
	passwd='5487',
	host='localhost'
)
c = conn.cursor()

# Insert some example data
c.execute("TRUNCATE numbers")
c.execute("INSERT INTO numbers VALUES (1, 'One!')")
c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
c.execute("INSERT INTO numbers VALUES (3, 'Three')")
conn.commit()

# Print the contents of the database
c.execute("SELECT * FROM numbers")
print([(r[0], r[1]) for r in c.fetchall()])



