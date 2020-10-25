import sqlite3 as sq
with sq.connect("saper.db") as con:
    cur=con.cursor()

    cur.execute("DROP TABLE worker")
    cur.execute("""CREATE TABLE IF NOT EXISTS worker(id INTEGER PRIMARY KEY,surname TEXT,name TEXT)""")
    users=[(123,'ivanov','ivan'),(456,'petrov','petya'),(789,'sidorov','sidor')]
    cur.executemany("INSERT INTO worker VALUES(?,?,?)",users)

    cur.execute("DROP TABLE salary")
    cur.execute("""CREATE TABLE IF NOT EXISTS salary(id INTEGER PRIMARY KEY,month$ INTEGER,year$ INTEGER)""")
    salaries=[(123,3000,36000),(456,4000,48000),(789,5000,60000)]
    cur.executemany("INSERT INTO salary VALUES(?,?,?)", salaries)

    cur.execute("SELECT * FROM worker ")
    for i in cur:
        print(i)

 #   cur.execute("UPDATE salary SET month$=month$+500 WHERE year$=48000")
  #  for i in cur:
   #     print(i)

    cur.execute("SELECT * FROM salary " )
    for i in cur:
        print(i)


    cur.execute("""SELECT surname,month$ FROM worker JOIN salary ON worker.id=salary.id
                WHERE month$>3500""")
    for i in cur:
        print(i)