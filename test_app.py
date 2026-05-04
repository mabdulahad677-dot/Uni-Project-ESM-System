import tkinter as ttk

class app(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Test app for project")
        self.geometry("300x400")

        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(padx = 30, pady = 50)

        self.label = ttk.Label(self.login_frame, text = "Login", font = ("Arial", 30))
        self.label.grid(row = 0, column = 0, columnspan = 2)

        self.u = ttk.Label(self.login_frame, text = "Username")
        self.u.grid(row = 1, column = 0, padx = 10, pady = 5)
        self.ue = ttk.Entry(self.login_frame)
        self.ue.grid(row = 1, column = 1)

        self.p = ttk.Label(self.login_frame, text="Password")
        self.p.grid(row=2, column=0, padx = 10, pady = 5)
        self.pe = ttk.Entry(self.login_frame)
        self.pe.grid(row=2, column=1)

        self.ver = ttk.Label(self.login_frame, text = "ver 1.0.0")
        self.ver.grid(row = 3, column = 0, columnspan = 2)

my_app = app()
my_app.mainloop()
