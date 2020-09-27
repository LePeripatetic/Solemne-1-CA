#______________________________
#ordenación por inserción
#_____________________________

def sortInsercion(v):
    n= len (v)
    for i in range (1,n):
        x= v[i]
        j= i-1
        while (j>=0 and x< v[j]):
            v[ j+1]= v[ j]
            j= j-1
        v[j+1]= x

#______________________________
#
#ordenación por selección
#______________________________

def sortSeleccion(v):
    n= len (v)
    for i in range (0 ,n -1):
        minimo = v[ i]
        argmin = i
        for j   in   range(i+1,n):
            if v[j]< minimo :
                    minimo = v[j]
                    argmin = j
        v[argmin]= v[i]
        v[i]= minimo

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

def particion(elementos,inicio,fin):
    pivot = inicio
    for i in range(inicio+1, fin+1):
        if elementos[i] <= elementos[inicio]:
            pivot += 1
            elementos[i], elementos[pivot] =elementos[pivot],elementos[i]
    elementos[pivot], elementos[inicio] =elementos[inicio],elementos[pivot]
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
                 
#-------------------------------
# Ordenamiento MergeSort
#_______________________________

def mergeSort(lista): 
    if len(lista) >1: 
        mid = len(lista)//2 
        L = lista[:mid] 
        R = lista[mid:] 
  
        mergeSort(L)
        mergeSort(R) 
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                lista[k] = L[i] 
                i+= 1
            else: 
                lista[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            lista[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            lista[k] = R[j] 
            j+= 1
            k+= 1
            
#______________________________
#
#Ordenamiento HeapSort
#______________________________

def heapsort(lista,tam):
    for k in range(tam-1,-1,-1):
        for i in range(0,k):
            item=lista[i]
            j=(i+1)/2
            while j>=0 and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=j/2
            lista[i]=item
        temp=lista[0]
        lista[0]=lista[k]
        lista[k]=temp
