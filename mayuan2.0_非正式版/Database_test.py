import sqlite3

conn=sqlite3.connect("mayuan.db")
cu=conn.cursor()
cu.execute("""CREATE TABLE mayuandb(id INTEGER PRIMARY KEY AUTOINCREMENT ,
question TEXT NOT NULL ,
answer TEXT NOT NULL )""")
conn.commit()
conn.close()