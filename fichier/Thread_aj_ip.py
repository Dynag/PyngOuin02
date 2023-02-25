import fichier.fct_ip as fct_ip
import fichier.var as var
import fichier.design as design
import threading
import time

###########################################################################################
#####   Fonction principale d'ajout de ip   										  #####
###########################################################################################
def threadIp(ip, tout, i, hote, port):
    var.progress.grid(row=0, column=2, padx=5, pady=5)
    var.threadouvert = int(var.threadouvert ) +1
    ipexist = False
    for parent in var.tab_ip.get_children():
        result = var.tab_ip.item(parent)["values"]
        ip1 = result[0]

        if ip1 == ip:
            threading.Thread(target=design.alert, args=("L'adresse  " +ip +" existe déja",)).start()
            ipexist = True
            pass
        else:
            ipexist = False
    if ipexist == False:
        time.sleep(0)
        result = fct_ip.ipPing(ip)
        nom =("")
        mac =""

        if tout == "Tout":
            if result == "OK":
                try:
                    nom = fct_ip.socket.gethostbyaddr(ip)
                except:
                    nom =(ip ,"")
                try:
                    mac = fct_ip.getmac(ip)
                except:
                    pass
                port = fct_ip.check_port(ip, port)

            else:
                nom =("" ,"")
                port =""
                mac = ""
            try:
                var.tab_ip.insert(parent='', index=i, iid=ip, tag=ip, values=(ip, nom[0] ,mac ,port ,""))
            except:
                pass
        else:
            if result == "OK":
                try:
                    nom = fct_ip.socket.gethostbyaddr(ip)
                except:
                    nom =(ip ,"")
                try:
                    mac = fct_ip.getmac(ip)
                except:
                    pass
                port = fct_ip.check_port(ip, port)
                try:
                    var.tab_ip.insert(parent='', index=i, tag=ip, iid=ip, values=(ip, nom[0] ,mac ,port ,""))
                except:
                    pass
        if result == "OK":

            var.tab_ip.tag_configure(tagname=ip, background=var.couleur_vert)
        else:
            var.tab_ip.tag_configure(tagname=ip, background=var.couleur_rouge)
    var.threadferme = int(var.threadferme ) +1
    thread = var.threadouvert - var.threadferme
    var.lab_thread.config(text=str(thread ) +" /  " +str(hote))

    progre = ((int(hote ) -int(thread) ) /int(hote) ) *100
    var.progress['value'] = progre

    if thread == 0:
        var.progress.grid_forget()
        design.alert("Le scan est terminé")

###########################################################################################
#####   Préparation de l'ajout      												  #####
###########################################################################################
def aj_ip(ip, hote, tout, port, mac):
    ip1 = ip.split(".")
    u = 0
    i = 0
    if int(hote) > 500:
        return
    while i < int(hote):
        ip2 = ip1[0] + "." + ip1[1] + "."
        ip3 = int(ip1[3]) + i

        i = i + 1
        if int(ip3) <= 255:
            ip2 = ip2 + ip1[2] + "." + str(ip3)
        else:
            ip4 = int(ip1[2]) + 1
            ip2 = ip2 + str(ip4) + "." + str(u)
            u = u + 1
        t = i
        t = threading.Thread(target=threadIp, args=(ip2, tout, i, hote, port))
        t.start()