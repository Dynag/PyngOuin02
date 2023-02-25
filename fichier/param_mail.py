from tkinter import * 
from tkinter import ttk
import fichier.var as var
import fichier.design as design
import pickle
import os.path
import threading


def lire_param_mail():
	fichierini = "tab"
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
		design.logs(inst)


def main():
	def save_param_mail():
		param_mail_compte = ent0.get()
		param_mail_pass = ent1.get()
		param_mail_port = ent3.get()
		param_mail_serveur = ent4.get()
		param_mail_envoie = ent5.get()
		param_mail_telegram = ent6.get()
		variables = [param_mail_compte, param_mail_pass, param_mail_port, param_mail_serveur, param_mail_envoie, param_mail_telegram]
		try:
			fichierSauvegarde = open("tab","wb")
			pickle.dump(variables, fichierSauvegarde)
			fichierSauvegarde.close()
		except Exception as inst:
			design.logs(inst)
		fenetre1.destroy()
		return
	def lire():
		try:
			variables=lire_param_mail()
			ent0.insert(0, variables[0])
			ent1.insert(0, variables[1])
			ent3.insert(0, variables[2])
			ent4.insert(0, variables[3])
			ent5.insert(0, variables[4])
			ent6.insert(0, variables[5])
		except Exception as inst:
			design.logs(inst)
			return

	fenetre1 = Toplevel()
	fenetre1.title("Paramètres")
	fenetre1.geometry("400x400")
	frame_haut = Frame(master=fenetre1, height=50, bg=var.bg_frame_mid, padx=5, pady=5)
	frame_haut.pack(fill=X)

	lab0 = Label(master=frame_haut, text="Compte", bg=var.bg_frame_mid).grid(row=0, column=0, padx=5, pady=5, sticky = 'w')
	ent0 = Entry(frame_haut, text="")
	ent0.grid(row=0, column=1, padx=5, pady=5, sticky = 'w')

	lab1 = Label(master=frame_haut, text="Pass", bg=var.bg_frame_mid).grid(row=1, column=0, padx=5, pady=5, sticky = 'w')
	ent1 = Entry(frame_haut, text="")
	ent1.grid(row=1, column=1, padx=5, pady=5, sticky = 'w')

	lab3 = Label(master=frame_haut, text="Port", bg=var.bg_frame_mid).grid(row=2, column=0, padx=5, pady=5, sticky = 'w')
	ent3 = Entry(frame_haut, text="")
	ent3.grid(row=2, column=1, padx=5, pady=5, sticky = 'w')

	lab4 = Label(master=frame_haut, text="Serveur", bg=var.bg_frame_mid).grid(row=3, column=0, padx=5, pady=5, sticky = 'w')
	ent4 = Entry(frame_haut, text="")
	ent4.grid(row=3, column=1, padx=5, pady=5, sticky = 'w')

	lab5 = Label(master=frame_haut, text="Mail à envoyer", bg=var.bg_frame_mid).grid(row=4, column=0, padx=5, pady=5, sticky = 'w')
	ent5 = Entry(frame_haut, text="")
	ent5.grid(row=4, column=1, padx=5, pady=5, sticky = 'w')

	lab6 = Label(master=frame_haut, text="ID Telegram", bg=var.bg_frame_mid).grid(row=5, column=0, padx=5, pady=5,
																					 sticky='w')
	ent6 = Entry(frame_haut, text="")
	ent6.grid(row=5, column=1, padx=5, pady=5, sticky='w')

	but_ip = Button(frame_haut, text='Valider', padx=10, command=save_param_mail).grid(row=6, columnspan=2, pady=5)
	lire()
	try:
		fenetre1.mainloop()
	except Exception as inst:
		design.logs("mail-"+str(inst))
	

	




