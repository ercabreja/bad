#creando lista con list()
lista = list([False, 2, 24,25,21,True])

#devuelve la cantidad de elementos de la lista
cantidadElementos = len(lista)

#agregando un elemento a la lista
lista.append(True)

#agregando elemento a la lista con un indice especifico 
lista.insert(2,48)

#agregando varios elementos a la lista 
lista.extend([False,2023])



#eliminando un elemento de la lista (por su indice)
lista.pop(0) #truco, si queremos solo eliminar el ultimo elemento solo colocamos -1 y asi sucesivamente


lista.remove(2)

#odena ls lits de forma ascendente (si usamos el parametro reverse=True lo odena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificamos si un elemento se encuentra en la lista
elementoEncontrado = lista.index(24)

#elimina todos los elementos de una lista
lista.clear()

print(elementoEncontrado)
