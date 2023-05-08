#creando diccionario con dict()
diccionario = dict(nombre="elvis", apellido="cabreja")

#las listas no se pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["elvis", "cabreja"]):"jaja"}

#creando diccionarios con fromkeys() valor por defecto: nono
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() valor por defecto: a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")


print(diccionario)