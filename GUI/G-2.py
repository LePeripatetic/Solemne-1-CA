
from tkinter import * 

#_____________________________

       
v=Tk()
v.geometry("350x220")
v.title("Clase 2")
v_2=Tk()
v_2.geometry("350x220")
v_2.title("Toma Cafe")
etiqueta=Label(v,text="Hola Unec")
Et=Label(v,text="Nuestro 1er programa")
Etiqueta_2= Label(v_2, text=" Escribo en la ventana Toma café")
etiqueta.pack()
Et.pack()
Etiqueta_2.pack()
Boton_1=Button (v,text="el boton de las opciones", command=v.quit)
Boton_1.pack()
v.mainloop()
