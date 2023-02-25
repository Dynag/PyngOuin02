import time
import datetime
import os
from tkinter import *
from tkinter import ttk, Toplevel
import fichier.var as var
import fichier.design as design


def ecrire(ip, message):
    try:
        fichier = open("suivi/"+ip+".txt", "a")
        fichier.write(message)
        fichier.close()
    except Exception as inst:
        design.logs("fct_suivi -"+str(inst))

def supprimer(ip):
    try:
        if os.path.exists('suivi/'+ip+'.txt'):
            os.remove('suivi/'+ip+'.txt')
        else:
            print("Impossible de supprimer le fichier car il n'existe pas")

    except Exception as inst:
        design.logs("fct_suivi -"+str(inst))

def creerDossier():
    try:
        if os.path.exists('suivi'):
            return
        else:
            os.mkdir('suivi')
    except Exception as inst:
        design.logs("fct_suivi -"+str(inst))

def suivitxt(fichier):
    fenetre1 = Toplevel()
    fenetre1.title(fichier)
    fenetre1.geometry("400x400")
    frame_haut = Frame(master=fenetre1, bg=var.bg_frame_mid, padx=5, pady=5)
    frame_haut.pack(fill=X)
    fopen = 'suivi/' + fichier + '.txt'
    f = open(fopen, 'r', encoding='utf-8')
    data = f.read()
    f.close
    text = Text(frame_haut, bg=var.bg_frame_mid)
    text.pack()
    text.insert('1.0', data)
    text['state'] = 'disabled'
    try:
        fenetre1.mainloop()
    except Exception as inst:
        design.logs("fct_suivi -"+str(inst))