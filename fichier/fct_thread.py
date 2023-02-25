import threading
import time
import fichier.design as design
import fichier.fct_thread_mail as fct_thread_mail
import fichier.thread_telegram as thread_telegram
import fichier.var as var
"""
*********************************************************************************************
*********************************************************************************************
*****	Threads des alertes															    *****
*********************************************************************************************
*********************************************************************************************
"""
############################################################################################
#####	Lancement des différentes alertes										       #####
############################################################################################
def main():
	while True:
		time.sleep(5)
		try:
			if var.ipPing == 1:
				if var.popup == 1:
					try:
						threading.Thread(target=popup, args=()).start()
					except Exception as inst:
						design.logs("fct_thread -" + str(inst))
				if var.mail == 1:
					try:
						threading.Thread(target=mail, args=()).start()
					except Exception as inst:
						design.logs("fct_thread -" + str(inst))
				if var.telegram == 1:
					try:
						threading.Thread(target=telegram, args=()).start()
					except Exception as inst:
						design.logs("fct_thread -" + str(inst))

			else:
				print("stop")
				break
		except Exception as inst:
			design.logs("fct_thread--"+str(inst))

############################################################################################
#####	Alerte Popup															       #####
############################################################################################
def popup():

	try:
		#time.sleep(10)
		erase = ()
		ip_hs = ""
		ip_ok = ""
		for key, value in var.liste_hs.items():
			print(str(key)+" - "+str(value)+ " / "+str(var.envoie_alert))
			if int(value) == int(var.envoie_alert):
				print("popup")
				ip_hs = ip_hs + key + "\n "
				var.liste_hs[key] = 10
			elif value == 20:
				ip_ok = ip_ok + key + "\n "
				erase = erase + (str(key),)
		for cle in erase:
			del var.liste_hs[cle]
		if len(ip_hs) > 0:
			t = threading.Thread(target=design.alert, args=("les hotes suivants sont HS : \n" + ip_hs,))
			t.start()
		if len(ip_ok) > 0:
			t = threading.Thread(target=design.alert, args=("les hotes suivants sont OK : \n" + ip_ok,))
			t.start()
		ip_hs = ""
		ip_ok = ""
	except Exception as inst:
		design.logs("fct_thread--"+str(inst))
############################################################################################
#####	Alertes mails															       #####
############################################################################################
def mail():
	#time.sleep(10)
	try:
		erase = ()
		ip_hs1 = ""
		ip_ok1 = ""
		mess = 0
		message = """\
		Bonjour,<br><br>
		<table border=1><tr><td width='50%' align=center>Nom</td><td width='50%' align=center>IP</td></tr>
		"""
		sujet = "Alerte sur le site " + var.nom_site
		time.sleep(1)
		for key1, value1 in var.liste_mail.items():
			if int(value1) == int(var.envoie_alert):
				nom = design.lire_nom(key1)
				p1 = "<tr><td align=center>" + nom + "</td><td align=center>" + key1 + "</td></tr>"
				ip_hs1 = ip_hs1 + p1
				var.liste_mail[key1] = 10

			elif value1 == 20:
				nom = design.lire_nom(key1)
				p1 = "<tr><td align=center>" + nom + "</td><td align=center>" + key1 + "</td></tr>"
				ip_ok1 = ip_ok1 + p1
				erase = erase + (str(key1),)
		for cle in erase:
			print(cle)
			del var.liste_mail[cle]

		if len(ip_hs1) > 0:
			mess = 1
			message = message + """\
			Les hôtes suivants sont <font color=red>HS</font><br>""" + ip_hs1 + """\
			</table><br><br>
			Cordialement,
			"""

		if len(ip_ok1) > 0:
			mess = 1
			message = message + """\
			Les hôtes suivants sont <font color=green>revenus</font><br>""" + ip_ok1 + """\
			</table><br><br>
			Cordialement,
			"""
		if mess == 1:
			t = threading.Thread(target=fct_thread_mail.envoie_mail, args=(message, sujet))
			t.start()
			mess = 0
		ip_hs = ""
		ip_ok = ""
	except Exception as inst:
		design.logs("fct_thread--"+str(inst))
############################################################################################
#####	Alertes Télégram														       #####
############################################################################################
def telegram():
	try:
		erase = ()
		ip_hs1 = ""
		ip_ok1 = ""
		mess = 0
		message = "Alerte sur le site " + var.nom_site + "\n \n"
		sujet = "Alerte sur le site " + var.nom_site
		time.sleep(1)
		for key1, value1 in var.liste_telegram.items():
			if int(value1) == int(var.envoie_alert):
				nom = design.lire_nom(key1)
				p1 = "" + nom + " : " + key1 + "\n"
				ip_hs1 = ip_hs1 + p1
				var.liste_telegram[key1] = 10

			elif value1 == 20:
				nom = design.lire_nom(key1)
				p1 = "" + nom + " : " + key1 + "\n"
				ip_ok1 = ip_ok1 + p1
				erase = erase + (str(key1),)
		for cle in erase:
			print(cle)
			del var.liste_telegram[cle]

		if len(ip_hs1) > 0:
			mess = 1
			message = message + """\
							Les hôtes suivants sont HS \n""" + ip_hs1 + """\
	
							"""

		if len(ip_ok1) > 0:
			mess = 1
			message = message + """\
							Les hôtes suivants sont revenus \n""" + ip_ok1 + """\
	
							"""
		if mess == 1:
			t = threading.Thread(target=thread_telegram.main, args=(message,))
			t.start()
			mess = 0
		ip_hs = ""
		ip_ok = ""
	except Exception as inst:
		design.logs("fct_thread--"+str(inst))
