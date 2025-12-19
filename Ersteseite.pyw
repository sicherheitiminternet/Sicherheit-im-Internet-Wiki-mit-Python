import tkinter as tk

root = tk.Tk()
root.title("Wiki Navigation Hub")
root.geometry("800x500")
root.config(bg="#f2f2f2")

# --- Funktion zum Öffnen von Seiten ---
def open_page(page_name):
    # Neues Fenster
    page = tk.Toplevel(root)
    page.title(page_name)
    page.geometry("800x500")
    page.config(bg="#ffffff")

    # Seitentitel
    title = tk.Label(page, text=page_name,
                     font=("Segoe UI", 20, "bold"),
                     bg="#ffffff", fg="#222222")
    title.pack(pady=20)

    # Beispieltext
    content = tk.Label(page,
        text="Willkommen auf der ersten Wiki-Seite!\nHier kannst du Inhalte einfügen.",
        font=("Segoe UI", 12),
        bg="#ffffff", fg="#333333"
    )
    content.pack(pady=10)

    # Zurück-Button
    back_btn = tk.Button(
        page, text="Zurück zum Hub",
        font=("Segoe UI", 12),
        bg="#e6e6e6", fg="#333333",
        activebackground="#dcdcdc",
        command=page.destroy
    )
    back_btn.pack(pady=30)


# --- Professionelle Navigation Cards ---
def create_card(text, y_pos):
    frame = tk.Frame(root, bg="#ffffff", width=300, height=60,
                     highlightbackground="#d1d1d1", highlightthickness=1)
    frame.place(x=250, y=y_pos)

    label = tk.Label(frame, text=text, fg="#333333", bg="#ffffff",
                     font=("Segoe UI", 14))
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Hover-Effekt
    def on_enter(event):
        frame.config(bg="#e9e9e9")
        label.config(bg="#e9e9e9")

    def on_leave(event):
        frame.config(bg="#ffffff")
        label.config(bg="#ffffff")

    # Klick
    def on_click(event):
        open_page(text)

    frame.bind("<Enter>", on_enter)
    frame.bind("<Leave>", on_leave)
    frame.bind("<Button-1>", on_click)
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<Button-1>", on_click)

create_card("Erste Seite", 200)

root.mainloop()
