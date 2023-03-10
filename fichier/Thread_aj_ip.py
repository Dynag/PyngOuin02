import fichier.fct_ip as fct_ip
import fichier.var as var
import fichier.design as design
import threading
import time
from queue import Queue
import multiprocessing
import queue





################s###########################################################################
#####   Fonction principale d'ajout de ip   										  #####
###########################################################################################

def labThread(value):
    var.progress['value'] = value

def worker(q, thread_no):
    try:
        while True:
            item = q.get()
            if item is None:
                break
            q.task_done()
    except Exception as e:
        design.logs("fct_ping - " + str(e))




def threadIp(ip, tout, i, hote, port):
    var.q.put(lambda: var.progress.grid(row=0, column=2, padx=5, pady=5))
    var.threadouvert = int(var.threadouvert) + 1
    ipexist = False
    for parent in var.tab_ip.get_children():
        result = var.tab_ip.item(parent)["values"]
        ip1 = result[0]

        if ip1 == ip:
            threading.Thread(target=design.alert, args=("L'adresse  " + ip + " existe déja",)).start()
            ipexist = True
            pass
        else:
            ipexist = False
    if ipexist == False:
        time.sleep(0)
        result = fct_ip.ipPing(ip)
        nom = ("")
        mac = ""

        if tout == "Tout":
            if result == "OK":
                try:
                    nom = fct_ip.socket.gethostbyaddr(ip)
                except:
                    nom = (ip, "")
                try:
                    mac = fct_ip.getmac(ip)
                except:
                    pass
                port = fct_ip.check_port(ip, port)

            else:
                nom = ("", "")
                port = ""
                mac = ""
            try:
                var.q.put(
                    lambda: var.tab_ip.insert(parent='', index=i, iid=ip, tag=ip, values=(ip, nom[0], mac, port, "")))
            except:
                pass
        else:
            if result == "OK":
                try:
                    nom = fct_ip.socket.gethostbyaddr(ip)
                except:
                    nom = (ip, "")
                try:
                    mac = fct_ip.getmac(ip)
                except:
                    pass
                port = fct_ip.check_port(ip, port)
                try:
                    var.q.put(lambda: var.tab_ip.insert(parent='', index=i, tag=ip, iid=ip,
                                                        values=(ip, nom[0], mac, port, "")))
                except:
                    pass
        if result == "OK":

            var.q.put(lambda: var.tab_ip.tag_configure(tagname=ip, background=var.couleur_vert))
        else:
            var.q.put(lambda: var.tab_ip.tag_configure(tagname=ip, background=var.couleur_noir))
    var.threadferme = int(var.threadferme) + 1
    thread = var.threadouvert - var.threadferme
    var.q.put(lambda: var.lab_thread.config(text=str(thread) + " /  " + str(hote)))

    progre = ((int(hote) - int(thread)) / int(hote)) * 100
    var.q.put(lambda: labThread(progre))

    if thread <= 0:
        var.q.put(lambda: var.progress.grid_forget())
        var.q.put(lambda: var.lab_thread.config(text=""))
        var.q.put(lambda: design.alert("Le scan est terminé"))


###########################################################################################
#####   Préparation de l'ajout      												  #####
###########################################################################################
def aj_ip(ip, hote, tout, port, mac):
    nbrworker = multiprocessing.cpu_count()
    num_worker_threads = nbrworker
    q = queue.Queue()
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(q, i,), daemon=True)
        t.start()
        threads.append(t)

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
        q.put(threading.Thread(target=threadIp, args=(ip2, tout, i, hote, port)).start())
