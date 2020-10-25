import sqlite3 as sq
with sq.connect("saper.db") as con:
    cur=con.cursor()

    cur.execute("DROP TABLE worker")
    cur.execute("""CREATE TABLE IF NOT EXISTS worker(surname TEXT PRIMARY KEY,name TEXT,id INTEGER)""")
    users=[('ivanov','ivan',123),('petrov','petya',456),('sidorov','sidor',789)]
    cur.executemany("INSERT INTO worker VALUES(?,?,?)",users)

    cur.execute("DROP TABLE salary")
    cur.execute("""CREATE TABLE IF NOT EXISTS salary(surname TEXT PRIMARY KEY,month$ INTEGER,year$ INTEGER)""")
    cur.execute("INSERT INTO salary(surname,month$,year$) VALUES('ivanov',3000,36000)")
    cur.execute("INSERT INTO salary(surname,month$,year$) VALUES('petrov',4000,48000)")
    cur.execute("INSERT INTO salary(surname,month$,year$) VALUES('sidorov',5000,60000)")

    cur.execute("SELECT * FROM worker ")
    for i in cur:
        print(i)

    cur.execute("SELECT * FROM salary ORDER BY month$ DESC" )
    for i in cur:
        print(i)
    cur.execute("UPDATE salary SET month$=month$+500 WHERE year$=48000")
    for i in cur:
        print(i)