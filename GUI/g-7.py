from tkinter import *
v = Tk()
v.geometry('300x300')
v.title("Unec")

def Op_1():
    print ("op 1")
    
def Op_2():
    print("op 2")

def Op_3():
    print ("op 3")

def Op_4():
    print ("op 4")

# Crear el menu principal
menubarra = Menu(v)
menubarra.add_command(label="Opcion 1", command=Op_1)
menubarra.add_command(label="Opcion 2", command=Op_2)
menubarra.add_command(label="Opcion 3", command=Op_3)
menubarra.add_command(label="Opcion 4", command=Op_4)
menubarra.add_command(label="Salir", command=v.quit)

# Mostrar el menu
v.config(menu=menubarra)

# Mostrar la ventana
v.mainloop()
