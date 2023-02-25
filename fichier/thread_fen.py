#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, Toplevel
import fichier.var as var
import fichier.design as design


def main(fichier):
    try:
        fenetre1 = Toplevel()
        fenetre1.title(fichier)
        fenetre1.geometry("400x400")
        frame_haut = Frame(master=fenetre1, bg=var.bg_frame_mid, padx=5, pady=5)
        frame_haut.pack(fill=X)
        fopen = 'fichier/'+fichier+'.txt'
        f = open(fopen, 'r', encoding='utf-8')
        data = f.read()
        f.close
        text = Text(frame_haut, bg=var.bg_frame_mid)
        text.pack()
        text.insert('1.0', data)
        text['state'] = 'disabled'
        fenetre1.mainloop()

    except Exception as inst:
        design.logs("param_db - " + str(inst))