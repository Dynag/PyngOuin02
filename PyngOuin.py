#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fichier.design as design
import fichier.var as var
import fichier.fct_ip as fct_ip
import fichier.fct_ping as fct_ping
import fichier.param_gene as param_gene
import fichier.Thread_aj_ip as Thread_aj_ip
import os
import fichier.fct_suivi as fct_suivi
import fichier.fct_graph as fct_graph
import threading
from tkinter import *
from tkinter import ttk
import math
import webbrowser
from tkinter.messagebox import *
from PIL import ImageTk, Image
import time




def queu():
    while True:
        time.sleep(0.01)
        try:
            try:
                f = var.q.get()
                f()
                if f is None:
                    break
            except Exception as inst:
                pass
        except TclError as inst:
            design.logs("ping-" + str(inst))


def maj():
    import fichier.thread_maj as maj1
    threading.Thread(target=maj1.main(), args=()).start()


def histo():
    selected_item = var.tab_ip.selection()[0]
    val = selected_item = var.tab_ip.selection()[0]
    fct_suivi.suivitxt(val)


def graph():
    val = var.tab_ip.selection()[0]
    fct_graph.main(val)


def suivi():
    selected_item = var.tab_ip.selection()[0]
    suivi = ""
    try:
        suivi = var.tab_ip.item(selected_item)["values"][6]
    except:
        pass
    if suivi == "X":
        var.tab_ip.set(selected_item, column="Suivi", value="")
    else:
        var.tab_ip.set(selected_item, column="Suivi", value="X")


###### Récupérer l'ip du PC
def getentip():
    ip = ent_ip.get()
    showinfo("OK", ip)


###### Fermeture de la fenetre
def Intercepte():
    try:
        val = design.question_box("Attention", "Etes vous sur de vouloir quitter ?")
        if val == True:
            os._exit(0)
    except Exception as e:
        design.logs("exit - " + str(e))


###### Fonction ajouter une IP
def aj_ip():
    Thread_aj_ip.aj_ip(ent_ip.get(), ent_hote.get(), ent_tout.get(), ent_port.get(), 0)


###### Délais entre 2 pings
def spinDelais():
    fct_ping.stopping(frame_haut)
    var.delais = 5
    nbr = spin_delais.get()
    var.delais = nbr
    if int(nbr) < 60:
        delais = str(nbr) + " s"
    elif int(nbr) < 3600:
        nbr = math.ceil(int(nbr) / 60)
        delais = str(nbr) + " min"
    elif int(nbr) < 86400:
        nbr = math.ceil(int(nbr) / 3600)
        delais = str(nbr) + " h"
    else:
        nbr = math.ceil(int(nbr) / 86400)
        delais = str(nbr) + " j"
    lab_delais1.config(text=delais)


def spinTest():
    fct_ping.stopping(frame_haut)
    nbr = spin_test.get()
    var.envoie_alert = nbr
    print(var.envoie_alert)


###### Sélection d'une ligne
def item_selected(event):
    selected_item = var.tab_ip.selection()
    result = var.tab_ip.item(selected_item)["values"]
    try:
        nom = result[1]
        ent_nom.delete(0, END)
        ent_nom.insert(0, nom)
    except Exception as e:
        design.logs("exit - " + str(e))


def open_nav(ip):
    webbrowser.open('http://' + ip)


def right_clic(event):
    # create a popup menu
    selected_item = var.tab_ip.selection()[0]
    suivi1 = ""
    try:
        suivi1 = var.tab_ip.item(selected_item)["values"][5]
    except:
        pass
    rowID = var.tab_ip.identify('item', event.x, event.y)
    if rowID:
        var.tab_ip.selection_set(rowID)
        var.tab_ip.focus_set()
        var.tab_ip.focus(rowID)

        menu_tree = Menu(fenetre, tearoff=0)
        menu_tree.add_command(label="Ouvrir dans le navigateur", command=lambda: open_nav(rowID))
        menu_tree.add_separator()
        menu_tree.add_command(label="Suivi", command=suivi)
        if suivi1 == "X":
            menu_tree.add_command(label="Historique", command=histo)
            menu_tree.add_command(label="Graphique", command=graph)
        menu_tree.add_separator()
        menu_tree.add_command(label="Effacer", command=delete_item)
        menu_tree.post(event.x_root, event.y_root)
    else:
        pass


###### Supprimer un item
def delete_item():
    selected_item = var.tab_ip.selection()[0]
    val = design.question_box("Attention", "Etes vous sur de vouloir effacer l'ip " + selected_item[0])
    if val:
        var.tab_ip.delete(selected_item)
        fct_ping.lancerping(frame_haut)


###### Modifier le nom
def nom_modif():
    selected_item = var.tab_ip.selection()
    var.tab_ip.set(selected_item, column="Nom", value=ent_nom.get())
    pass


def treeview_sort_column(tv, col, reverse):
    column_index = var.tab_ip["columns"].index(col)
    l = [(str(tv.item(k)["values"][column_index]), k) for k in tv.get_children()]
    l.sort(key=lambda t: t[0], reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


###### Cocher case Popup
def isCheckedpopup():
    fct_ping.stopping(frame_haut)
    if check_popup1.get() == 1:
        var.popup = 1
    elif check_popup1.get() == 0:
        var.popup = 0


def isCheckedPort():
    if check_port1.get() == 1:
        var.checkPort = True
    elif check_port1.get() == 0:
        var.checkPort = False


###### Cocher case mail
def isCheckedMail():
    fct_ping.stopping(frame_haut)
    if check_mail1.get() == 1:
        var.mail = 1
    elif check_mail1.get() == 0:
        var.mail = 0


###### Cocher case recap
def isCheckedRecap():
    fct_ping.stopping(frame_haut)
    if check_recap1.get() == 1:
        var.recap = 1
    elif check_recap1.get() == 0:
        var.recap = 0


def isCheckedLat():
    fct_ping.stopping(frame_haut)
    if check_lat1.get() == 1:
        var.lat = 1

    elif check_lat1.get() == 0:
        var.lat = 0


def isCheckedTelegram():
    fct_ping.stopping(frame_haut)
    if check_telegram1.get() == 1:
        var.telegram = 1

    elif check_telegram1.get() == 0:
        var.telegram = 0


def isCheckedDb():
    fct_ping.stopping(frame_haut)
    if check_db1.get() == 1:
        var.db = 1

    elif check_db1.get() == 0:
        var.db = 0


if __name__ == "__main__":
    ###################################################################################################################
    ###### Fenetre principale																					 ######
    ###################################################################################################################
    # Créer une nouvelle fenêtre
    fenetre = Tk()

    fenetre.title("PyngOuin")
    fenetre.geometry("910x600")
    fenetre.minsize(width=910, height=600)
    fenetre.iconbitmap('fichier/logoP.ico')

    ip_pc = fct_ip.recup_ip()

    check_popup1 = IntVar()
    check_mail1 = IntVar()
    check_recap1 = IntVar()
    check_lat1 = IntVar()
    check_port1 = IntVar()
    check_telegram1 = IntVar()
    check_db1 = IntVar()

    var.nom_site = param_gene.nom_site()
    try:
        maj()
    except Exception as e:
        design.logs("MAJ - " + str(e))
        pass
    threading.Thread(target=queu, args=()).start()
    # threading.Thread(target=threado, args=()).start()
    ###################################################################################################################
    ###### Définition des frames																				 ######
    ###################################################################################################################
    frame_haut = Frame(master=fenetre, height=50, bg=var.bg_frame_haut, padx=5, pady=5)
    frame_haut.pack(fill=X)

    frame_main = Frame(master=fenetre, bg=var.bg_frame_mid, padx=5, pady=5)
    frame_main.pack(fill=BOTH, expand=True)

    frame_bas = Frame(master=fenetre, width=25, height=25, bg=var.bg_frame_haut, padx=5, pady=5)
    frame_bas.pack(fill=X)

    ###################################################################################################################
    ###### Frame bas																							 ######
    ###################################################################################################################
    var.lab_thread = Label(master=frame_bas, bg=var.bg_frame_haut, text="")
    var.lab_thread.grid(row=0, column=0, padx=5, pady=5)
    lab_version = Label(master=frame_bas, bg=var.bg_frame_haut, text="PyngOuin version :" + var.version)
    lab_version.grid(row=0, column=1, padx=5, pady=5)
    lab_touvert = Label(master=frame_bas, bg=var.bg_frame_haut, text="")
    lab_touvert.grid(row=0, column=2, padx=5, pady=5)

    ###################################################################################################################
    ###### Frame haut 																							 ######
    ###################################################################################################################
    img = Image.open("fichier/logoP.png")
    img = img.resize((65, 65), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(frame_haut, image=img, height=65, width=65, bg=var.bg_frame_haut)
    panel.grid(row=0, column=0, pady=5, padx=10)
    Button(frame_haut, text='Start', padx=15, bg=var.couleur_rouge,
           command=lambda: fct_ping.lancerping(frame_haut), height=3).grid(row=0, column=1,
                                                                           pady=5)
    var.progress = ttk.Progressbar(frame_haut, orient=HORIZONTAL,
                                   length=250, mode='determinate')
    var.progress.grid(row=0, column=2, padx=5, pady=5)
    var.progress.grid_forget()
    var.lab_pourcent = Label(master=frame_haut, text="", bg=var.bg_frame_haut)
    var.lab_pourcent.grid(row=0, column=3, padx=5, pady=5)
    var.lab_pourcent.grid_forget()
    lab_nom_site = Label(master=frame_haut, text="", bg=var.bg_frame_haut)
    lab_nom_site.grid(row=0, column=4, padx=5, pady=5)
    lab_nom_site.config(text=var.nom_site)

    ###################################################################################################################
    ###### Frame centrale 																						 ######
    ###################################################################################################################
    frame1 = Frame(master=frame_main, bg=var.bg_frame_droit, padx=0, pady=0, width=200, relief=SUNKEN)
    frame1.pack(fill=BOTH, side=LEFT)
    frame2 = Frame(master=frame_main, bg=var.bg_frame_droit, padx=5, pady=5)
    frame2.pack(fill=BOTH, expand=True, side=LEFT)
    frame3 = Frame(master=frame_main, bg=var.bg_frame_droit, padx=0, pady=0, width=200, relief=SUNKEN)
    frame3.pack(fill=BOTH, side=LEFT)
    frame3.pack_propagate(False)
    #############################################
    ##### Gauche
    frameIp = Frame(master=frame1, bg="#FFFFFF", padx=5, pady=0, width=150, height=200, relief=SUNKEN)
    frameIp.pack_propagate(0)
    frameIp.pack(side=TOP, padx=5, pady=5, fill=X)
    frameAutre = Frame(master=frame1, bg="#FFFFFF", padx=5, pady=10, width=150, height=200, relief=SUNKEN)
    frameAutre.pack_propagate(0)
    frameAutre.pack(side=TOP, padx=5, pady=5, fill=X)

    lab_ip = Label(master=frameIp, text="IP", bg="#FFFFFF")
    lab_ip.grid(row=0, column=0, padx=5, pady=5)
    ent_ip = Entry(frameIp, text=ip_pc)
    ent_ip.grid(row=1, column=0, padx=5, pady=5)
    ent_ip.insert(0, ip_pc)
    lab_hote = Label(master=frameIp, text="Nombre d'hotes", bg="#FFFFFF")
    lab_hote.grid(row=2, column=0, padx=5, pady=5)
    ent_hote = Entry(frameIp, text="255")
    ent_hote.grid(row=3, column=0, padx=5, pady=5)
    ent_hote.insert(0, "255")
    ent_tout = ttk.Combobox(master=frameIp, values=[
        "Tout",
        "Alive"], width=18)
    ent_tout.set("Tout")
    ent_tout.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

    lab_port = Label(master=frameIp, text="Ports (xx,xx)", bg="#FFFFFF")
    lab_port.grid(row=5, column=0, padx=5, pady=5)
    ent_port = Entry(frameIp, text="80")
    ent_port.grid(row=6, column=0, padx=5, pady=5)


    Button(frameIp, text='Valider', width=15, padx=10, command=aj_ip, bg=var.bg_but).grid(row=10, columnspan=2,
                                                                                          pady=5)

    Button(frameAutre, text='SnyfCam', width=15, padx=10, command=design.snyf, bg=var.bg_but).grid(row=0,
                                                                                                   padx=12,
                                                                                                   pady=5)

    #############################################
    ##### Frame centrale
    tab_ip_scroll = Scrollbar(frame2)
    tab_ip_scroll.pack(side=RIGHT, fill=Y)
    columns = ('IP', 'Nom', 'mac', 'port', 'Latence', 'Suivi')
    var.tab_ip = ttk.Treeview(frame2, yscrollcommand=tab_ip_scroll.set, selectmode="extended", columns=columns,
                              show='headings')
    for col in columns:
        var.tab_ip.heading(col, text=col, command=lambda _col=col: treeview_sort_column(var.tab_ip, _col, False))
    var.q.put(lambda: var.tab_ip.column("#0", width=0, stretch=FALSE))
    var.q.put(lambda: var.tab_ip.column("IP", anchor=CENTER, stretch=TRUE, width=80))
    var.q.put(lambda: var.tab_ip.column("Nom", anchor=CENTER, stretch=TRUE, width=80))
    var.q.put(lambda: var.tab_ip.column("mac", anchor=CENTER, stretch=TRUE, width=80))
    var.q.put(lambda: var.tab_ip.column("port", anchor=CENTER, stretch=TRUE, width=80))
    var.q.put(lambda: var.tab_ip.column("Latence", anchor=CENTER, width=50, stretch=TRUE))
    var.q.put(lambda: var.tab_ip.column("Suivi", anchor=CENTER, width=30, stretch=FALSE))
    var.q.put(lambda: var.tab_ip.bind('<ButtonRelease-1>', item_selected))
    var.q.put(lambda: var.tab_ip.bind('<3>', right_clic))
    var.q.put(lambda: var.tab_ip.pack(expand=YES, fill=BOTH))

    ### Frame Droit

    frameNom = Frame(master=frame3, bg="#FFFFFF", padx=5, pady=5, width=180, relief=SUNKEN)
    frameNom.pack_propagate(0)
    frameNom.pack(side=TOP, padx=5, pady=5, fill=X)

    ent_nom = Entry(frameNom, text="")
    ent_nom.grid_propagate(0)
    ent_nom.grid(row=0, column=0, padx=5, pady=5)

    ent_nom.insert(0, "")

    Button(frameNom, text='Modifier', padx=10, command=nom_modif, width=10, bg=var.bg_but).grid(row=1, pady=5)

    frametab2 = Frame(master=frame3, bg=var.bg_frame_droit, padx=5, pady=5, width=180, height=20, relief=SUNKEN)
    frametab2.pack_propagate(0)
    frametab2.pack(side=TOP)
    frameDelais = Frame(master=frame3, bg="#FFFFFF", padx=5, pady=5, width=180, relief=SUNKEN)
    frameDelais.pack(side=TOP, padx=5, pady=5, fill=X)

    lab_delais = Label(master=frameDelais, text="Délais entre 2 pings", bg="#FFFFFF", width=20)
    lab_delais.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
    spin_delais = Spinbox(frameDelais, from_=5, to=100000000, width=5, command=spinDelais)
    spin_delais.grid(row=1, column=1, padx=0, pady=5)
    lab_delais1 = Label(master=frameDelais, text="5 s", bg="#FFFFFF")
    lab_delais1.grid(row=1, column=0, padx=0, pady=5)

    lab_test = Label(master=frameDelais, text="Nombre HS", bg="#FFFFFF")
    lab_test.grid(row=2, column=0, padx=0, pady=5)
    spin_test = Spinbox(frameDelais, from_=1, to=10, width=5, command=spinTest)
    spin_test.grid(row=2, column=1, padx=0, pady=5)

    check_popup = Checkbutton(frameDelais, text='Popup', variable=check_popup1, onvalue=1, offvalue=0, bg="#FFFFFF",
                              command=isCheckedpopup)
    check_popup.grid(row=3, columnspan=3, padx=0, pady=5, sticky='w')

    check_mail = Checkbutton(frameDelais, text='Mail', variable=check_mail1, onvalue=1, offvalue=0, bg="#FFFFFF",
                             command=isCheckedMail)
    check_mail.grid(row=4, columnspan=3, padx=0, pady=5, sticky='w')

    check_telegram = Checkbutton(frameDelais, text='Telegram', variable=check_telegram1, onvalue=1, offvalue=0,
                                 bg="#FFFFFF",
                                 command=isCheckedTelegram)
    check_telegram.grid(row=5, columnspan=3, padx=0, pady=5, sticky='w')

    check_recap = Checkbutton(frameDelais, text='Mail Recap', variable=check_recap1, onvalue=1, offvalue=0,
                              bg="#FFFFFF",
                              command=isCheckedRecap)
    check_recap.grid(row=6, columnspan=3, padx=0, pady=5, sticky='w')

    check_db = Checkbutton(frameDelais, text='DB Externe', variable=check_db1, onvalue=1, offvalue=0,
                           bg="#FFFFFF",
                           command=isCheckedDb)
    check_db.grid(row=7, columnspan=3, padx=0, pady=5, sticky='w')

    ########### Effacer #########################################
    frametab1 = Frame(master=frame3, bg=var.bg_frame_droit, padx=5, pady=5, width=180, height=20, relief=SUNKEN)
    frametab1.pack_propagate(0)
    frametab1.pack(side=TOP, expand=False)
    design.load_csv()
    # ______________________________________________________________
    # Créer un menu
    # ______________________________________________________________
    menubar = design.create_menu(fenetre, frame_haut)
    fenetre.config(menu=menubar)

    # ______________________________________________________________
    # Lancer la fenetre
    # ______________________________________________________________
    fenetre.protocol("WM_DELETE_WINDOW", Intercepte)
    try:
        while 1:
            fenetre.mainloop()
    except Exception as e:
        design.logs("Impossible d'ouvrir la fenetre principale - " + e)
