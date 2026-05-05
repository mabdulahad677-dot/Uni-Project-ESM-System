from customtkinter import CTkFrame, CTkEntry, CTkLabel

def simple_label_with_entry(window, text, row, column):
    frame = CTkFrame(window, width=400)
    frame.grid(row = row, column = column, padx = 5, pady = 5,ipadx = 3, ipady = 3, sticky = "ew")
    label = CTkLabel(frame, text = text, width=100)
    label.pack(side = "left", anchor = "e")
    entry = CTkEntry(frame, width = 250, border_width=1, corner_radius=0, height = 30)
    entry.pack(side= "left")

    return entry

def password_label_with_entry(window, text, row, column):
    frame = CTkFrame(window, width=400)
    frame.grid(row = row, column = column, padx = 5, pady = 5,ipadx = 3, ipady = 3, sticky = "news")
    label = CTkLabel(frame, text = text, width=100)
    label.pack(side = "left", anchor = "e")
    entry = CTkEntry(frame, width = 250, border_width=1, corner_radius=0, height = 30, show = "*")
    entry.pack(side= "left")

    return entry