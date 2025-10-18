from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()

val = BooleanVar(value=False)
y = IntVar()  # score total
x = StringVar()

def drop():
    return randint(1, 13)

def debut():
    a=drop()
    if a >= 10:
        a = 10  # Valet, Dame, Roi → 10 points
    b=drop()
    if b >= 10:
        b = 10  # Valet, Dame, Roi → 10 points
    return a+b

def hit_action():
    double_button.config(state=DISABLED)
    nouvelle_carte = drop()
    nouvelle_point = nouvelle_carte
    if nouvelle_point >= 10:
        nouvelle_point = 10  # Valet, Dame, Roi → 10 points

    score_actuel = y.get()
    nouveau_score = score_actuel + nouvelle_point

    if nouveau_score > 21:
        x.set(f"Tu as perdu avec {nouveau_score} points")
        hit_button.config(state=DISABLED)
        Stand_button.config(state=DISABLED)
        return

    y.set(nouveau_score)
    x.set(f"Tu as {nouveau_score} points")
    print("Carte tirée :", nouvelle_carte)

def stand():
    Stand_button.config(state=DISABLED)
    score_joueur = y.get()
    a=drop()
    if a >= 10:
        a = 10  # Valet, Dame, Roi → 10 points
    b=drop()
    if b >= 10:
        b = 10  # Valet, Dame, Roi → 10 points
    val_fin=a+b
    for i in range(4):
        if randint(1, 5) == 1:
            val_fin += drop()

    if score_joueur > 21:
        x.set(f"Tu as perdu (score joueur : {score_joueur})")
        hit_button.config(state=DISABLED)
    elif val_fin > 21:
        x.set(f"Tu as gagné ! Le croupier a fait {val_fin} points (score joueur : {score_joueur})")
        hit_button.config(state=DISABLED)
    elif val_fin > score_joueur:
        x.set(f"Tu as perdu. Le croupier a {val_fin} points (score joueur : {score_joueur})")
        hit_button.config(state=DISABLED)
    elif val_fin < score_joueur:
        x.set(f"Tu as gagné ! Le croupier a {val_fin} points (score joueur : {score_joueur})")
        hit_button.config(state=DISABLED)
    else:
        x.set(f"Match nul. Le croupier a aussi {val_fin} points (score joueur : {score_joueur})")
        hit_button.config(state=DISABLED)

def jouer():
    val.set(True)
    score_initial = debut()
    y.set(score_initial)
    x.set(f"Tu as {score_initial} points")
    afficher_jeu()

def afficher_jeu():
    global hit_button
    global double_button
    global Stand_button
    if val.get():
        ttk.Label(frm, textvariable=x).grid(column=0, row=0)
        hit_button = ttk.Button(frm, text="Hit", command=hit_action)
        hit_button.grid(column=1, row=0)
        Stand_button = ttk.Button(frm, text="Stand", command=stand)
        Stand_button.grid(column=1, row=1)
        double_button = ttk.Button(frm, text="Double", command=root.destroy)
        double_button.grid(column=1, row=2)

ttk.Button(frm, text="Jouer", command=jouer).grid(column=0, row=1)

root.mainloop()
