from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import ttk
import webbrowser
import time
from time import sleep

root = tk.Tk()
root.title("FinanceCalc Pro Max Ultra")
root.geometry("600x500")
root.resizable(False, False)
root.iconbitmap("iconbitmap.ico")

def check_startkapital():
    global startkapital_entry, value_error_label
    startkapital = startkapital_entry.get()
    try:
        if int(startkapital) > 0:
            return True
        else:
            value_error_label.config(text="Das Startkapital darf nicht negativ sein!", fg="red")
    except ValueError:
        value_error_label.config(text="Die Eingabe darf nur auf Zahlen bestehen!", fg="red")

def show_credits():
    global credits_label, back_button
    for widget in root.winfo_children():
        widget.destroy()
    credits_label = tk.Label(root, text="Fast alles: Maxi | Design der Bilder: ChatGPT")
    credits_label.place(x=300, y=250, anchor="center")
    back_button = tk.Button(root, text="")
    credits_label.pack()
    

def main_menu():
    global startkapital_entry, value_error_label, credits_label, back_button
    # HIER IF EXISTS DA IST DER FEHLER!!
    credits_label.destroy()
    back_button.destroy()
    pic = Image.open("menu_pic.png")
    pic = pic.resize((600, 250))
    menu_pic = ImageTk.PhotoImage(pic)

    label_start_pic = tk.Label(root, image=menu_pic)
    label_start_pic.place(x=300, y=100, anchor="center")

    label_start_pic.image = menu_pic 

    startkapital_entry = ttk.Entry(root, width=25)
    startkapital_entry.place(x=300, y=300, anchor="center")

    startkapital_info_label = tk.Label(root, text="Startkapital")
    startkapital_info_label.place(x=300, y=280, anchor="center")

    euro_sign = tk.Label(root, text="€")
    euro_sign.place(x=385, y=300, anchor="center")

    startkapital_button = tk.Button(root, text="Next", width=15, command=check_startkapital)
    startkapital_button.place(x=300, y=330, anchor="center")

    value_error_label = tk.Label(root, text="", fg="red")
    value_error_label.place(x=300, y=355, anchor="center")

    premium_button = tk.Button(root, text="Premium kaufen", command=show_premium_popup)
    premium_button.place(x=300, y=400, anchor="center")

    credits_button = tk.Button(root, text="Credits")
    credits_button.place(x=300, y=440, anchor="center", command=show_credits)


def show_premium_popup():
    popup = tk.Toplevel(root)
    popup.title("FinanceCalc Pro Max Ultra +")
    popup.geometry("400x300")
    popup.resizable(False, False)
    popup.iconbitmap("popupicon.ico")

    popup.grab_set()

    img = Image.open("popup.png")
    img = img.resize((170, 170), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(popup, image=photo)
    img_label.image = photo 
    img_label.pack(pady=10)

    text = tk.Label(popup, text="Möchtest du ein FinanceCalc Pro Max Ultra + Abo abschließen?")
    text.pack(pady=10)

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=15)

    def yes():
        webbrowser.open("https://www.youtube.com./watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
        remove_labels()
        popup.destroy()

    def no():
        remove_labels()
        popup.destroy()

    tk.Button(button_frame, text="Ja (239,99€ /m)", width=15, command=yes).pack(side="left", padx=10)
    tk.Button(button_frame, text="Nein", width=15, command=no).pack(side="right", padx=10)

def remove_labels():
    global label_start 
    label_start.destroy()
    main_menu()

def start_loading():
    global label_start
    pic_start = Image.open("startpic.png")
    pic_start = pic_start.resize((600, 500))
    start_pic = ImageTk.PhotoImage(pic_start)

    label_start = tk.Label(root, image=start_pic)
    label_start.pack()

    label_start.image = start_pic
    time.sleep(3)
    show_premium_popup()


start_loading()
root.mainloop()