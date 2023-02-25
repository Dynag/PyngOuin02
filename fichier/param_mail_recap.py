from tkinter import * 
from tkinter import ttk
import pickle
import os.path
import threading
import fichier.var as var
import fichier.design as design
import tkinter as tk



def lire_param_mail():
	fichierini = "tabr"
	try:
		if os.path.isfile(fichierini):
			fichierSauvegarde = open(fichierini,"rb")
			variables = pickle.load(fichierSauvegarde)
			fichierSauvegarde.close()

			#Affichage de la liste
			return variables
		else:
			#Le fichier n'existe pas
			print("Fichier " + fichierini + " non trouvé")
	except Exception as inst:
		design.logs("mail-"+str(inst))


def main():


	def save_param_mail():
		param_mail_heure = ent0.get()
		param_mail_lun = str(clun.get())
		param_mail_mar = str(cmar.get())
		param_mail_merc = str(cmer.get())
		param_mail_jeu = str(cjeu.get())
		param_mail_ven = str(cven.get())
		param_mail_sam = str(csam.get())
		param_mail_dim = str(cdim.get())
		print(clun.get())
		variables = [param_mail_heure, param_mail_lun, param_mail_mar, param_mail_merc, param_mail_jeu, param_mail_ven, param_mail_sam, param_mail_dim]
		try:
			fichierSauvegarde = open("tabr","wb")
			pickle.dump(variables, fichierSauvegarde)
			fichierSauvegarde.close()
		except Exception as inst:
			design.logs("mail-"+str(inst))
		fenetre2.destroy()
		return

	def lire():
		try:
			variables=lire_param_mail()
			print(variables)
			ent0.insert(0, variables[0])
			if variables[1] == "1":
				clun=1
				c1.select()
			if variables[2] == "1":
				cmar=1
				c2.select()
			if variables[3] == "1":
				cmer=1
				c3.select()
			if variables[4] == "1":
				cjeu=1
				c4.select()
			if variables[5] == "1":
				cven=1
				c5.select()
			if variables[6] == "1":
				csam=1
				c6.select()
			if variables[7] == "1":
				cdim=1
				c7.select()
		except Exception as inst:
			design.logs("mail-"+str(inst))
			return

	fenetre2 = Toplevel()
	fenetre2.title("Paramètres Mail Recap")
	fenetre2.geometry("400x400")
	clun = IntVar()
	cmar = IntVar()
	cmer = IntVar()
	cjeu = IntVar()
	cven = IntVar()
	csam = IntVar()
	cdim = IntVar()
	frame_haut2 = Frame(master=fenetre2, height=50, bg=var.bg_frame_mid, padx=5, pady=5)
	frame_haut2.pack(fill=X)

	lab0 = Label(master=frame_haut2, text="Heure (hh:mm)", bg=var.bg_frame_mid).grid(row=0, columnspan=2, padx=5, pady=5)
	ent0 = Entry(frame_haut2, text="")
	ent0.grid(row=0, column=2, padx=5, pady=5)



	c1 = Checkbutton(frame_haut2, text='Lundi', variable=clun, onvalue=1, offvalue=0, bg=var.bg_frame_mid)
	c1.grid(row=1, column=0, padx=5, pady=5)
	c2 = Checkbutton(frame_haut2, text="Mardi", onvalue = 1, offvalue = 0,variable=cmar, bg=var.bg_frame_mid)
	c2.grid(row=1, column=1, padx=5, pady=5)
	c3 = Checkbutton(frame_haut2, text="Mercredi", onvalue = 1, offvalue = 0,variable=cmer, bg=var.bg_frame_mid)
	c3.grid(row=1, column=2, padx=5, pady=5)
	c4 = Checkbutton(frame_haut2, text="Jeudi", onvalue = 1, offvalue = 0,variable=cjeu, bg=var.bg_frame_mid)
	c4.grid(row=1, column=3, padx=5, pady=5)
	c5 = Checkbutton(frame_haut2, text="Vendredi", onvalue = 1, offvalue = 0,variable=cven, bg=var.bg_frame_mid)
	c5.grid(row=2, column=0, padx=5, pady=5)
	c6 = Checkbutton(frame_haut2, text="Samedi", onvalue = 1, offvalue = 0,variable=csam, bg=var.bg_frame_mid)
	c6.grid(row=2, column=1, padx=5, pady=5)
	c7 = Checkbutton(frame_haut2, text="Dimanche", onvalue = 1, offvalue = 0,variable=cdim, bg=var.bg_frame_mid)
	c7.grid(row=2, column=2, padx=5, pady=5)

	but_ip2 = Button(frame_haut2, text='Valider', padx=10, command=save_param_mail).grid(row=6, columnspan=4, pady=5)
	lire()
	try:
		fenetre2.mainloop()
	except Exception as inst:
		design.logs("mail-"+str(inst))