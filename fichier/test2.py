from tkinter import *
import var as var

fenetre1 = Toplevel()
fenetre1.title("Snyf")
fenetre1.geometry("400x400")
frame_haut = Frame(master=fenetre1, bg=var.bg_frame_haut, padx=5, pady=5)
frame_haut.pack(fill=X)

fenetre1.mainloop()
