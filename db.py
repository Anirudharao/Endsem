import sqlite3

conn = sqlite3.connect("datafile")

cursor = conn.cursor()

# cursor.execute("create table Employee (id integer , name text, salary integer)")

cursor.execute("insert into Employee(id, name, salary) values (1, 'Sheldon', 90000)")
cursor.execute("insert into Employee(id, name, salary) values (2, 'Leonard', 90000)")
cursor.execute("insert into Employee (id, name, salary) values (3, 'Raj', 95000)")

q = cursor.execute("select * from Employee where name like :name", {"name":"Raj"})
print(q.fetchall())