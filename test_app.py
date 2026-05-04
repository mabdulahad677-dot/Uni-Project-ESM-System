import tkinter as ttk

class app(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Test app for project")

        self.username = ttk.Label(self, text = "Username")
        self.username.pack()
        self.en_username = ttk.Entry(self)
        self.en_username.pack()

        self.password = ttk.Label(self, text="Password")
        self.password.pack()
        self.en_password = ttk.Entry(self)
        self.en_password.pack()

my_app = app()
my_app.mainloop()
