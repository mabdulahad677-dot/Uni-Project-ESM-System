from customtkinter import CTkFrame, CTkEntry, CTkLabel

def simple_label_with_entry(window, text, row, column):
    frame = CTkFrame(window, width=300, fg_color="transparent")
    frame.grid(row = row, column = column, padx = 5, pady = 5)
    label = CTkLabel(frame,
                        text=text,
                        font = ("Roboto", 15))
    label.grid(row=0,
               column=0,
               padx=5,
               sticky="w")
    en = CTkEntry(frame,
                  width=310,
                  height=35,
                  border_width=1)
    en.grid(row=1,
            column=0)
    return en

def password_label_with_entry(window, text, row, column):
    frame = CTkFrame(window, width=300, fg_color="transparent")
    frame.grid(row = row, column = column, padx = 5, pady = 5)
    label = CTkLabel(frame,
                     text=text,
                        font = ("Roboto", 15))
    label.grid(row      = 0,
               column   = 0,
               padx     = 5,
               sticky   = "w")
    en = CTkEntry(frame,
                  width         = 310,
                  height        = 35,
                  show          = "*",
                  border_width  = 1)
    en.grid(row     = 1,
            column  = 0)
    return en