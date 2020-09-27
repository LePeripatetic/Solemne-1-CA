from tkinter import *

def muestra_datos():
    print("Nombre: ", e1.get(),"Apellido:", e2.get() )

v = Tk()
Etiqueta_1=Label(v, text="Nombre ").grid(row=0)
Etiqueta_2=Label(v, text="Apellido ").grid(row=1)
Etiqueta_2=Label(v, text="Dirección").grid(row=2)
Boton_1 =   Button(v,  text="Imprima los datos", fg="Blue",command=muestra_datos).place(x=60,y=60)
v.geometry('380x300')
v.title("MINOR")
e1 = Entry(v)
e2 = Entry(v)
e3 = Entry(v)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
v.mainloop()

