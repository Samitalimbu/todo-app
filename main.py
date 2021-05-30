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


def click_task(task_id):
    add_task_screen(task_id)


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
        uid = db.login(username.get(), password.get())
        if uid > 0:
            home_screen()
        else:
            messagebox.showwarning("Login Failed", "Invalid username or password")

    Button(login_window, text="Login", border=0, fg="white", image=img_btn, compound="center", command=login) \
        .place(x=20, y=340, height=50, width=260)

    Label(login_window, text="Don't have account ?").place(x=20, y=390)
    Button(login_window, text="Sign Up", bg="#F0F0F0", border=0, fg="blue", command=register_screen).place(x=135, y=390)


def register_screen():
    global logo, bg, img_btn, register_window
    login_window.withdraw()
    register_window.title("Register")
    register_window.geometry("300x550")
    register_window.geometry("+530+50")
    register_window.resizable(False, False)
    register_window.deiconify()

    img_btn = ImageTk.PhotoImage(Image.open("./images/btn_long.png"))
    logo = ImageTk.PhotoImage(Image.open("./images/logo.png"))

    Label(register_window, image=logo).place(x=120, y=20)

    bg = ImageTk.PhotoImage(Image.open("./images/bg.PNG"))
    Label(register_window, image=bg).place(x=0, y=470)

    Label(register_window, text="ToDo App", font=("Tahoma", 11)).place(x=115, y=70)

    font = ("Tahoma", 10)

    Label(register_window, text="Full Name").place(x=20, y=130)
    name = Entry(register_window, bg="white", border=0, font=font)
    name.place(x=20, y=150, height=25, width=260)

    Label(register_window, text="Username").place(x=20, y=180)
    username = Entry(register_window, bg="white", border=0, font=font)
    username.place(x=20, y=200, height=25, width=260)

    blood_group = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    blood = StringVar()
    blood.set("A+")
    Label(register_window, text="Blood Group").place(x=20, y=230)
    option_blood = OptionMenu(register_window, blood, *blood_group)
    option_blood.config(bg="white", border=0)
    option_blood["menu"].config(bg="white")
    option_blood.place(x=20, y=250, height=25, width=260)

    Label(register_window, text="Age").place(x=20, y=280)
    age = Entry(register_window, bg="white", border=0, font=font)
    age.place(x=20, y=300, height=25, width=260)

    Label(register_window, text="Password").place(x=20, y=330)
    password = Entry(register_window, show="\u2022", bg="white", border=0, font=font)
    password.place(x=20, y=350, height=25, width=260)

    def register():
        db.register(name.get(), username.get(), blood.get(), age.get(), password.get())
        messagebox.showinfo("Success", "User Created Successfully")
        login_screen()

    Button(register_window, text="Register", border=0, fg="white", image=img_btn, compound="center", command=register) \
        .place(x=20, y=380, height=50, width=260)

    Label(register_window, text="Already have account ?").place(x=20, y=430)
    Button(register_window, text="Login", bg="#F0F0F0", border=0, fg="blue", command=login_screen).place(x=145, y=430)


def home_screen():
    window.deiconify()
    window.geometry("300x600")
    window.geometry("+550+50")
    window.resizable(False, False)
    window.title("Todo App")
    login_window.withdraw()

    global header, add
    add = ImageTk.PhotoImage(Image.open("./images/plus.png"))
    header = ImageTk.PhotoImage(Image.open("./images/header.png"))
    Label(window, image=header).place(x=0, y=0, width=300, height=200)

    today = date.today()
    today = today.strftime("%B %d, %Y")

    name = db.get_name(uid)
    lbl_name = Label(window, text=name, font=("Arial", 12, "normal"), bg="black", fg="white")
    lbl_name.place(x=10, y=150)
    Label(window, text=today, bg="black", fg="white").place(x=10, y=170)
    Button(window, image=add, border=0, command=lambda: add_task_screen(-1)).place(x=250, y=150)

    y_axis = 0

    for row in db.get_all_task(uid):
        tsk = widget.CustomWidget(content_frame, row[2], row[0], row[3], row[5], check, circle)
        tsk.bind("<Button-1>", lambda event, pos=row[0]: click_task(pos))
        tsk.place(x=0, y=y_axis, height=50, width=300)
        y_axis += 52


def add_task_screen(task_id):
    window.withdraw()
    add_task_window.deiconify()
    add_task_window.geometry("300x320")
    add_task_window.geometry("+550+130")
    add_task_window.resizable(False, False)
    add_task_window.title("Add New Task")
    global title_icon, category_icon, desc_icon
    title_icon = ImageTk.PhotoImage(Image.open("./images/title.png"))
    category_icon = ImageTk.PhotoImage(Image.open("./images/category.png"))
    desc_icon = ImageTk.PhotoImage(Image.open("./images/description.png"))

    ttk.Style().configure('pad.TEntry', padding='25 1 1 1')

    Label(add_task_window, text="Title").place(x=10, y=10)
    title = Entry(add_task_window, borderwidth=0)
    title.place(x=40, y=30, height=25, width=250)
    Label(add_task_window, image=title_icon, bg="white").place(x=10, y=30, width=30, height=25)

    Label(add_task_window, text="Category").place(x=10, y=65)
    category = Entry(add_task_window, borderwidth=0)
    category.place(x=40, y=85, height=25, width=250)
    Label(add_task_window, image=category_icon, bg="white").place(x=10, y=85, width=30, height=25)

    Label(add_task_window, text="Description").place(x=10, y=115)
    desc = Entry(add_task_window, borderwidth=0)
    desc.place(x=40, y=135, height=60, width=250)
    Label(add_task_window, image=desc_icon, bg="white").place(x=10, y=135, width=30, height=60)

    def change():
        var1.set(1) if var1.get() == 1 else var1.set(0)

    def on_closing():
        add_task_window.destroy()
        window.deiconify()

    def add_task():
        db.add_task(title.get(), category.get(), desc.get(), var1.get(), uid)
        messagebox.showinfo("Success", "Task added successfully!!!")
        add_task_window.withdraw()
        home_screen()

    def update_task():
        if db.update_task(task_id, title.get(), category.get(), desc.get(), var1.get()):
            messagebox.showinfo("Success", "Task updated successfully!!!")
            add_task_window.withdraw()
            home_screen()
        else:
            messagebox.showerror("Failed", "Failed to update task")

    def delete_task():
        if db.delete_task(task_id):
            messagebox.showinfo("Success", "Task deleted successfully!!!")
            add_task_window.withdraw()

            global content_frame
            for w in content_frame.winfo_children():
                w.destroy()

            y_axis = 0

            for row in db.get_all_task(uid):
                tsk = widget.CustomWidget(content_frame, row[2], row[0], row[3], row[5], check, circle)
                tsk.bind("<Button-1>", lambda event, pos=row[0]: click_task(pos))
                tsk.place(x=0, y=y_axis, height=50, width=300)
                y_axis += 52

            home_screen()
        else:
            messagebox.showerror("Failed", "Failed to update task")

    add_task_window.protocol("WM_DELETE_WINDOW", on_closing)

    var1 = IntVar()
    chk = Checkbutton(add_task_window, text='Completed', variable=var1, onvalue=1, offvalue=0, command=change)

    global img_btn
    img_btn = ImageTk.PhotoImage(Image.open("./images/btn_long.png"))
    Button(add_task_window, text="Update" if task_id > 0 else "Save", border=0, fg="white", image=img_btn,
           compound="center", command=update_task if task_id > 0 else add_task) \
        .place(x=10, y=230, height=50, width=280)

    if task_id > 0:
        chk.place(x=10, y=200)
        Button(add_task_window, text="Delete", border=0, fg="white", image=img_btn,
               compound="center", command=delete_task) \
            .place(x=10, y=270, height=50, width=280)
        for row in db.get_task(task_id):
            title.insert(0, row[2])
            category.insert(0, row[3])
            desc.insert(0, row[4])
            var1.set(row[5])


db.create_table()

login_screen()
register_window.withdraw()
add_task_window.withdraw()
window.withdraw()
window.mainloop()
