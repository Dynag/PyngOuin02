from tkinter import *
import fichier.design as design

def valeur(ip):
    try:
        val=[]
        fopen = 'suivi/' + ip + '.txt'
        f = open(fopen, 'r', encoding='utf-8')
        data = f.read()
        f.close
        data2 = data.split('\n')
        for data3 in data2:
            data4 = data3.split(" || ")
            try:
                data5 = data4[2]
            except:
                pass
            data6 = data5.split(" ms")
            data7=data6[0].split(".")
            data8=data7[0]
            val.append(int(data8))
        val2 = list(reversed(val))
        i = 0
        val4=[]
        for val3 in val2:
            if i<100:
                val4.append(val3)
                i+=1
            else:
                pass
        val5 = list(reversed(val4))
        return val5
    except Exception as e:
        design.logs("fct_graph - " + str(e))


def fen(val):
    try:
        fenetre1 = Toplevel()
        fenetre1.title("Suivi")
        fenetre1.geometry("400x300")
        scroll = len(val) * 20
        frame1 = Frame(master=fenetre1, bg="white", padx=5, pady=5, width=30, height=300, relief=SUNKEN)
        frame1.pack(fill=BOTH,side=LEFT, expand=False)
        frame2 = Frame(master=fenetre1, bg="white", padx=5, pady=5)
        frame2.pack(fill=BOTH, expand=True, side=LEFT)
        canvas1 = Canvas(frame1, width=30, height=250)
        canvas1.pack(side=LEFT, expand=True, fill=BOTH)
        lab4 = Label(master=canvas1, bg="white", text="100")
        lab4.place(x=0, y=50, anchor='nw')

        lab3 = Label(master=canvas1, bg="white", text="50")
        lab3.place(x=0, y=130, anchor='nw')

        lab2 = Label(master=canvas1, bg="white", text="10")
        lab2.place(x=0, y=190, anchor='nw')

        lab1 = Label(master=canvas1, bg="white", text="5")
        lab1.place(x=0, y=220, anchor='nw')

        lab0 = Label(master=canvas1, bg="white", text="0")
        lab0.place(x=0, y=240, anchor='nw')




        canvas=Canvas(frame2, width=scroll, height=300,scrollregion=(0,0,scroll,250))
        horibar=Scrollbar(
            frame2,
            orient=HORIZONTAL
            )
        horibar.pack(side=BOTTOM,fill=X)
        horibar.config(command=canvas.xview)
        canvas.config(
            xscrollcommand=horibar.set
            )
        canvas.pack(side=LEFT,expand=True,fill=BOTH)
        line(canvas, scroll)
        graph(canvas,val)

        frame3 = Frame(master=fenetre1, bg="white", padx=5, pady=5)
        frame3.pack(fill=BOTH, expand=True, side=LEFT)
        canvas3 = Canvas(frame3, width=30, height=250)
        canvas3.pack(side=LEFT, expand=True, fill=BOTH)


        return fenetre1
    except Exception as e:
        design.logs("fct_graph - " + str(e))

def line(canvas, scroll):
    try:
        canvas.create_line(0, 250, 0, 0, fill="blue", width=1)
        canvas.create_line(0, 250, scroll, 250, fill="blue", width=1)
        canvas.create_line(0, 230, scroll, 230, fill="blue", width=1)
        canvas.create_line(0, 210, scroll, 210, fill="blue", width=1)
        canvas.create_line(0, 150, scroll, 150, fill="blue", width=1)
        canvas.create_line(0, 50, scroll, 50, fill="blue", width=1)
    except Exception as e:
        design.logs("fct_graph - " + str(e))

def graph(canvas,val):
    try:
        xdep=0
        ydep=250
        xfin=0
        yfin=0
        i=0
        for pt in val:
            if pt >120:
                pt=120
            yfin=250-(int(pt)*2)
            xfin=xfin+20
            canvas.create_line(xdep, ydep, xfin, yfin, fill="green", width=2)
            xdep=xfin
            ydep=yfin
            i+=1
    except Exception as e:
        design.logs("fct_graph - " + str(e))

def main(ip):
    try:
        val=valeur(ip)
        fenetre1=fen(val)
        fenetre1.mainloop()
    except Exception as e:
        design.logs("fct_graph - " + str(e))
