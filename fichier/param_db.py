from tkinter import *
import fichier.var as var
import pickle
import os.path
import threading
import fichier.design as design


def lire_param_db():
	try:
		fichierini = "tab3"
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
		design.logs("param_db - " + str(inst))



def main():
	def save_param_db():
		try:
			param_mail_compte = ent0.get()
			param_mail_pass = ent1.get()
			param_mail_port = ent3.get()
			param_mail_serveur = ent4.get()
			variables = [param_mail_compte, param_mail_pass, param_mail_port, param_mail_serveur]
			try:
				fichierSauvegarde = open("tab3","wb")
				pickle.dump(variables, fichierSauvegarde)
				fichierSauvegarde.close()
			except Exception as inst:
				design.logs(str(inst))
			fenetre1.destroy()
			return
		except Exception as inst:
			design.logs("param_db - " + str(inst))
	def lire():
		try:
			variables=lire_param_db()
			ent0.insert(0, variables[0])
			ent1.insert(0, variables[1])
			ent3.insert(0, variables[2])
			ent4.insert(0, variables[3])


		except Exception as inst:

			design.logs("param_db - " + str(inst))
		return

	fenetre1 = Toplevel()
	fenetre1.title("Paramètres DB")
	fenetre1.geometry("400x400")
	frame_haut = Frame(master=fenetre1, height=50, bg=var.bg_frame_mid, padx=5, pady=5)
	frame_haut.pack(fill=X)

	lab0 = Label(master=frame_haut, text="Adresse", bg=var.bg_frame_mid).grid(row=0, column=0, padx=5, pady=5, sticky = 'w')
	ent0 = Entry(frame_haut, text="")
	ent0.grid(row=0, column=1, padx=5, pady=5, sticky = 'w')

	lab1 = Label(master=frame_haut, text="Table", bg=var.bg_frame_mid).grid(row=1, column=0, padx=5, pady=5, sticky = 'w')
	ent1 = Entry(frame_haut, text="")
	ent1.grid(row=1, column=1, padx=5, pady=5, sticky = 'w')

	lab3 = Label(master=frame_haut, text="User", bg=var.bg_frame_mid).grid(row=2, column=0, padx=5, pady=5, sticky = 'w')
	ent3 = Entry(frame_haut, text="")
	ent3.grid(row=2, column=1, padx=5, pady=5, sticky = 'w')

	lab4 = Label(master=frame_haut, text="Pass", bg=var.bg_frame_mid).grid(row=3, column=0, padx=5, pady=5, sticky = 'w')
	ent4 = Entry(frame_haut, text="")
	ent4.grid(row=3, column=1, padx=5, pady=5, sticky = 'w')

	but_ip = Button(frame_haut, text='Valider', padx=10, command=save_param_db).grid(row=6, columnspan=2, pady=5)
	lire()
	try:
		fenetre1.mainloop()
	except Exception as inst:
		design.logs("param_db - " + str(inst))
	

	




