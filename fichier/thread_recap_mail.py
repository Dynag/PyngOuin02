import fichier.var as var
import fichier.design as design
import fichier.param_mail_recap as param_mail_recap
import fichier.fct_thread_mail as fct_thread_mail
import threading
import time
import fichier.fct_thread_mail as fct_thread_mail
from datetime import datetime



def jour_demande():
    jourDemande = tuple()
    data = param_mail_recap.lire_param_mail()
    lun = data[1]
    mar = data[2]
    mer = data[3]
    jeu = data[4]
    ven = data[5]
    sam = data[6]
    dim = data[7]
    if lun == "1":
        jourDemande = jourDemande + ("0",)
    if mar == "1":
        jourDemande = jourDemande + ("1",)
    if mer == "1":
        jourDemande = jourDemande + ("2",)
    if jeu == "1":
        jourDemande = jourDemande + ("3",)
    if ven == "1":
        jourDemande = jourDemande + ("4",)
    if sam == "1":
        jourDemande = jourDemande + ("5",)
    if dim == "1":
        jourDemande = jourDemande + ("6",)
    return jourDemande

def prepaMail():
	sujet = """\
	Compte rendu du site """+var.nom_site+"""
	"""
	message = """\
	Bonjour,<br><br>
	Voici le compte rendu des équipements sous surveillance : <br><br>
	<table width=50%><tr><td bgcolor="""+var.bg_frame_haut+""">Nom</td><td bgcolor="""+var.bg_frame_haut+""">IP</td>
	<td  bgcolor="""+var.bg_frame_haut+""">Latence</tr>
	"""
	for row_id in var.tab_ip.get_children():
		result = var.tab_ip.item(row_id)["values"]
		color = ""
		if result[4] == "":
			color = var.couleur_noir
		else:
			color = var.couleur_vert
		message = message + """\
		<tr><td bgcolor="""+color+""">"""+result[1]+"""</td><td bgcolor="""+color+""">"""+result[0]+"""</td>
		<td bgcolor="""+color+""">"""+result[4]+"""</td></tr>
		"""
	message = message + """\
	</table><br><br>
	Cordialement,<br><br>
	<b>PyngOuin</b>
	"""
	try:
		fct_thread_mail.envoie_mail(message, sujet)
	except Exception as inst:
		design.logs(inst)

def main():
	data = param_mail_recap.lire_param_mail()
	heureDemande = data[0]
	print(heureDemande)
	jourDemande = tuple()
	while True:
		try:
			if var.ipPing == 1:
				if var.recap == 1:
					a = False
					j = jour_demande()
					d = datetime.now()
					jour = str(d.weekday())
					heure = d.strftime('%H:%M')
					for x in j:
						print(x)
						if str(x) == jour:
							if str(heure) == str(heureDemande):
								a = True
					print(a)
					if a == True:
						prepaMail()
					time.sleep(60)
			else:
				print("stop")
				return
		except Exception as inst:
			design.logs("thread_recap - " + str(inst))