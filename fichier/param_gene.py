from tkinter import * 
from tkinter import ttk
import fichier.var as var
import fichier.design as design
import pickle
import os.path
import threading

fichierini = "tabG"
"""
check_popup1 = IntVar()
check_mail1 = IntVar()
check_recap1 = IntVar()

popup = False
mail = False
recap = False
"""
def lire_param_gene():
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
		design.logs("param_gene - "+str(inst))

def nom_site():
	try:
		param = lire_param_gene()
		var.nom_site=param[0]
		print(param[0])
	except Exception as inst:
		design.logs("param_gene - "+str(inst))
		return


def main():
	def save_param_gene():
		param_site = ent0.get()
		variables = [param_site]
		try:
			fichierSauvegarde = open(fichierini,"wb")
			pickle.dump(variables, fichierSauvegarde)
			fichierSauvegarde.close()
		except Exception as inst:
			design.logs("param_gene - "+str(inst))
		fenetre1.destroy()
		return
	def lire():
		try:
			variables=lire_param_gene()

			ent0.insert(0, variables[0])

		except Exception as inst:
			design.logs("param_gene - "+str(inst))
			return

	fenetre1 = Toplevel()
	fenetre1.title("Paramètres généraux")
	fenetre1.geometry("400x400")
	frame_haut = Frame(master=fenetre1, height=50, bg=var.bg_frame_mid, padx=5, pady=5)
	frame_haut.pack(fill=X)

	lab0 = Label(master=frame_haut, text="Nom du site", bg=var.bg_frame_mid).grid(row=0, column=0, padx=5, pady=5, sticky = 'w')
	ent0 = Entry(frame_haut, text="")
	ent0.grid(row=0, column=1, padx=5, pady=5, sticky = 'w')

	but_ip = Button(frame_haut, text='Valider', padx=10, command=save_param_gene).grid(row=6, columnspan=2, pady=5)
	lire()
	try:
		fenetre1.mainloop()
	except Exception as inst:
		design.logs("param_gene - "+str(inst))
	

	




