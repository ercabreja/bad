cadena1 = "Hola,soy,elvis,Hola,ss"
cadena2 = "bienvenido papu"
cadena3 = "15651"
cadena4 = "dasdasdas"

#convierte a MAYUSCULA
mayusculas = cadena1.upper()

#convierte a minuscula
minuscula = cadena1.lower()

#convierte a la primera en Mayuscula
primerMayuscula = cadena2.capitalize()

#Buscar una cadena en otra cadena, si no hay coincidencia devuelve -1
busquedaFind = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hoy coincidencia devulve una excepcion
busquedaIndex = cadena1.index("H")

#si es numerico, devolvemos true, si es falso devuelve false
esNumerico = cadena3.isnumeric()

#si es alfanumerico devuelve true, sino devuelve false
esAlphanumeric = cadena4.isalpha()

#contamos coincidencias de una cadena dentro de otro cadena, y devuelve la cantidad de veces que coincida, si no encuentra coincidencia devuelve 0.
contarCoincidencias = cadena1.count("Hola")

#cuanta la cantidad de caracteres que tiene una cadena
contarCaracteres = len(cadena1)

#verifica si una cadena empieza con otra cadena dada, si es asi devuelve True, de lo contrario devuelve False.
empiezaCon = cadena1.startswith("h")

#verifica si una cadena termina con otra cadena dada, si es asi devuelve True, de lo contrario devuelve False.
termunaCon = cadena1.endswith("ss")

#remplaza un pedazo de la cadena dada, por otra dada, en caso de no encontrar coincidencias nos devolvera el valor anterior.
cadenaNueva = cadena1.replace("Hola", "hola")

#separa la cadena con la cadena que le pasemos
cadenaSeparada = cadena1.split(",")
print (cadenaSeparada[0])



