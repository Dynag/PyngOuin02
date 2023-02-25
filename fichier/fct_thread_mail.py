import fichier.lib.multipart as MIMEMultipart1
import fichier.lib.smtplib as smtplib
import fichier.lib.ssl as ssl
import fichier.lib.text as MIMEText1
import fichier.param_mail as param_mail
from email.utils import formatdate
import fichier.design as design


def envoie_mail(messageRecep, sujet):
	print("001")
	variables = param_mail.lire_param_mail()

	destinateur = variables[0]
	password = variables[1]
	port = variables[2]
	smtp_server = variables[3]
	destinataire = variables[4]


	message = MIMEMultipart1.MIMEMultipart('alternative')
	message['Subject'] = sujet
	message['From'] = destinateur
	message['To'] = destinataire
	message['Date'] = formatdate(localtime=True)

	email_texte = messageRecep
	email_html = messageRecep

	mimetext_texte = MIMEText1.MIMEText(email_texte, "texte")
	mimetext_html = MIMEText1.MIMEText(email_html, "html")
	message.attach(mimetext_texte)
	message.attach(mimetext_html)

	context = ssl.create_default_context()
	print("Test envoie mail")
	try:
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(destinateur, password)
			server.sendmail(destinateur, destinataire.split(","), message.as_string())
			print("Test envoie mail OK")
			

	except Exception as inst:
		log = design.logs("fct_tread_mail"+inst)
		print(inst)
		print(log)
		return

