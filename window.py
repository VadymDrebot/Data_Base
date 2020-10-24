from tkinter import *
clicks = 0
def click_button():
    global clicks
    clicks += 1
    buttonText.set("Clicks{}".format(clicks))
###################################
def create_window(x,y):
    root = Tk()
    root.title(x)
    root.geometry("400x300+200+300")

    btn = Button(root,text=y, padx="30",pady="30",command=click_button())
    btn.pack()
    root.mainloop()

    return
###########################################
#def create_button(x):

 #   return
#####################################
window_name=input("name of window: ")
button_name=input("input name of button: ")
create_window(window_name,button_name)
#create_button(button_name)

