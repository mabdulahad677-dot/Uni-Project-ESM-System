import tkinter as ttk

class app(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Test app for project")

        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(padx = 30, pady = 50)

        self.label = ttk.Label(self.login_frame, text = "Login", font = ("Arial", 30))
        self.label.pack()



my_app = app()
my_app.mainloop()
