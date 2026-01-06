# import tkinter as tk
# import os
# import sys

# # Get folder of the script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def show_beans():
#     image_path = os.path.join(BASE_DIR, "beans.jpeg")  # <-- match your file name
#     os.system(f'start "" "{image_path}"')

# root = tk.Tk()
# root.title("Beans App")
# root.geometry("300x200")

# # Big BEANS label
# label = tk.Label(root, text="BEANS", font=("Arial", 24))
# label.pack(pady=20)

# # Button to open the image
# button = tk.Button(root, text="Beans", command=show_beans, width=15, height=2)
# button.pack()

# root.mainloop()








# import os
# import sys
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *

# # Get folder of the script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def show_beans():
#     image_path = os.path.join(BASE_DIR, "beans.jpeg")
#     os.system(f'start "" "{image_path}"')

# # Create a modern themed window
# app = tb.Window(
#     title="Beans App",
#     themename="superhero",  # Dark theme, looks modern
#     size=(400, 300)
# )

# # Big modern label
# label = tb.Label(
#     app,
#     text="BEANS",
#     font=("Segoe UI", 30, "bold"),
#     bootstyle=INFO
# )
# label.pack(pady=40)

# # Modern button
# button = tb.Button(
#     app,
#     text="Beans",
#     command=show_beans,
#     bootstyle=SUCCESS,  # green modern button
#     width=15
# )
# button.pack(pady=10)

# app.mainloop()


















# import os
# import random
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import pyttsx3

# # Get folder of the script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Initialize TTS engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # speaking speed

# # Beans image function
# def show_beans():
#     image_path = os.path.join(BASE_DIR, "beans.jpeg")
#     os.system(f'start "" "{image_path}"')

# # Random Bart line function using TTS
# def bart_line():
#     lines = [
#         "Eat my shorts!",
#         "Ay caramba!",
#         "Don't have a cow, man!",
#         "Cowabunga!",
#         "I'm Bart Simpson, who the hell are you?",
#         "Get bent!"
#     ]
#     chosen = random.choice(lines)
#     engine.say(chosen)
#     engine.runAndWait()

# # Create modern themed window
# app = tb.Window(
#     title="Beans App",
#     themename="superhero",    # Dark modern theme
#     size=(400, 300)
# )
# app.geometry("400x300")
# app.minsize(300, 200)

# # Main frame with padding
# main_frame = tb.Frame(app, padding=20, bootstyle=PRIMARY)
# main_frame.pack(expand=True, fill=BOTH)

# # Responsive label
# label = tb.Label(main_frame, text="BEANS", bootstyle=INFO)
# label.pack(expand=True, fill=BOTH, pady=(0,20))

# # Function to resize label text dynamically
# def resize_text(event):
#     new_size = max(14, int(event.height / 6))
#     label.config(font=("Segoe UI", new_size, "bold"))

# app.bind("<Configure>", resize_text)

# # Beans button
# button_beans = tb.Button(
#     main_frame,
#     text="Beans",
#     command=show_beans,
#     bootstyle=SUCCESS,
#     width=20
# )
# button_beans.pack(pady=(0,10))

# # Bart button with TTS
# button_bart = tb.Button(
#     main_frame,
#     text="Random Bart Line",
#     command=bart_line,
#     bootstyle=INFO,
#     width=20
# )
# button_bart.pack(pady=(0,10))

# # Set EXE / taskbar icon
# try:
#     app.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# app.mainloop()

























# import os
# import random
# import threading
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import pyttsx3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # ---------------- TTS ----------------
# engine = pyttsx3.init()
# engine.setProperty('rate', 180)

# def bart_line():
#     def speak():
#         lines = [
#             "Eat my shorts!",
#             "Ay caramba!",
#             "Don't have a cow, man!",
#             "Cowabunga!",
#             "Get bent!"
#         ]
#         engine.stop()
#         engine.say(random.choice(lines))
#         engine.runAndWait()

#     threading.Thread(target=speak, daemon=True).start()

# # ---------------- BEANS ----------------
# def show_beans():
#     os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')

# # ---------------- WINDOW ----------------
# app = tb.Window(
#     title="Beans App",
#     themename="vapor",   # 🔥 AERO-LIKE THEME
#     size=(420, 300)
# )

# app.minsize(360, 260)

# try:
#     app.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# # ---------------- MAIN AERO PANEL ----------------
# panel = tb.Frame(
#     app,
#     padding=(30, 25),
#     bootstyle="light"
# )
# panel.place(relx=0.5, rely=0.5, anchor=CENTER)

# # ---------------- TITLE ----------------
# title = tb.Label(
#     panel,
#     text="BEANS",
#     font=("Segoe UI", 30),
#     bootstyle="primary"
# )
# title.pack(pady=(0, 20))

# # ---------------- BUTTONS ----------------
# btn_beans = tb.Button(
#     panel,
#     text="Show Beans",
#     command=show_beans,
#     bootstyle="primary",
#     width=22
# )
# btn_beans.pack(pady=(0, 10))

# btn_bart = tb.Button(
#     panel,
#     text="Random Bart Line",
#     command=bart_line,
#     bootstyle="info",
#     width=22
# )
# btn_bart.pack()

# # ---------------- SOFT RESIZE (AERO STYLE) ----------------
# def on_resize(event):
#     w = event.width
#     if w < 420:
#         title.configure(font=("Segoe UI", 24))
#     elif w < 520:
#         title.configure(font=("Segoe UI", 28))
#     else:
#         title.configure(font=("Segoe UI", 32))

# app.bind("<Configure>", on_resize)

# app.mainloop()


























# import tkinter as tk
# from tkinter import ttk
# import os
# import random
# import threading
# import pyttsx3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # --------- TTS ----------
# engine = pyttsx3.init()
# engine.setProperty("rate", 180)

# def bart_line():
#     def speak():
#         lines = [
#             "Eat my shorts!",
#             "Ay caramba!",
#             "Don't have a cow, man!",
#             "Cowabunga!",
#             "Get bent!"
#         ]
#         engine.stop()
#         engine.say(random.choice(lines))
#         engine.runAndWait()

#     threading.Thread(target=speak, daemon=True).start()

# def show_beans():
#     os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')

# # --------- WINDOW ----------
# root = tk.Tk()
# root.title("Beans App")
# root.geometry("420x300")
# root.minsize(360, 260)

# try:
#     root.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# # --------- STYLE ----------
# style = ttk.Style()
# style.theme_use("vista")  # 🔥 THIS IS KEY (AERO)

# style.configure(
#     "TButton",
#     font=("Segoe UI", 10),
#     padding=8
# )

# style.configure(
#     "Title.TLabel",
#     font=("Segoe UI", 28, "bold")
# )

# # --------- LAYOUT ----------
# container = ttk.Frame(root, padding=20)
# container.pack(expand=True)

# title = ttk.Label(container, text="BEANS", style="Title.TLabel")
# title.pack(pady=(10, 25))

# btn_beans = ttk.Button(container, text="Show Beans", command=show_beans)
# btn_beans.pack(pady=(0, 10), ipadx=20)

# btn_bart = ttk.Button(container, text="Random Bart Line", command=bart_line)
# btn_bart.pack(ipadx=20)

# # --------- SMOOTH RESIZE ----------
# def on_resize(event):
#     w = event.width
#     if w < 420:
#         title.config(font=("Segoe UI", 22, "bold"))
#     elif w < 520:
#         title.config(font=("Segoe UI", 26, "bold"))
#     else:
#         title.config(font=("Segoe UI", 30, "bold"))

# root.bind("<Configure>", on_resize)

# root.mainloop()





























# import tkinter as tk
# from tkinter import ttk
# import os
# import random
# import threading
# import pyttsx3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # ---------- FUNCTIONS ----------

# def show_beans():
#     os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')

# def bart_line():
#     def speak():
#         engine = pyttsx3.init()   # NEW ENGINE EVERY TIME
#         engine.setProperty("rate", 185)
#         lines = [
#             "Eat my shorts!",
#             "Ay caramba!",
#             "Don't have a cow, man!",
#             "Cowabunga!",
#             "Get bent!"
#         ]
#         engine.say(random.choice(lines))
#         engine.runAndWait()
#         engine.stop()

#     threading.Thread(target=speak, daemon=True).start()

# # ---------- WINDOW ----------

# root = tk.Tk()
# root.title("Beans App")
# root.geometry("520x360")
# root.minsize(420, 300)

# try:
#     root.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# # ---------- AERO STYLE ----------
# style = ttk.Style()
# style.theme_use("vista")

# style.configure("TButton", font=("Segoe UI", 10), padding=10)
# style.configure("Title.TLabel", font=("Segoe UI", 32, "bold"))

# # ---------- GRID LAYOUT ----------
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# container = ttk.Frame(root, padding=20)
# container.grid(row=0, column=0, sticky="nsew")

# container.columnconfigure(0, weight=1)
# for i in range(4):
#     container.rowconfigure(i, weight=1)

# title = ttk.Label(container, text="BEANS", style="Title.TLabel")
# title.grid(row=0, column=0, pady=(20, 30))

# btn_beans = ttk.Button(container, text="Show Beans", command=show_beans)
# btn_beans.grid(row=1, column=0, pady=8, ipadx=25)

# btn_bart = ttk.Button(container, text="Random Bart Line", command=bart_line)
# btn_bart.grid(row=2, column=0, pady=8, ipadx=25)

# # ---------- SMOOTH SCALING ----------
# def resize(event):
#     w = event.width
#     size = max(22, min(38, w // 14))
#     title.config(font=("Segoe UI", size, "bold"))

# root.bind("<Configure>", resize)

# root.mainloop()






























# import tkinter as tk
# from tkinter import ttk
# import os
# import random
# import threading
# import pyttsx3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # ---------- TTS HELPERS ----------

# def speak(text, rate=185):
#     engine = pyttsx3.init()
#     engine.setProperty("rate", rate)
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

# # ---------- ACTIONS ----------

# def show_beans():
#     def task():
#         speak("showing beans!", rate=190)
#         os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')

#     threading.Thread(target=task, daemon=True).start()

# def bart_line():
#     def task():
#         lines = [
#             "Eat my shorts!",
#             "Ayy caramba!",
#             "Don't have a cow man!",
#             "Cowabunga!",
#             "Get absolutley bent!"
#         ]
#         speak(random.choice(lines), rate=185)

#     threading.Thread(target=task, daemon=True).start()

# # ---------- WINDOW ----------

# root = tk.Tk()
# root.title("Beans App")
# root.geometry("520x360")
# root.minsize(420, 300)

# try:
#     root.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# # ---------- STYLE (AERO / VISTA) ----------

# style = ttk.Style()
# style.theme_use("vista")

# style.configure(
#     "Title.TLabel",
#     font=("Segoe UI", 32, "bold"),
#     anchor="center"
# )

# style.configure(
#     "TButton",
#     font=("Segoe UI", 11),
#     padding=(18, 10)
# )

# # ---------- LAYOUT ----------

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# container = ttk.Frame(root)
# container.grid(row=0, column=0, sticky="nsew")

# container.columnconfigure(0, weight=1)
# container.rowconfigure(0, weight=3)
# container.rowconfigure(1, weight=1)
# container.rowconfigure(2, weight=1)

# title = ttk.Label(container, text="BEANS", style="Title.TLabel")
# title.grid(row=0, column=0, pady=(40, 25))

# btn_beans = ttk.Button(container, text="Show Beans", command=show_beans)
# btn_beans.grid(row=1, column=0, pady=8)

# btn_bart = ttk.Button(container, text="Random Bart Line", command=bart_line)
# btn_bart.grid(row=2, column=0, pady=8)

# # ---------- STABLE SCALING ----------

# def resize(event):
#     width = root.winfo_width()
#     size = max(26, min(40, width // 13))
#     title.configure(font=("Segoe UI", size, "bold"))

# root.bind("<Configure>", resize)

# root.mainloop()







































# import tkinter as tk
# from tkinter import ttk
# import os
# import random
# import threading
# import pyttsx3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # ---------- TTS ----------

# def speak(text, rate=185, pitch_voice=True):
#     engine = pyttsx3.init()
#     engine.setProperty("rate", rate)

#     if pitch_voice:
#         for v in engine.getProperty("voices"):
#             if "child" in v.name.lower() or "male" in v.name.lower():
#                 engine.setProperty("voice", v.id)
#                 break

#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

# # ---------- ACTIONS ----------

# def show_beans():
#     def task():
#         speak("here is some beans!", rate=190, pitch_voice=False)
#         os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')
#     threading.Thread(target=task, daemon=True).start()

# def bart_line():
#     def task():
#         lines = [
#             "Eat my shorts!",
#             "Ay caramba!",
#             "Don't have a cow, man!",
#             "Cowabunga!",
#             "Get bent!"
#         ]
#         speak(random.choice(lines), rate=210, pitch_voice=True)
#     threading.Thread(target=task, daemon=True).start()

# def random_words():
#     def task():
#         words = [
#             "beans",
#             "skateboard",
#             "go to detention",
#             "chalkboard",
#             "cowabunga",
#             "mischief",
#             "Mr skinner",
#             "donuts",
#             "HOMER",
#         ]
#         speak(" ".join(random.sample(words, 3)), rate=180, pitch_voice=False)
#     threading.Thread(target=task, daemon=True).start()

# # ---------- WINDOW ----------

# root = tk.Tk()
# root.title("Beans App")
# root.geometry("520x360")
# root.minsize(420, 300)
# root.configure(bg="#0e0e0e")

# try:
#     root.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# # ---------- DARK STYLE ----------

# style = ttk.Style()
# style.theme_use("default")

# style.configure(
#     "Dark.TFrame",
#     background="#0e0e0e"
# )

# style.configure(
#     "Title.TLabel",
#     background="#0e0e0e",
#     foreground="#e30000",
#     font=("Segoe UI", 34, "bold")
# )

# style.configure(
#     "Dark.TButton",
#     background="#1f1f1f",
#     foreground="#ffffff",
#     font=("Segoe UI", 11),
#     padding=(20, 12),
#     borderwidth=0
# )

# style.map(
#     "Dark.TButton",
#     background=[("active", "#2a2a2a")]
# )

# # ---------- LAYOUT ----------

# container = ttk.Frame(root, style="Dark.TFrame")
# container.pack(expand=True, fill="both")

# title = ttk.Label(container, text="BEANS", style="Title.TLabel")
# title.pack(pady=(40, 25))

# btn_beans = ttk.Button(
#     container,
#     text="Show Beans",
#     style="Dark.TButton",
#     command=show_beans
# )
# btn_beans.pack(pady=6)

# btn_bart = ttk.Button(
#     container,
#     text="Random Bart Line",
#     style="Dark.TButton",
#     command=bart_line
# )
# btn_bart.pack(pady=6)

# btn_words = ttk.Button(
#     container,
#     text="Random Words",
#     style="Dark.TButton",
#     command=random_words
# )
# btn_words.pack(pady=6)

# # ---------- SMOOTH SCALING ----------

# def resize(event):
#     w = root.winfo_width()
#     size = max(28, min(42, w // 12))
#     title.configure(font=("Segoe UI", size, "bold"))

# root.bind("<Configure>", resize)

# root.mainloop()






























# import tkinter as tk
# import os
# import random
# import threading
# import pyttsx3
# import winsound
# import ctypes

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # ---------- FONT ----------

# FONT_PATH = os.path.join(BASE_DIR, "BeansFont.ttf")
# if os.path.exists(FONT_PATH):
#     ctypes.windll.gdi32.AddFontResourceW(FONT_PATH)
#     TITLE_FONT = ("BeansFont", 38, "bold")
# else:
#     TITLE_FONT = ("Segoe UI", 38, "bold")

# # ---------- SOUND ----------

# def play_click():
#     try:
#         winsound.PlaySound(
#             winsound.SND_FILENAME | winsound.SND_ASYNC
#         )
#     except:
#         pass

# # ---------- TTS ----------

# def speak(text, rate=185, pitch_voice=True):
#     engine = pyttsx3.init()
#     engine.setProperty("rate", rate)

#     if pitch_voice:
#         for v in engine.getProperty("voices"):
#             if "male" in v.name.lower():
#                 engine.setProperty("voice", v.id)
#                 break

#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

# # ---------- ACTIONS ----------

# def show_beans():
#     def task():
#         play_click()
#         speak("here is some beans!", 190, False)
#         os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')
#     threading.Thread(target=task, daemon=True).start()

# def bart_line():
#     def task():
#         play_click()
#         lines = [
#             "Eat my shorts!",
#             "Ay caramba!",
#             "Don't have a cow, man!",
#             "Cowabunga!",
#             "Get bent!"
#         ]
#         speak(random.choice(lines), 215, True)
#     threading.Thread(target=task, daemon=True).start()

# def random_words():
#     def task():
#         play_click()
#         words = [
#             "beans",
#             "skateboard",
#             "go to detention",
#             "chalkboard",
#             "cowabunga",
#             "mischief",
#             "Mr Skinner",
#             "donuts",
#             "HOMER"
#         ]
#         speak(" ".join(random.sample(words, 3)), 180, False)
#     threading.Thread(target=task, daemon=True).start()

# # ---------- WINDOW ----------

# root = tk.Tk()
# root.title("Beans App")
# root.geometry("600x420")
# root.configure(bg="#0b0b0b")
# root.attributes("-alpha", 0.0)

# try:
#     root.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
# except:
#     pass

# # ---------- FADE IN ----------

# def fade_in(a=0.0):
#     a += 0.05
#     if a <= 1:
#         root.attributes("-alpha", a)
#         root.after(20, fade_in, a)

# fade_in()

# # ---------- CARD ----------

# card = tk.Frame(
#     root,
#     bg="#141414",
#     highlightthickness=1,
#     highlightbackground="#2a2a2a"
# )
# card.place(relx=0.5, rely=0.5, anchor="center", width=440, height=320)

# title = tk.Label(
#     card,
#     text="BEANS",
#     font=TITLE_FONT,
#     bg="#141414",
#     fg="#e30000"
# )
# title.pack(pady=(32, 26))

# # ---------- BUTTON FACTORY ----------

# def glow_button(text, command):
#     btn = tk.Label(
#         card,
#         text=text,
#         bg="#1f1f1f",
#         fg="white",
#         font=("Segoe UI", 11),
#         padx=26,
#         pady=12,
#         cursor="hand2"
#     )

#     def enter(e):
#         btn.config(bg="#2a2a2a", padx=28, pady=13)

#     def leave(e):
#         btn.config(bg="#1f1f1f", padx=26, pady=12)

#     def click(e):
#         btn.config(bg="#3a3a3a")
#         command()

#     btn.bind("<Enter>", enter)
#     btn.bind("<Leave>", leave)
#     btn.bind("<Button-1>", click)
#     return btn

# glow_button("Show Beans", show_beans).pack(pady=6)
# glow_button("Random Bart Line", bart_line).pack(pady=6)
# glow_button("Random Words", random_words).pack(pady=6)

# # ---------- RESPONSIVE TITLE ----------

# def resize(event):
#     w = root.winfo_width()
#     size = max(28, min(44, w // 12))
#     title.config(font=(TITLE_FONT[0], size, "bold"))

# root.bind("<Configure>", resize)

# root.mainloop()

























import tkinter as tk
import os
import random
import threading
import pyttsx3
import ctypes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- FONT ----------

FONT_PATH = os.path.join(BASE_DIR, "BeansFont.ttf")
if os.path.exists(FONT_PATH):
    ctypes.windll.gdi32.AddFontResourceW(FONT_PATH)
    TITLE_FONT = ("BeansFont", 38, "bold")
else:
    TITLE_FONT = ("Segoe UI", 38, "bold")

# ---------- TTS ----------

def speak(text, rate=185, pitch_voice=True):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)

    if pitch_voice:
        for v in engine.getProperty("voices"):
            if "male" in v.name.lower():
                engine.setProperty("voice", v.id)
                break

    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ---------- ACTIONS ----------

def show_beans():
    def task():
        speak("here is some beans!", 190, False)
        os.system(f'start "" "{os.path.join(BASE_DIR, "beans.jpeg")}"')
    threading.Thread(target=task, daemon=True).start()

def bart_line():
    def task():
        lines = [
            "Eat my shorts!",
            "Ay caramba!",
            "Don't have a cow, man!",
            "Cowabunga!",
            "Get bent!"
        ]
        speak(random.choice(lines), 215, True)
    threading.Thread(target=task, daemon=True).start()

def random_words():
    def task():
        words = [
            "beans",
            "skateboard",
            "go to detention",
            "chalkboard",
            "cowabunga",
            "mischief",
            "Mr Skinner",
            "donuts",
            "HOMER"
        ]
        speak(" ".join(random.sample(words, 3)), 180, False)
    threading.Thread(target=task, daemon=True).start()

# ---------- WINDOW ----------

root = tk.Tk()
root.title("Beans App")
root.geometry("600x420")
root.configure(bg="#0b0b0b")
root.attributes("-alpha", 0.0)

try:
    root.iconbitmap(os.path.join(BASE_DIR, "beans.ico"))
except:
    pass

# ---------- FADE IN ----------

def fade_in(a=0.0):
    a += 0.05
    if a <= 1:
        root.attributes("-alpha", a)
        root.after(20, fade_in, a)

fade_in()

# ---------- CARD ----------

card = tk.Frame(
    root,
    bg="#141414",
    highlightthickness=1,
    highlightbackground="#2a2a2a"
)
card.place(relx=0.5, rely=0.5, anchor="center", width=440, height=320)

title = tk.Label(
    card,
    text="BEANS",
    font=TITLE_FONT,
    bg="#141414",
    fg="#e30000"
)
title.pack(pady=(32, 26))

# ---------- BUTTON FACTORY ----------

def glow_button(text, command):
    btn = tk.Label(
        card,
        text=text,
        bg="#1f1f1f",
        fg="white",
        font=("Segoe UI", 11),
        padx=26,
        pady=12,
        cursor="hand2"
    )

    def enter(e):
        btn.config(bg="#2a2a2a", padx=28, pady=13)

    def leave(e):
        btn.config(bg="#1f1f1f", padx=26, pady=12)

    def click(e):
        btn.config(bg="#3a3a3a")
        command()

    btn.bind("<Enter>", enter)
    btn.bind("<Leave>", leave)
    btn.bind("<Button-1>", click)
    return btn

glow_button("Show Beans", show_beans).pack(pady=6)
glow_button("Random Bart Line", bart_line).pack(pady=6)
glow_button("Random Words", random_words).pack(pady=6)

# ---------- RESPONSIVE TITLE ----------

def resize(event):
    w = root.winfo_width()
    size = max(28, min(44, w // 12))
    title.config(font=(TITLE_FONT[0], size, "bold"))

root.bind("<Configure>", resize)

root.mainloop()
