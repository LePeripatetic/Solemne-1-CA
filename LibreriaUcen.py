
#from numpy import * 
#____________________________________________________________________________________
# Libreria de Funciones Básicas reutilizables
#Prof Rodolfo Canelón Osal
#_____________________________________________________________________________________

#____________________________________________________________________
def leerVocal(Mensaje,Str_Validos,Mensaje_Error="Caracter Inválido") :
    while True :
        Str=input(Mensaje)
        if Str.upper() in Str_Validos :
            break
        else :
            print(Mensaje_Error)
    return Str

# Leer letras con caracteres válidos
#____________________________________________________________________
def leerValidos(Mensaje,Str_Validos,Mensaje_Error="Caracter Inválido") :
    while True :
        Str=input(Mensaje)
        if Str.upper() in Str_Validos :
            break
        else :
            print(Mensaje_Error)
    return Str
#___________________________________________________________
def invertirCadena(Cadena) :
    Frase_Invertida=""
    Posicion=len(Cadena)-1
    for Indice in range(0,len(Cadena)) :
        Frase_Invertida+=Cadena[Posicion]
        Posicion-=1
    return Frase_Invertida

#___________________________________________________________
def capicua(Cadena) :
    Frase=Cadena
    EsCapicua=False
    if Frase==Invertir_Cadena(Cadena) :
            EsCapicua=True
    return EsCapicua

#___________________________________________________________
def palindrome(Cadena) :
    return Capicua(Cadena)

#___________________________________________________________
def leerNumeroEntero(Mensaje,Mensaje_Error="Caracteres Inválidos") :
    while True :
        Numero_Str=input(Mensaje)
        if Numero_Str.isdigit() :
            break
        else :
            print(Mensaje_Error)
    return int(Numero_Str)

#___________________________________________________________
def leerNumeroDecimal(Mensaje,Mensaje_Error="Caracteres Inválidos") :
    while True :
        Numero_Str=input(Mensaje)
        if Numero_Str in ["0123456789,"] :
            break
        else :
            print(Mensaje_Error)
    return float(Numero_Str)

#___________________________________________________________
def sumar(x,y):
    return x+y

#___________________________________________________________
def restar(x,y):
    return x-y
#___________________________________________________________
def multiplicar(x,y):
    return x*y

#___________________________________________________________
def dividir(x,y):
    if y==0 :
        print("No esta definida division por 0")
        return 0
    else :
        return x/y
#__________________________________________________
def primos(Numero) :
    Es_Primo=True
    if Numero == 1 :
        Es_Primo=False
    else :
        for x in range(2, Numero-1):
            if Numero % x == 0:
                Es_Primo=False
                break
    return Es_Primo
#__________________________________________________
def amigos(a,b):
    Suma_divisor_1=0
    Suma_divisor_2=0
    for x in range(1,a) :
        if a % x == 0 :
            Suma_divisor_1+=x
    for y in range(1,b) :
        if b % y == 0 :
            Suma_divisor_2+=y
    if Suma_divisor_1 ==  b and Suma_divisor_2==a:
        return True
    else :
        return False

#__________________________________________________
def esPar(n):
    if n % 2 == 0 :
       par=True
    else :
        Par=False
    return par
#__________________________________________________
def esImpar(n):
    return not es_par(n)

#__________________________________________________
def paresHasta(n):
    return range(0, n, 2)

#______________________________________________________________________
def buscarElemento(Lista_Donde_Buscar,Elemento,Cantidad_Elementos) :
    P=0
    Conseguido=False
    while P<= Cantidad_Elementos-1 :
        if Lista_Donde_Buscar[P]== Elemento :
            Conseguido=True
            break
        else :
            P+=1
    if not Conseguido :
        P=-1
    return P
#______________________________________________________________________
def eliminarElemento(Lista_Donde_Buscar,Elemento,Cantidad_Elementos) :
    Pos=Buscar_Elemento(Lista_Donde_Buscar,Elemento,Cantidad_Elementos)
    if Pos >=0 :
        Lista_Donde_Buscar.remove(Elemento)
        Eliminado=True
    else :
        Eliminado=False
    return Eliminado

#______________________________________________________________________
def modificarElemento(Lista_Donde_Buscar,Lista_Cambiar,Elemento,Nuevo_Valor,Cantidad_Elementos) :
    Pos=Buscar_Elemento(Lista_Donde_Buscar,Elemento,Cantidad_Elementos)
    if Pos >=0 :
            Lista_Cambiar[Pos]=Nuevo_Valor
            Modificado=True
    else :
            Modificado=False
    return Modificado

#______________________________________________________________________
def swapListas(Lista_1,Lista_2) :
    Lista_Aux=Lista_1
    Lista_1=Lista_2
    Lista_2=Lista_Aux
    return True
#______________________________________________________________________
def  sumarElementos(Lista) :
    Sum=0
    Cantidad=len(Lista)
    for i in range(0,Cantidad-1) :
        Sum+=Lista[i]
    return Sum

#______________________________________________________________________
def multipElementos(Lista) :
    Mul=0
    Cantidad=len(Lista)
    for i in range(0,Cantidad-1):
        Mul*=Lista[i]
    return Mul

#______________________________________________________________________
# Forma 1 Creciente
#       2 Decreciente
def ordenarDatos(Datos,Forma=1) :
    if Forma==1 :
        return Datos.sort()
    else :
        return Datos.sort(reverse=True)

#______________________________________________________________________
def superPosicion(Lista_A,Lista_B) :
    P=0
    Conseguido=False
    L_1=len(Lista_A)
    L_2=len(Lista_B)
    while P<= L_1 and not Conseguido:
        Elemento=Lista_A[P]
        I=0
        while I<= L_2 and not Conseguido:
            if Lista_B [I]== Elemento :
                Conseguido=True
                break
            else :
                I+=1
        if not Conseguido :
            P+=1
    return Conseguido

#______________________________________________________________________
def moda(Datos,Cant_Datos):
    Aux = 0
    Cont = 0
    Valor = -1
    Datos=sorted(Datos)
    for i in range(0,Cant_Datos-1):
        if (Datos[i] == Datos[i+1]):
            Cont +=1
            if Cont >= Aux:
                Aux = Cont
                Valor= Datos[i]
        else:
            Cont=0
    return Valor

#______________________________________________________________________
def media(Datos,Cant_Datos) :
    if Cant_Datos>0 :
        Sum=0
        for i in range(0,Cant_Datos-1) :
                Sum=Sum+Datos[i]
        return Sum/Cant_Datos
    else :
        return -1

#______________________________________________________________________
def mediana(Data,Cant_Datos):
    Data = sorted(Data)
    if Cant_Datos == 0:
        return 0
    if Cant_Datos%2 == 1:
        return Data[Cant_Datos//2]
    else:
        i = Cant_Datos//2
        
    return (Data[i - 1] + Data[i])/2


#______________________________
#ordenación por inserción
#_____________________________

def sortInsercion(v):
    n= len (v)
    for i in range (1,n):
        x= v[ i]
        j= i-1
        while (j>=0 and x< v[ j]):
            v[ j+1]= v[ j]
            j= j-1
        v[ j+1]= x

#______________________________
#
#ordenación por selección
#______________________________

def sortSeleccion( v):
    n= len ( v)
    for i in range (0 ,n -1):
        minimo = v[ i]
        argmin = i
        for j   in   range( i+1 , n):
            if v[ j]< minimo :
                    minimo = v[ j]
                    argmin = j
        v[ argmin ]= v[ i]
        v[ i]= minimo

#______________________________
#
#ordenación por intercambio
#______________________________

def sortIntercambio( v):
    n= len( v)
    for i in range (0 ,n -1):
        for j in range(n-1 ,i,-1):
            if   v[j]< v[j-1]:
                    tmp= v[j]
                    v[j]= v[j-1]
                    v[j-1]= tmp

#______________________________
#
#ordenación por burbuja
#______________________________

def sortBurbuja(lista):
     for dato in range(len(lista)-1,0,-1):
         for i in range(dato):
             if lista[i]>lista[i+1]:
                 temp = lista[i]
                 lista[i] = lista[i+1]
                 lista[i+1] = temp

#-------------------------------
# Ordenamiento QuickSort
#_______________________________

def particion(elementos, inicio, fin):
    pivot = inicio
    for i in range(inicio+1, fin+1):
        if elementos[i] <= elementos[inicio]:
            pivot += 1
            elementos[i], elementos[pivot] = elementos[pivot], elementos[i]
    elementos[pivot], elementos[inicio] = elementos[inicio], elementos[pivot]
    return pivot



def quickSort(elementos, inicio=0, fin=None):
    if fin is None:
        fin = len(elementos) - 1
    def _quicksort(elementos, inicio, fin):
        if inicio >= fin:
            return
        pivot = particion(elementos, inicio, fin)
        _quicksort(elementos, inicio, pivot-1)
        _quicksort(elementos, pivot+1, fin)
    return _quicksort(elementos, inicio, fin)
                 
