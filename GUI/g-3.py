
#Botones y etiquetas

from tkinter import * 

def preparaMoca():
	print('Excelente')

def preparaLeche() :
        print("Preparar leche")

darling = Tk()
darling.title("Unec")
etiqueta= Label(darling,text="este es el contenedor").place(x=10,y=12)
boton_1 =   Button(darling,  text="Mi primer boton", fg="Blue",command=preparaMoca).place(x=14,y=12)
boton_2= Button (darling, text="mi segundo boton ", fg="red",command=preparaLeche).place(x=14,y=40)
boton_3= Button (darling, text="Finalizar", fg="Blue",command=darling.quit).place(x=14,y=72)
darling.geometry('383x500')

darling.mainloop()

 
