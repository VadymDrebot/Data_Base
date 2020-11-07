def find_click():
    combo.get()
    cur = con.cursor()
    search = find_mes.get()
    cur.execute("""SELECT st_id,surname,name,telefon FROM students """)
    count = 0
    for el in cur:
        for i in range(4):
            if search == el[i]:
                lbl_create = Label(add_window, text=el, font="Arial 14")
                lbl_create.place(x=20, y=170)
                count = 1
    if count == 0:
        lbl_create = Label(add_window, text="Такого студента нет в базе", font="Arial 14")
        lbl_create.place(x=20, y=170)