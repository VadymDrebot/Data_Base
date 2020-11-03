from tkinter import *
import sqlite3
con = sqlite3.connect("suppliers.db")
m_window = Tk()
add=[]                                      # пустой список для добавления элементов
def clean_window():                         # очистка экрана
    for i in range(0,400,50):
        lbl_create = Label(m_window, text="                                            "
                                          "                                            "
                                          "                                            "
                                          "                                              " )
        lbl_create.place(x=i, y=1)
    return
def create_suppliers():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS suppliers""")
    cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                    id TEXT PRIMARY KEY,surname TEXT,name TEXT,group_id TEXT) """)
    users = [(12, 'ivanov', 'ivan', 48), (23, 'petrov', 'petr', 65), (45, 'sidorov', 'sidr', 48)]
    cur.executemany("""INSERT INTO suppliers VALUES(?,?,?,?)""", users)
    con.commit()
    return

def create_supply_group():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS supply_group""")
    cur.execute("""CREATE TABLE IF NOT EXISTS supply_group(
                        group_id INTEGER PRIMARY KEY,group_name)""")
    groups = [(48, 'global'), (65, 'local')]
    cur.executemany("""INSERT INTO supply_group VALUES(?,?)""", groups)
    con.commit()
    return

def out_suplliers():
    clean_window()

    cur = con.cursor()
    cur.execute("""SELECT id,surname,name,group_id FROM suppliers """)
    a = 150
    for i in cur:
        lbl_create = Label(m_window, text=i,font="Arial 14")
        lbl_create.place(x=150, y=a)
        a += 40
    return

def out_supply_group():
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT group_id,group_name FROM supply_group """)
    for a in range(200,550,10):
        lbl_create = Label(m_window, text="                          "
                                        "                           ")
        lbl_create.place(x=150, y=a)
    a = 200
    for i in cur:
        lbl_create = Label(m_window, text=i,font="Arial 14")
        lbl_create.place(x=150, y=a)
        a += 40
    return

def add_click():       # кнопка в окне ADD STRING--"добавления новой строки"
    for i in range(4):
       add.append(message[i].get())
    cur = con.cursor()
    cur.execute("""INSERT INTO suppliers (id,surname,name,group_id) VALUES (?,?,?,?)""", add)
    con.commit()
    add_window.after(3,lambda: add_window.destroy())             # закрытие окна через 3 млсек
    return


def add_string():
    global message
    global add_window
    add_window=Toplevel()                                   # создание дополнительного окна
    add_window.title("Работа с базами данных")  # заголовок окна
    add_window.geometry("350x250+700+500")

    line = ["Введите ID","Введите фамилию: ","Введите имя:","Введите group_id:"]
    a=10
    for i in range(4):
        x = line[i]
        input_lbl = Label(add_window, text=x)  # неактивна надпись слева
        input_lbl.place(x=20, y=a)
        a+=30
    message1=StringVar()
    message2=StringVar()
    message3 = StringVar()
    message4 = StringVar()
    message=[message1,message2,message3,message4]
    a = 10
    for i in range(4):
        txt1 = Entry(add_window, textvariable=message[i])  # ввод с клавиатуры
        txt1.place(x=150, y=a)
        a+=30
    btn = Button(add_window, text="    OK    ", command=add_click)  # конструктор BUTTON
    btn.place(x=100, y=150)
    btn = Button(add_window, text="Отмена", state='disable')  # конструктор BUTTON
    btn.place(x=165, y=150)

    add_window.mainloop()
    return




def main_window():

    m_window.title("Работа с базами данных")   # заголовок окна
    m_window.geometry("500x400+300+200")
    mainmenu = Menu(m_window)
    new_menu = Menu()
    edit_menu= Menu()
    view_menu= Menu()
    mainmenu.add_cascade(label="   NEW   ", menu=new_menu)
    new_menu.add_command(label="New SUPPLIERS",command=create_suppliers)
    new_menu.add_command(label="New SUPPLY_GROUP",command=create_supply_group)

    mainmenu.add_cascade(label="   EDIT   ",menu=edit_menu)
    edit_menu.add_command(label="Add string",command=add_string)
    edit_menu.add_command(label="Change string")
    edit_menu.add_command(label="Delete string")

    mainmenu.add_cascade(label="   VIEW   ",menu=view_menu)
    view_menu.add_command(label="View SUPPLIERS",command=out_suplliers)
    view_menu.add_command(label="View SUPPLY_GROUP",command=out_supply_group)
    view_menu.add_separator()
    view_menu.add_command(label="Search in SUPPLIERS")
    view_menu.add_command(label="Search in SUPPLY_GROUP")
    m_window.config(menu=mainmenu)

    #window.after(3000, lambda: window.destroy())  # закрытие окна--3 сек


    m_window.mainloop()
    return

main_window()
