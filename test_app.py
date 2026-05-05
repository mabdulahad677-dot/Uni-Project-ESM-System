import customtkinter as ctk
import tkinter as ttk

from Widgets import login_widgets

class app(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Test app for project")
        self.geometry("700x400")

        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(anchor = "center")

        self.label = ttk.Label(self.login_frame, text = "Login", font = ("Calibri", 30))
        self.label.grid(row = 0, column = 0, columnspan = 2)

        self.user = login_widgets.simple_label_with_entry(self.login_frame, "user", 1, 0)
        self.password = login_widgets.password_label_with_entry(self.login_frame, "Password", 2, 0)

        self.btn = ctk.CTkButton(self.login_frame, text = "login", command=self.login_logic)
        self.btn.grid(row = 3, column = 0)


    def login_logic(self):
        print(self.user.get())
        print(self.password.get())
my_app = app()
my_app.mainloop()
