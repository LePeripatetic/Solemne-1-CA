
from tkinter import *
precios=[1234,2000,3000]
Monto_Pagar=0
def imprima_mes():
     print(radioLeido)
     
def obtenga_precio():
       Monto_Pagar=e1.get()*precios[radioLeido.get()]
       print("Precio:",precios[radioLeido.get()])
       
 
app = Tk() 
app.geometry('300x300')
app.title("MINOR")
radioLeido = IntVar() 

 
rdioOne = Radiobutton(app, text='Moca',
                             variable=radioLeido, value=0) 
rdioTwo = Radiobutton(app, text='Leche',
                             variable=radioLeido, value=1) 
rdioThree = Radiobutton(app, text='Negro',
                             variable=radioLeido, value=2)
Etiqueta_1=Label(app, text="Tazas ").grid(column=0,row=5)
Boton_1 =   Button(app,  text="Calcular Monto", fg="Blue",command=obtenga_precio).place(x=60,y=90)

rdioOne.grid(column=0, row=0)
rdioTwo.grid(column=0, row=1)
rdioThree.grid(column=0, row=2)
e1 = Entry(app)
e1.grid(row=5, column=1)
app.mainloop()
