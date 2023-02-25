from tkinter import * 
from tkinter import ttk

version = "1.2.8"
site = 'http://prog.dynag.co'
###########   Couleurs ##########
bg_frame_haut = "#81BEF7"
bg_frame_mid = "#A9D0F5"
bg_frame_droit = "#A9D0F5"
bg_but = "#81BEF7"



couleur_vert = "#baf595"
couleur_jaune = "#fffd6a"
couleur_orange = "#ffb845"
couleur_rouge = "#f97e7e"
couleur_noir = "#6d6d6d"

chunk = []

ipPing = 0
popup = 0
mail = 0
telegram = 0
db = 0
recap = 0
lat = 0
nom_site=""
z=0
checkPort = False
nom_site

envoie_alert = 1

tab_ip = ttk.Treeview
lab_thread = Label
progress = ttk.Progressbar
but_lancer_ping = Button
lab_nom_site = Label
lab_pourcent = Label

threadouvert=0
threadferme=0
delais="5"

liste_nom={}
liste_hs={}
liste_mail={}
liste_telegram={}

param_mail_compte=""
param_mail_pass=""
param_mail_smtp=""
param_mail_port=""
param_mail_serveur=""
param_mail_envoie=""


telegram_id = "548421802"

hik = 0
axis = 0
samsung = 0
avigilon = 0
onvif = 0
upnp = 0

timeTest = 3