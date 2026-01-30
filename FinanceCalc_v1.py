from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import ttk
import webbrowser
import time
from time import sleep
import random

root = tk.Tk()
root.title("FinanceCalc Pro Max Ultra")
root.geometry("600x500")
root.resizable(False, False)
root.iconbitmap("iconbitmap.ico")

def aktien_append():
    global aktien_button, chosen_investments
    if "aktien" in chosen_investments:
        chosen_investments.remove("aktien")
        aktien_button.config(fg="black", relief="raised")
        print(chosen_investments)
    else:
        chosen_investments.append("aktien")
        aktien_button.config(fg="green", relief="sunken")
        print(chosen_investments)

def immobilien_append():
    global immobilien_button, chosen_investments
    if "immobilien" in chosen_investments:
        chosen_investments.remove("immobilien")
        immobilien_button.config(fg="black", relief="raised")
        print(chosen_investments)
    else:
        chosen_investments.append("immobilien")
        immobilien_button.config(fg="green", relief="sunken")
        print(chosen_investments)

def edelmetalle_append():
    global edelmetalle_button, chosen_investments
    if "edelmetalle" in chosen_investments:
        chosen_investments.remove("edelmetalle")
        edelmetalle_button.config(fg="black", relief="raised")
        print(chosen_investments)
    else:
        chosen_investments.append("edelmetalle")
        edelmetalle_button.config(fg="green", relief="sunken")
        print(chosen_investments)

def anleihen_append():
    global anleihen_button, chosen_investments
    if "anleihen" in chosen_investments:
        chosen_investments.remove("anleihen")
        anleihen_button.config(fg="black", relief="raised")
        print(chosen_investments)
    else:
        chosen_investments.append("anleihen")
        anleihen_button.config(fg="green", relief="sunken")
        print(chosen_investments)




def go_to_chatgpt():
    webbrowser.open("chatgpt.com")

def ergebnisse_ausgeben():
    global ergebnis_liste
    for w in root.winfo_children():
        w.destroy()
    title_label = tk.Label(root, text="""Jahr  |  Startkapital  |  Rendite (%)  |  Endkapital
                                      -------------------------------------------------------""")
    title_label.place(x=300, y=50, anchor="center")

    y = 70

    for ergebnis in ergebnis_liste:

        label = tk.Label(root, text=ergebnis)
        label.place(x=300, y=y, anchor="center")

        y += 20


def simulate_year(K0, r, o):
    z = random.gauss(-1, 2)
    return K0 * (1 + (r + o * z))

def calculate():
    global int_startkapital, int_laufzeit, chosen_investments, investment_params, ergebnis_liste

    ergebnis_liste = []

    count_investments = len(chosen_investments)
    if count_investments == 0:
        value_error_label.config(text="Du musst mindestens ein Investment auswählen", fg="red")
        value_error_label.place(y=370)
        return

    investment_params = {
    "aktien":      {"r": 0.15, "o": 0.15},
    "immobilien": {"r": 0.08, "o": 0.10},
    "anleihen":   {"r": 0.03, "o": 0.05},
    "edelmetalle":{"r": 0.05, "o": 0.12},
    }

    single_budget = int_startkapital / count_investments
    
    capitals = {name: single_budget for name in chosen_investments}

    for year in range(1, int_laufzeit +1):
        total = 0

        year_start = sum(capitals.values())

        for name in capitals:
            params = investment_params[name]
            capitals[name] = simulate_year(capitals[name], params["r"], params["o"])

            year_end = sum(capitals.values())
            year_return = (year_end - year_start) / year_start * 100

        ergebnis_liste.append(f"{year:>4}   | {year_start:>12,.2f} | {year_return:>10.2f}% | {year_end:>12,.2f}")

    endkapital = sum(capitals.values())
    gesamtverdienst = int(endkapital) - int_startkapital
    ergebnis_liste.append(f"\nZusammenfassung: {endkapital:,.2f}€")
    ergebnis_liste.append(f"\nGewinn/Verlust: {gesamtverdienst:,.2f}€")

    ergebnisse_ausgeben()




def anlageklassen():
    global startkapital_info_label, laufzeit_entry, laufzeit_button, euro_sign, aktien_button, immobilien_button, anleihen_button, edelmetalle_button, chosen_investments
    laufzeit_entry.destroy()
    laufzeit_button.destroy()
    euro_sign.destroy()

    chosen_investments = []

    startkapital_info_label.config(text="Wähle eine oder mehrere Anlageklassen aus")
    startkapital_info_label.place(y=250)

    aktien_button = tk.Button(root, text="Aktien", command=aktien_append)
    aktien_button.place(x=150, y=300, anchor="center")

    immobilien_button = tk.Button(root, text="Immobilien", command=immobilien_append)
    immobilien_button.place(x=450, y=300, anchor="center")

    anleihen_button = tk.Button(root, text="Anleihen", command=anleihen_append)
    anleihen_button.place(x=150, y=350, anchor="center")

    edelmetalle_button = tk.Button(root, text="Edelmetalle", command=edelmetalle_append)
    edelmetalle_button.place(x=450, y=350, anchor="center")

    ausrechnen_resize = Image.open("ausr.png").resize((50, 50))
    ausrechnen_button_pic = ImageTk.PhotoImage(ausrechnen_resize)

    ausrechnen_button = tk.Button(root, image=ausrechnen_button_pic, borderwidth=0, highlightthickness=0, cursor="hand2", command=calculate)
    ausrechnen_button.place(x=300, y=300, anchor="center")

    ausrechnen_button.image = ausrechnen_button_pic



def laufzeit_check():
    global value_error_label, startkapital_info_label, laufzeit_entry, int_laufzeit
    laufzeit = laufzeit_entry.get()
    try:
        if int(laufzeit) > 0:
            int_laufzeit = int(laufzeit)
            anlageklassen()
        else:
            value_error_label.config(text="Die Laufzeit darf nicht negativ sein!", fg="red")
    except ValueError:
        value_error_label.config(text="Die Eingabe darf nur auf Zahlen bestehen!", fg="red")

def laufzeit():
    global value_error_label, startkapital_entry,  startkapital_button, startkapital_info_label, premium_button, credits_button, button_disabled_info, laufzeit_entry, laufzeit_button, euro_sign
    startkapital_entry.destroy()
    startkapital_button.destroy()
    value_error_label.config(text="")

    euro_sign.config(text="Jahre")

    premium_button.config(state=tk.DISABLED)
    credits_button.config(state=tk.DISABLED)

    button_disabled_info = tk.Label(root, text="Funktionen sind eingeschränkt bis der Vorgang beendet ist")
    button_disabled_info.place(x=300, y=480, anchor="center")
    
    startkapital_info_label.config(text="Laufzeit")

    laufzeit_entry = ttk.Entry(root, width=25)
    laufzeit_entry.place(x=300, y=300, anchor="center")

    laufzeit_button = tk.Button(root, text="Weiter", command=laufzeit_check)
    laufzeit_button.place(x=300, y=330, anchor="center")


def check_startkapital():
    global startkapital_entry, value_error_label, int_startkapital
    startkapital = startkapital_entry.get()
    try:
        if int(startkapital) > 0:
            int_startkapital = int(startkapital)
            laufzeit()
        else:
            value_error_label.config(text="Das Startkapital darf nicht negativ sein!", fg="red")
    except ValueError:
        value_error_label.config(text="Die Eingabe darf nur auf Zahlen bestehen!", fg="red")

def show_credits():
    global credits_label, back_button
    for widget in root.winfo_children():
        widget.destroy()
    credits_label = tk.Label(root, text="Fast alles: Maxi | Design der Bilder: ChatGPT (der süße 💕)")
    credits_label.place(x=300, y=100, anchor="center")

    back_button = tk.Button(root, text="Zurück zum Menü", command=main_menu)
    back_button.pack()

    mdm_button = tk.Button(root, text="Mitarbeiter des Monats (nicht von Lennart geklaut):", command=go_to_chatgpt)
    mdm_button.place(x=300, y=250, anchor="center")

    mdm_logo = Image.open("mdm.jpg")
    mdm_logo = mdm_logo.resize((200, 200))
    mdm = ImageTk.PhotoImage(mdm_logo)

    mdm_logo_label = tk.Label(root, image=mdm)
    mdm_logo_label.place(x=300, y=400, anchor="center")
    mdm_logo_label.image = mdm
    

def main_menu():
    global startkapital_entry, value_error_label, credits_label, back_button, startkapital_button, startkapital_info_label, premium_button, credits_button, euro_sign
    for widget in root.winfo_children():
        widget.destroy()
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
    euro_sign.place(x=395, y=300, anchor="center")

    startkapital_button = tk.Button(root, text="Weiter", width=15, command=check_startkapital)
    startkapital_button.place(x=300, y=330, anchor="center")

    value_error_label = tk.Label(root, text="", fg="red")
    value_error_label.place(x=300, y=355, anchor="center")

    premium_button = tk.Button(root, text="Premium kaufen", command=show_premium_popup)
    premium_button.place(x=300, y=400, anchor="center")

    credits_button = tk.Button(root, text="Credits", command=show_credits)
    credits_button.place(x=300, y=440, anchor="center")


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