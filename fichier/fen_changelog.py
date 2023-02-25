#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, Toplevel
import traceback
import fichier.lib.urllib3 as urllib3
import fichier.lib.xmltodict as xmltodict
import fichier.var as var
import fichier.design as design

def getxml():
    try:
        url = var.site+"/PyngOuin/changelog.xml"
        http = urllib3.PoolManager(cert_reqs='CERT_NONE')
        response = http.request('GET', url)
        try:
            data = xmltodict.parse(response.data)
            return data
        except:
            print("Failed to parse xml from response (%s)" % traceback.format_exc())
    except Exception as inst:
        design.logs("fen_a_propos -" + str(inst))

def data():
    try:
        xml = getxml()
        data = ""
        for val in xml["changelog"]["version"]:
            data = data+"Version : "+val["versio"]+"\n"+val["change"]+"\n \n"
        return data
    except Exception as inst:
        design.logs("fen_a_propos -" + str(inst))

def main():
    fenetre1 = Toplevel()
    fenetre1.title("Changelog")
    fenetre1.geometry("400x400")
    frame_haut = Frame(master=fenetre1, bg=var.bg_frame_mid, padx=5, pady=5)
    frame_haut.pack(fill=X)
    text = Text(frame_haut, bg=var.bg_frame_mid)
    text.pack()
    text.insert('1.0', data())
    text['state'] = 'disabled'
    try:
        fenetre1.mainloop()
    except Exception as inst:
        design.logs("fen_a_propos -" + str(inst))