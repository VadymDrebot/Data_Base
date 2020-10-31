import sqlite3
from tkinter import *
from tkinter.ttk import Radiobutton
def click_button():
    nam=message.get()

    con = sqlite3.connect("suppliers.db")
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS suppliers""")
    cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                    id INTEGER PRIMARY KEY,surname TEXT,name TEXT,group_id INTEGER NOT NULL,
                    FOREIGN KEY (group_id) REFERENCES supply_group (group_id)) """)
    users = [(12, 'ivanov', 'ivan', 48), (23, 'petrov', 'petr', 65), (45, 'sidorov', 'sidr', 48)]
    cur.executemany("""INSERT INTO suppliers VALUES(?,?,?,?)""", users)

    a = [78, 'durov', nam, 65]
    cur.execute("""INSERT INTO suppliers VALUES(?,?,?,?)""", a)

    cur.execute("""SELECT name,surname,group_id FROM suppliers """)
    for i in cur:
        print(i)
    con.commit()

    return

window = Tk()
window.title("Работа с базами данных")   # заголовок окна
window.geometry("500x400+600+400")       # ширина и высота окна со смещением

input_lbl = Label(window,text=" input")  # неактивна надпись слева
input_lbl.place(x=20, y=10)

message = StringVar()
txt=Entry(window,textvariable=message)   # ввод с клавиатуры
txt.place(x=120, y=10)
txt.focus()                              # фокус на окно ввода при запуске
                            # message= значение из окна ввода
btn = Button(text=" OK ",command=click_button) # конструктор BUTTON
btn.place(x=350,y=10)



window.mainloop()
con.close()
