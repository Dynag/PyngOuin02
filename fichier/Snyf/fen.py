#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import fichier.var as var
import time
import threading
import fichier.Snyf.send as send
import fichier.design as design



def snyf():
    check_hik1 = IntVar()
    check_axis1 = IntVar()
    check_Samsung1 = IntVar()
    check_Avigilon1 = IntVar()
    check_Onvif1 = IntVar()
    check_upnp1 = IntVar()
    fenetre1 = Toplevel()

    def snyfScan():
        for i in var.tab_ip.get_children():
            var.tab_ip.delete(i)
        if (var.hik == 1):
            t = threading.Thread(target=send.send("hik")).start()
            var.hik = 0
        if (var.axis == 1):
            t = threading.Thread(target=send.send("axis")).start()
            var.axis = 0
        if (var.onvif == 1):
            t = threading.Thread(target=send.send("onvif")).start()
            var.onvif = 0
        if (var.avigilon == 1):
            t = threading.Thread(target=send.send("avigilon")).start()
            var.avigilon = 0
        if (var.samsung == 1):
            t = threading.Thread(target=send.send("samsung")).start()
            var.samsung = 0
        if (var.upnp == 1):
            t = threading.Thread(target=send.send("upnp")).start()
            var.upnp = 0

        fenetre1.destroy()
        threading.Thread(target=threadCount).start()

    def stop():
        fenetre1.destroy()
    ###### Cocher case Popup
    def isCheckedHik():
        if check_hik1.get() == 1:
            var.hik = 1
        elif check_hik1.get() == 0:
            var.hik = 0

    def isCheckedaxis():
        if check_axis1.get() == 1:
            var.axis = 1
        elif check_axis1.get() == 0:
            var.axis = 0

    def isCheckedSamsung():
        if check_Samsung1.get() == 1:
            var.samsung = 1
        elif check_Samsung1.get() == 0:
            var.samsung = 0



    def isCheckedAvigilon():
        if check_Avigilon1.get() == 1:
            var.avigilon = 1
        elif check_Avigilon1.get() == 0:
            var.avigilon = 0

    def isCheckedOnvif():
        if check_Onvif1.get() == 1:
            var.onvif = 1
        elif check_Onvif1.get() == 0:
            var.onvif = 0
    def isCheckedUpnp():
        if check_upnp1.get() == 1:
            var.upnp = 1
        elif check_upnp1.get() == 0:
            var.upnp = 0

    def threadCount():
        var.progress.grid(row=0, column=2, padx=5, pady=5)
        i = 0
        while i <= var.timeTest:
            progre = (i / var.timeTest) * 100
            print(progre)
            var.progress['value'] = progre
            i += 1
            time.sleep(1)
        var.progress.grid_forget()
        var.ipPing = 0


    def main():

        ###################################################################################################################
        ###### Fenetre principale																					 ######
        ###################################################################################################################
        # Créer une nouvelle fenêtre

        fenetre1.title("Snyf")
        fenetre1.geometry("400x400")
        fenetre1.overrideredirect(1)

        frame_haut = Frame(master=fenetre1, bg=var.bg_frame_haut, height=50, padx=5, pady=5)
        frame_haut.pack(fill=X)
        frame_mid = Frame(master=fenetre1, bg=var.bg_frame_mid, height=300,padx=5, pady=5)
        frame_mid.pack(fill=X)
        frame_bot = Frame(master=fenetre1, bg=var.bg_frame_haut, height=50, padx=5, pady=5)
        frame_bot.pack(fill=X)


        frameCam = Frame(master=frame_mid, bg="#FFFFFF", padx=5, pady=5, width=30, height=280, relief=SUNKEN)
        frameCam.pack(side=LEFT,padx=5, pady=5,fill=Y)
        frameAutre = Frame(master=frame_mid, bg="#FFFFFF", padx=5, pady=5, width=30, height=280, relief=SUNKEN)
        frameAutre.pack(side=LEFT,padx=5, pady=5,fill=Y)

        ########################################
        ## Titre
        Label(master=frame_haut, text="Snyf, récupération automatique des éléments", bg="#FFFFFF").pack(fill=X)
        ####################################################################################################################
        # Caméras
        nomCam = Label(master=frameCam, text="Caméras", bg="#FFFFFF", width=20)
        nomCam.grid(row=0, column=0, padx=5, pady=5, columnspan=1)

        check_popup0 = Checkbutton(frameCam, text='Onvif', variable=check_Onvif1, onvalue=1, offvalue=0, bg="#FFFFFF",
                                  command=isCheckedOnvif)
        check_popup0.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky='w')

        check_popup = Checkbutton(frameCam, text='HIK', variable=check_hik1, onvalue=1, offvalue=0, bg="#FFFFFF",
                                  command=isCheckedHik)
        check_popup.grid(row=2, column=0, padx=5, pady=5, columnspan=1, sticky='w')
        check_popup1 = Checkbutton(frameCam, text='Axis', variable=check_axis1, onvalue=1, offvalue=0, bg="#FFFFFF",
                                  command=isCheckedaxis)
        #check_popup1.grid(row=3, column=0, padx=5, pady=5, columnspan=1, sticky='w')

        check_popup2 = Checkbutton(frameCam, text='Samsung', variable=check_Samsung1, onvalue=1, offvalue=0, bg="#FFFFFF",
                                   command=isCheckedSamsung)
        check_popup2.grid(row=4, column=0, padx=5, pady=5, columnspan=1, sticky='w')

        check_popup3 = Checkbutton(frameCam, text='Avigilon', variable=check_Avigilon1, onvalue=1, offvalue=0, bg="#FFFFFF",
                                   command=isCheckedAvigilon)
        check_popup3.grid(row=5, column=0, padx=5, pady=5, columnspan=1, sticky='w')



        nomAutre = Label(master=frameAutre, text="Autres", bg="#FFFFFF", width=20)
        nomAutre.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        check_popup4 = Checkbutton(frameAutre, text='Upnp', variable=check_upnp1, onvalue=1, offvalue=0,
                                   bg="#FFFFFF",
                                   command=isCheckedUpnp)
        check_popup4.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky='w')

        Button(frame_bot, text='Annuler', padx=10, command=stop).pack(side=LEFT, padx=5, pady=5)
        Button(frame_bot, text='Valider', padx=10, command=snyfScan).pack(side=LEFT, padx=5, pady=5)
        # ______________________________________________________________
        # Créer un menu
        # ______________________________________________________________
        design.center_window(fenetre1)
        fenetre1.mainloop()

    main()