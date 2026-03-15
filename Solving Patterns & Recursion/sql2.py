import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# cursor.execute("""
# SELECT *
# FROM Students
# """)    

# cursor.execute("INSERT INTO Students VALUES (2,'Mohamed',50)")

conn.commit()

for row in cursor.execute("SELECT * FROM Students"):
    print(row)

conn.close()