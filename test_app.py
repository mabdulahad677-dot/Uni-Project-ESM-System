import tkinter as ttk

class app(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Test app for project")

        self.label = ttk.Label(self, text = "This is test app for project", font = ("Arial", 30))
        self.label.pack()

my_app = app()
my_app.mainloop()