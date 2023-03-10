import socket
from contextlib import closing
import time
import platform
import os, sys
import fichier.design as design
import fichier.lib.pythonping.ping as ping
import fichier.var as var

#############################################################################################
#####	Récupérer les adresses MAC														#####
#############################################################################################
def getmac(ip):
	mac = ""
	try:
		my_os = platform.system()
		if my_os == "Windows":
			# grep with a space at the end of IP address to make sure you get a single line
			fields = os.popen('arp -a ' + ip).read().split()
			if len(fields) == 12 and fields[10] != "00:00:00:00:00:00":
				mac = fields[10]
	except Exception as e:
		design.logs("fct_ip - " + str(e))
		pass
	return mac

#############################################################################################
#####	Tester les ports ouvert															#####
#############################################################################################
def check_port(host,port):
	result = ""
	try:
		if len(port) > 0:
			port01 = port.split(",")
			for port02 in port01:
				result = result + check_socket(host, port02)
	except Exception as e:
		design.logs("fct_ip - " + str(e))
		pass
	return result

#############################################################################################
#####	Récupérer les Noms																#####
#############################################################################################
def check_socket(host, port):
	try:
		with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
			if sock.connect_ex((host, int(port))) == 0:
				return str(port)+"/"
			else:
				return ""
	except Exception as e:
		design.logs("fct_ip - " + str(e))
		return ""

#############################################################################################
#####	Effectuer un ping																#####
#############################################################################################
def ipPing(ip):
	try:
		result = ping.ping(ip, size=10, count=1)
		if result.rtt_avg_ms == int(2000):
			return "HS"
		else:
			return "OK"
	except Exception as inst:
		design.logs(inst)

#############################################################################################
#####	Récupérer l'adresse ip															#####
#############################################################################################
def recup_ip():
	try:
		h_name = socket.gethostname()
		IP_addres = socket.gethostbyname(h_name)
		ip = IP_addres.split(".")
		ipadress = ip[0]+"."+ip[1]+"."+ip[2]+".1"
		return ipadress
	except Exception as e:
		design.logs("fct_ip - " + str(e))


def suiviLat():
	try:
		while True:
			if var.lat == 1:
				column_index = var.tab_ip["columns"].index("Etat")
				l = [(str(var.tab_ip.item(k)["values"][column_index]), k) for k in var.tab_ip.get_children()]
				l.sort(key=lambda t: t[0], reverse=True)
				for index, (val, k) in enumerate(l):
					var.q.put(lambda: var.tab_ip.move(k, '', index))
			else:
				return
			time.sleep(1)
	except Exception as inst:
		design.logs(inst)

