import tkinter as tk
import tkinter.font as tkFont


class CustomWidget(tk.Frame):
    def __init__(self, parent, title, id, category, is_over, check, circle):
        tk.Frame.__init__(self, parent)

        tk.Frame.config(self, bg="white")

        normal_Font = tkFont.Font(family="Tahoma", size=10, overstrike=0)
        strike_Font = tkFont.Font(family="Tahoma", size=10, overstrike=1)

        self.check = tk.Label(self, image=check if is_over else circle, bg="white")
        self.title = tk.Label(self, text=title, anchor="w", bg="white", fg="black",
                              font=strike_Font if is_over == 1 else normal_Font)
        self.category = tk.Label(self, text=category, anchor="w", bg="white", fg="gray",
                                 font=strike_Font if is_over else normal_Font)
        self.entry = tk.Entry(self)
        self.entry.insert(0, id)

        self.check.place(x=5, y=10)
        self.title.place(x=35, y=5)
        self.category.place(x=35, y=25)

    def get(self):
        return self.entry.get()
