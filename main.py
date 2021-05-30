from datetime import date
from tkinter import *
from tkinter import ttk, messagebox

from PIL import Image, ImageTk

import dbhandler as db
import widget

window = Tk()
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
login_window = Toplevel(window)
register_window = Toplevel(window)
add_task_window = Toplevel(window)

icon = PhotoImage(file="./images/logo.png")

login_window.iconphoto(False, icon)
register_window.iconphoto(False, icon)
add_task_window.iconphoto(False, icon)

check = ImageTk.PhotoImage(Image.open("./images/check.png"))
circle = ImageTk.PhotoImage(Image.open("./images/circle.png"))
calendar = ImageTk.PhotoImage(Image.open("./images/calendar.png"))

uid = -1

content_frame = Frame(window)
content_frame.place(x=0, y=200, height=400, width=300)


def login_screen():
    global logo, bg, login_window, img_btn, username_icon, password_icon

    img_btn = ImageTk.PhotoImage(Image.open("./images/btn_long.png"))
    username_icon = ImageTk.PhotoImage(Image.open("./images/username.png"))
    password_icon = ImageTk.PhotoImage(Image.open("./images/password.png"))

    register_window.withdraw()
    login_window.title("Login")
    login_window.geometry("300x550")
    login_window.geometry("+530+50")
    login_window.resizable(False, False)
    login_window.deiconify()

    logo = ImageTk.PhotoImage(Image.open("./images/logo.png"))
    Label(login_window, image=logo).place(x=120, y=80)

    bg = ImageTk.PhotoImage(Image.open("./images/bg.PNG"))
    Label(login_window, image=bg).place(x=0, y=470)

    Label(login_window, text="ToDo App", font=("Tahoma", 11)).place(x=115, y=160)

    font = ("Tahoma", 10)

    Label(login_window, text="Username").place(x=20, y=230)
    Label(login_window, image=username_icon, bg="white").place(x=20, y=250, height=25, width=30)
    username = Entry(login_window, bg="white", border=0, font=font)
    username.place(x=50, y=250, height=25, width=230)

    Label(login_window, text="Password").place(x=20, y=280)
    Label(login_window, image=password_icon, bg="white").place(x=20, y=300, height=25, width=30)
    password = Entry(login_window, show="\u2022", bg="white", border=0, font=font)
    password.place(x=50, y=300, height=25, width=230)

    def login():
        global uid
    Button(login_window, text="Login", border=0, fg="white", image=img_btn, compound="center", command=login) \
        .place(x=20, y=340, height=50, width=260)

    Label(login_window, text="Don't have account ?").place(x=20, y=390)
    Button(login_window, text="Sign Up", bg="#F0F0F0", border=0, fg="blue", command=register_screen).place(x=135, y=390)


login_screen()
register_window.withdraw()
window.withdraw()
window.mainloop()
