import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LoadingScreen(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.parent = parent
        self.switch_callback = switch_callback

        self.parent.attributes("-alpha", 0.0)
        self.pack(fill="both", expand=True)

        # ===== CENTER CARD ===== #
        self.card = ctk.CTkFrame(
            self,
            width=320,
            height=200,
            corner_radius=20
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        self.title = ctk.CTkLabel(
            self.card,
            text="MY APPLICATION",
            font=("Arial", 22, "bold")
        )
        self.title.pack(pady=(30, 10))

        # Animated loading text
        self.loading_text = ctk.CTkLabel(
            self.card,
            text="Loading",
            font=("Arial", 14)
        )
        self.loading_text.pack(pady=5, side = "left")

        # Progress bar (indeterminate)
        self.progress = ctk.CTkProgressBar(self.card, width=220)
        self.progress.pack(pady=15)
        self.progress.configure(mode="indeterminate")
        self.progress.start()

        # Animation states
        self.dot_state = 0

        # Start animations
        self.fade_in()
        self.animate_dots()

        self.after(3500, self.fade_out)

    # ===== FADE IN ===== #
    def fade_in(self):
        alpha = self.parent.attributes("-alpha")
        if alpha < 1:
            alpha += 0.04
            self.parent.attributes("-alpha", alpha)
            self.after(30, self.fade_in)

    # ===== DOT ANIMATION ===== #
    def animate_dots(self):
        dots = ["Loading", "Loading.", "Loading..", "Loading..."]
        self.loading_text.configure(text=dots[self.dot_state])

        self.dot_state = (self.dot_state + 1) % len(dots)
        self.after(500, self.animate_dots)

    # ===== FADE OUT ===== #
    def fade_out(self):
        alpha = self.parent.attributes("-alpha")

        if alpha > 0:
            alpha -= 0.05
            self.parent.attributes("-alpha", alpha)
            self.after(25, self.fade_out)
        else:
            self.progress.stop()
            self.switch_callback()


class MainApp(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self,
            text="Welcome to the Main App",
            font=("Arial", 22, "bold")
        ).pack(pady=60)

        ctk.CTkButton(self, text="Exit", command=parent.quit).pack()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x250")
        self.overrideredirect(True)
        self.center_window(400, 250)

        self.loading = LoadingScreen(self, self.show_main)

    def center_window(self, w, h):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw // 2) - (w // 2)
        y = (sh // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def show_main(self):
        self.loading.destroy()

        self.overrideredirect(False)
        self.geometry("600x400")
        self.center_window(600, 400)

        self.attributes("-alpha", 0.0)
        self.main = MainApp(self)

        self.fade_in()

    def fade_in(self):
        alpha = self.attributes("-alpha")
        if alpha < 1:
            alpha += 0.05
            self.attributes("-alpha", alpha)
            self.after(30, self.fade_in)


if __name__ == "__main__":
    app = App()
    app.mainloop()