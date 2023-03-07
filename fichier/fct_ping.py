import time
from tkinter import *
from queue import Queue
import datetime
import os
import queue
import threading
import multiprocessing
import fichier.fct_thread as fct_thread_popup
import fichier.lib.pythonping.ping as ping
import fichier.param_gene as param_gene
import fichier.thread_recap_mail as thread_recap_mail
import fichier.var as var
import fichier.fct_ip as fct_ip
import fichier.fct_suivi as fct_suivi
import fichier.MySql as mysql
import fichier.design as design

"""
*********************************************************************************************
*********************************************************************************************
*****	Fonctions de pings															   ******
*********************************************************************************************
*********************************************************************************************
"""
q = Queue()
qq = Queue()


###########################################################################################
#####				Incrémentation de la perte sur la liste							  #####
###########################################################################################
def list_increment(liste, ip):
    try:
        if ip in liste:
            if int(liste[ip]) < int(var.envoie_alert):
                liste[ip] += 1
            else:
                liste[ip] = liste[ip]
        else:

            liste[ip] = 1
    except Exception as inst:
        design.logs("ping-" + str(inst))




###########################################################################################
#####				Marqué l'hôte comme revenu sur les listes						  #####
###########################################################################################
def list_ok(liste, ip):
    try:
        if ip in liste:
            if liste[ip] == 10:
                liste[ip] = 20
            else:
                del var.liste[ip]
    except Exception as inst:
        design.logs("ping-" + str(inst))


def db_ext(ip, nom, etat, latence):
    if var.db == 1:
        try:
            var.q.put(lambda: mysql.add_enre(ip, nom, etat, latence, var.nom_site))
        except Exception as inst:
            design.logs("ping-" + str(inst))


###########################################################################################
#####				Fonction de ping												  #####
###########################################################################################
def test_ping(ip):
    try:
        time.sleep(0.01)
        result = ping.ping(ip, size=10, count=1)
        etat = ""
        latence = ""
        nom = ""

        selected_item = ip
        valeur = var.q.put(lambda: var.tab_ip.item(selected_item)["values"])
        try:
            suivi = valeur[6]
            nom = valeur[1]
        except:
            if os.path.exists('suivi/' + ip + '.txt'):
                fct_suivi.supprimer(ip)
            suivi = ""

        date = str(datetime.datetime.now())
        message = date + " || "
        if var.ipPing == 0:
            return
        if result.rtt_avg_ms == int(2000):
            message = message + "HS || 200"

            try:
                var.q.put(lambda: var.tab_ip.tag_configure(tagname=ip, background=var.couleur_noir))
                var.q.put(lambda: var.tab_ip.delete(ip, column="Latence"))
                var.q.put(lambda: var.tab_ip.set(ip, column="Latence", value=""))
            except TclError as inst:
                design.logs("ping-" + str(inst))
                pass
            try:
                var.q.put(list_increment(var.liste_hs, ip))
                var.q.put(list_increment(var.liste_mail, ip))
                var.q.put(list_increment(var.liste_telegram, ip))
            except Exception as inst:
                design.logs("ping-" + str(inst))
            etat = "HS"
            latence = ""

        else:
            message = message + " OK || " + str(result.rtt_avg_ms) + " ms"
            if result.rtt_avg_ms < 2:
                color = var.couleur_vert
            elif result.rtt_avg_ms < 10:
                color = var.couleur_jaune
            elif result.rtt_avg_ms < 50:
                color = var.couleur_orange
            else:
                color = var.couleur_rouge

            if result.rtt_avg_ms < 1:
                ttot = "<1 ms"
            else:
                ttot = str(result.rtt_avg_ms) + " ms"
            try:
                list_ok(var.liste_hs, ip)
            except Exception as inst:
                design.logs("ping-" + str(inst))
            try:
                list_ok(var.liste_mail, ip)
            except Exception as inst:
                design.logs("ping-" + str(inst))
            try:
                list_ok(var.liste_telegram, ip)
            except Exception as inst:
                design.logs("ping-" + str(inst))
            try:
                var.q.put(lambda: var.tab_ip.tag_configure(tagname=ip, background=color))
                var.q.put(lambda: var.tab_ip.delete(ip, column="Latence"))
                var.q.put(lambda: var.tab_ip.set(ip, column="Latence", value=ttot))
            except TclError as inst:
                design.logs("ping-" + str(inst))
                pass
            etat = "OK"
            latence = ttot
        message = message + "\n"
        if var.db == 1:
            var.q.put(lambda: db_ext(ip, nom, etat, latence))
        if suivi == "X":
            var.q.put(lambda: fct_suivi.ecrire(ip, message))
        return message
    except Exception as e:
        design.logs("fct_ping - " + str(e))


###########################################################################################
#####				Lancement des pings sur les workers                  			  #####
###########################################################################################
def worker(q, thread_no):
    try:
        while True:
            item = q.get()
            if item is None:
                break
            mess = test_ping(str(item))
            q.task_done()
    except Exception as e:
        design.logs("fct_ping - " + str(e))


###########################################################################################
#####				Création des workers et mise en liste des tâches     			  #####
###########################################################################################
def threadPing():
    param_gene.nom_site()
    if var.db == 1:
        try:
            mysql.create_table(var.nom_site)
        except:
            pass
    while True:
        try:
            if var.db == 1:
                try:
                    mysql.vider_table(var.nom_site)
                except:
                    pass
            startfct = time.time() * 1000.0
            if var.ipPing == 1:
                nbrworker = multiprocessing.cpu_count()
                print(str(nbrworker))
                num_worker_threads = nbrworker
                q = queue.Queue()
                threads = []
                for i in range(num_worker_threads):
                    t = threading.Thread(target=worker, args=(q, i,), daemon=True)
                    t.start()
                    threads.append(t)
                i = 0
                for parent in var.tab_ip.get_children():
                    result = var.tab_ip.item(parent)["values"]
                    ip1 = result[0]
                    q.put(ip1)
                # block until all tasks are done
                q.join()
                # stop workers
                for i in range(num_worker_threads):
                    q.put(None)
                for t in threads:
                    t.join()
                stopfct = time.time() * 1000.0
                tpsfct = (stopfct - startfct) / 1000
                if tpsfct < int(var.delais):
                    time.sleep(int(var.delais) - tpsfct)
            else:
                break
        except Exception as e:
            design.logs("fct_ping - " + str(e))


###########################################################################################
#####				Gestion du bouton ping, lancer ou arrêter les pings				  #####
###########################################################################################
def lancerping(fenetre1):
    if var.ipPing == 0:
        fct_suivi.creerDossier()
        var.ipPing = 1
        var.but_lancer_ping = Button(fenetre1, text='Stop', padx=15, bg=var.couleur_vert, command=lambda: lancerping(fenetre1), height=3).grid(row=0, column=1, pady=5)
        threading.Thread(target=threadPing).start()
        if var.popup == 1 or var.mail == 1 or var.telegram == 1:
            var.q.put(lambda: threading.Thread(target=fct_thread_popup.main).start())
        if var.recap == 1:
            var.q.put(lambda: threading.Thread(target=thread_recap_mail.main).start())
        if var.lat == 1:
            var.q.put(lambda: threading.Thread(target=fct_ip.suiviLat, args=()).start())
    else:
        var.but_lancer_ping = Button(fenetre1, text='Start', padx=15, bg=var.couleur_rouge,
                                     command=lambda: lancerping(fenetre1), height=3).grid(row=0, column=1, pady=5)
        var.ipPing = 0
    return


###########################################################################################
#####				Arrêt des pings si coche d'une case								  #####
###########################################################################################
def stopping(fenetre1):
    if var.ipPing == 0:
        return
    else:
        var.but_lancer_ping = Button(fenetre1, text='Start', padx=10, bg=var.couleur_rouge, command=lambda: lancerping(fenetre1), height=3).grid(row=0, column=1, pady=5)
        var.ipPing = 0
    return
