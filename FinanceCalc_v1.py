from PIL import Image, ImageTk
import tkinter as tk 
import webbrowser
import time
from time import sleep

root = tk.Tk()
root.title("FinanceCalc Pro Max Ultra")
root.geometry("600x500")
root.resizable(False, False)
root.iconbitmap("iconbitmap.ico")

def show_premium_popup():
    popup = tk.Toplevel(root)
    popup.title("FinanceCalc Pro Max Ultra +")
    popup.geometry("400x300")
    popup.resizable(False, False)

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
        popup.destroy()

    def no():
        popup.destroy()

    tk.Button(button_frame, text="Ja (239,99€ /m)", width=15, command=yes).pack(side="left", padx=10)
    tk.Button(button_frame, text="Nein", width=15, command=no).pack(side="right", padx=10)


def start_loading():
    pic = Image.open("startpic.png")
    pic = pic.resize((600, 500))
    start_pic = ImageTk.PhotoImage(pic)

    label = tk.Label(root, image=start_pic)
    label.pack()

    label.image = start_pic
    time.sleep(3)
    show_premium_popup()


start_loading()
root.mainloop()