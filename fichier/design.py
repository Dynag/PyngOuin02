import csv
import datetime
import threading
from tkinter import *
from tkinter.messagebox import *
import time
from tkinter import messagebox
import fichier.Snyf.fen as snyfFen
import fichier.param_mail as param_mail
import fichier.param_gene as param_gene
import fichier.param_db as param_db
import fichier.param_mail_recap as param_mail_recap
import fichier.var as var
import fichier.thread_xls as thread_xls
import fichier.thread_fen as thread_fen
import fichier.fct_ping as fct_ping
import logging.config
import logging


def logs(log):
	logging.config.fileConfig('fichier/logger.ini', disable_existing_loggers=False)
	logger = logging.getLogger(__name__)
	logger.error(log, exc_info=True)

def question_box(title, message):
	var = messagebox.askquestion(title, message)
	resp = False
	if var == "yes":
		resp = True
	else:
		resp = False
	return resp

def rac_s(ev=None):
	try:
		save_csv()
	except Exception as e:
		logs("design - " + str(e))

def rac_x(ev=None):
	try:
		xlsExport()
	except Exception as e:
		logs("design - " + str(e))
def rac_o(ev=None):
	try:
		xlsImport()
	except Exception as e:
		logs("design - " + str(e))

def rac_f(ev=None):
	try:
		snyf()
	except Exception as e:
		logs("design - " + str(e))



def fenAPropos():
	try:
		thread_fen.main("apropos")
	except Exception as e:
		logs("design - " + str(e))

def fenAChangelog():
	try:
		import fichier.fen_a_propos as apropos
		apropos.main()
	except Exception as e:
		logs("design - " + str(e))

def xlsImport():
	#try:
		thread_xls.openExcel()
	#except Exception as e:
	#	logs("design - " + str(e))

def xlsExport():
	#try:
		thread_xls.saveExcel()
	#except Exception as e:
	#	logs("design - " + str(e))
def snyf():
	try:
		snyfFen.snyf()
	except Exception as e:
		logs("design - " + str(e))
def test():
	try:
		import fichier.test as test
		t = threading.Thread(target=test.main).start()
	except Exception as e:
		logs("design - " + str(e))


def alert(message):
    showinfo("alerte", message)

def lire_nom(ip):
	try:
		nom1 = var.tab_ip.item(ip,'values')
		nom = nom1[1]
		return nom
	except Exception as e:
		logs("design - " + str(e))

def save_csv():
	try:
		with open("ip", "w", newline='') as myfile:
			csvwriter = csv.writer(myfile, delimiter=',')

			for row_id in var.tab_ip.get_children():
				row = var.tab_ip.item(row_id)['values']
				csvwriter.writerow(row)

		threading.Thread(target=alert, args=("Votre plage IP à été enregistré",)).start()
	except Exception as e:
		logs("design - " + str(e))
		return

def load_csv():
	try:
	    with open("ip") as myfile:
	        csvread = csv.reader(myfile, delimiter=',')
	        i = 0
	        for row in csvread:
	            var.tab_ip.insert(parent='', index=i, tag=row[0], iid=row[0], values=row)
	            var.tab_ip.tag_configure(tagname=row[0])
	            i = i+1
	except Exception as e:
		logs("design - " + str(e))
		return

def paramGene():
	threading.Thread(target=param_gene.main).start()
def paramDb():
	threading.Thread(target=param_db.main).start()
def paramMail():
	threading.Thread(target=param_mail.main).start()
def paramMailRecap():
	threading.Thread(target=param_mail_recap.main).start()
#  Menu
def create_menu(fenetre, frame_haut):
	menubar = Menu(fenetre)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Sauvegarder  ctrl+s", command=save_csv)
	menu1.add_command(label="Charger", command=load_csv)
	menu1.add_command(label="Tout effacer", command=tab_erase)
	menu1.add_separator()
	#menu1.add_command(label="Quitter ctrl+q", command=fenetre.quit)
	#menu1.add_command(label="Test", command=test)
	menubar.add_cascade(label="Fichier", menu=menu1)

	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="Général", command=paramGene)
	menu2.add_command(label="Envoies", command=paramMail)
	menu2.add_command(label="Mail Recap", command=paramMailRecap)
	menu2.add_command(label="DB", command=paramDb)
	menubar.add_cascade(label="Paramètres", menu=menu2)

	menu4 = Menu(menubar, tearoff=0)
	menu4.add_command(label="Export xls ctrl+x", command=xlsExport)
	menu4.add_command(label="Import xls ctrl+o", command=xlsImport)
	menu4.add_separator()
	menu4.add_command(label="Snyf ctrl + f", command=snyf)
	menubar.add_cascade(label="Fonctions", menu=menu4)

	menu3 = Menu(menubar, tearoff=0)
	menu3.add_command(label="A propos", command=fenAPropos)
	menu3.add_command(label="Changelog", command=fenAChangelog)
	menu3.add_separator()
	menubar.add_cascade(label="?", menu=menu3)
	menubar.bind_all('<Control-s>', rac_s)
	menubar.bind_all('<Control-a>', lambda ev: fct_ping.lancerping(frame_haut))
	menubar.bind_all('<Control-x>', rac_x)
	menubar.bind_all('<Control-o>', rac_o)
	menubar.bind_all('<Control-f>', rac_f)
	return menubar

def tab_erase():
	try:
		val = question_box("Attention", "Etes vous sur de vouloir effacer la liste ?")
		if val == True:
			for i in var.tab_ip.get_children():
				var.tab_ip.delete(i)
	except Exception as e:
		logs("design - " + str(e))


def center_window(w):
	try:
		eval_ = w.nametowidget('.').eval
		eval_('tk::PlaceWindow %s center' % w)
	except Exception as e:
		logs("design - " + str(e))