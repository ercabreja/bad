diccionario = {
    "nombre" : "elvis",
    "apellido" : "Cabreja",
    "telefono"  : 8097195183
}

#nos devuelve un objecto dict_item
clave = diccionario.keys()

#obteniendo un elemento con get() si no encuentra nada el programa continua)
valorDeNombre = diccionario.get("nombre")
print("hola compai")

#eliminando  todo el diccionario
#diccionario.clear()

#eliminando un solo elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable

diccionario_iterable = diccionario.items()


print(diccionario_iterable) 