# Importamos la librería
import solemne as lib
import random as rdm

# Funciones

def crearlista(largoLista):
    lista=[]
    while(largoLista>0):
        lista.append(rdm.randint(0,100))
        largoLista-=1
    return lista    

def detectarOpcion(lista,opcion):
    if (opcion==1):
        lib.sortSeleccion(lista)        
    elif (opcion==2):
        lib.sortInsercion(lista)
    elif (opcion==3):
        lib.sortBurbuja(lista)
    elif (opcion==4):
        lib.quickSort(lista)
    elif (opcion==5):
        lib.mergeSort(lista)
    elif (opcion==6):
        lib.heapsort(lista)

#Menú
val=True

while(val):
    largoLista=int(input("Ingrese el largo de la Lista que desea crear, con rango entre 5 y 100: "))
    if (largoLista<5):
        print("Debe ingresar un número dentro del rango")
    else:
        lista=crearlista(largoLista)
        print("La lista creada es: \n",lista)
        opcion=int(input("1.Selección\n2.Inserción\n3.Burbuja\n4.QuickSort\n5.MergeSort\n6.HeapSort\n7.Salir\nIngrese que método de ordenamiento desea utilizar: "))
        if (opcion==7):
            val=False
        else:
            detectarOpcion(lista,opcion)
            print("La lista ha sido ordenada",lista)

