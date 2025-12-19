import tkinter as tk
import webview
import os

pages = [
    "Viren.html", "Rootkits.html", "Trojaner.html",
    "Ransomware.html", "Phishing.html", "DDOS.html", "Webinjection.html",
    "Cybermobbing.html", "Cryptojacking.html", "Glossar.html", "Ressourcen.html", "Haftung.html"
]

def open_page(file_name):
    # Prüfen, ob Datei existiert
    if not os.path.exists(file_name):
        print(f"[Fehler] Datei '{file_name}' existiert nicht!")
        return

    # Vollbild für HTML-Fenster
    webview.create_window(
        file_name.replace(".html",""), 
        os.path.abspath(file_name), 
        fullscreen=True
    )
    webview.start()
    
    # Hub nach Schließen der HTML-Seite wieder öffnen
    start_hub()

def start_hub():
    root = tk.Tk()
    root.title("Owner Wiki Hub")
    
    # Vollbild aktivieren
    root.attributes("-fullscreen", True)
    
    # Escape-Taste zum Verlassen des Vollbilds
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

    root.config(bg="#f4f4f4")

    # Header
    header = tk.Frame(root, bg="#4a90e2", height=100)
    header.pack(fill=tk.X)

    # Titel im Header
    title = tk.Label(header, text="Willkommen bei Sicherheit im Internet", bg="#4a90e2", fg="white",
                     font=("Arial", 24, "bold"))
    title.pack(pady=10)

    # Buttons horizontal unter dem Titel
    nav_frame = tk.Frame(header, bg="#4a90e2")
    nav_frame.pack(pady=5)

    def on_enter(e):
        e.widget.config(bg="#357ABD")
    def on_leave(e):
        e.widget.config(bg="#4a90e2")

    for page in pages:
        btn = tk.Button(nav_frame, text=page.replace(".html",""),
                        bg="#4a90e2", fg="white", font=("Arial", 12, "bold"),
                        padx=15, pady=8, bd=0, relief="raised",
                        command=lambda p=page, r=root: [r.destroy(), open_page(p)])
        btn.pack(side=tk.LEFT, padx=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Hauptbereich
    main_area = tk.Frame(root, bg="white", bd=0)
    main_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    main_label = tk.Label(
        main_area,
        text="Willkommen und schön, dass Sie hier sind!\nDieses Wiki hilft Ihnen, sicher im Internet unterwegs zu sein. Klicken Sie auf die Seiten oben, um mehr zu lernen.",
        bg="white",
        fg="#333333",
        font=("Arial", 28, "bold"),
        justify="center"
    )
    main_label.pack(expand=True)
    
    # Footer
    footer = tk.Frame(root, bg="#4a90e2", height=80)
    footer.pack(side=tk.BOTTOM, fill=tk.X)

    footer_label = tk.Label(
        footer,
        text="© 2025 Sicherheit im Internet Wiki",
        bg="#4a90e2",
        fg="white",
        font=("Arial", 18, "bold")
    )
    footer_label.pack(expand=True)

    root.mainloop()

# Hub starten
start_hub()
