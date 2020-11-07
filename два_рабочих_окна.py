from tkinter import *
m_window=Tk()

def click():
    a = message.get()
    input_lbl1 = Label(window, text=a)
    input_lbl1.place(x=20, y=10)

    return
def win():
    global message
    global window
    window = Toplevel()                      # окно в приложении, закрытие окна уничтожит все дочерние виджеты,-
    window.title("Работа с базами данных")   # размещенные в этом окне , но не выключит программу.
    window.geometry("500x400+600+200")

    message = StringVar()
    txt1 = Entry(window, textvariable=message)  # ввод с клавиатуры
    txt1.place(x=120, y=10)
    txt1.focus()

    line="sdsd"
    input_lbl = Label(window, text=line)  # неактивна надпись слева
    input_lbl.place(x=20, y=10)

    btn = Button(window,text=" OK ",command=click) # конструктор BUTTON
    btn.place(x=350,y=10)
    window.mainloop()
    return

def main_window():
    m_window.title("Работа с базами данных")   # заголовок окна
    m_window.geometry("500x400+300+200")

    m_line="sdsd"
    input_lbl = Label(m_window, text=m_line)  # неактивна надпись слева
    input_lbl.place(x=20, y=10)

    btn = Button(m_window,text=" OK ",command=win) # конструктор BUTTON
    btn.place(x=350,y=10)

    m_window.mainloop()
main_window()
