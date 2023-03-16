
#le pedimos al usuario que nos diga una frase o varias
frase = input("Dime un frase y te calculare cuanto tardarias si tuvieras que decirlas: ")

#creamos una lista de todas las palabras de la frase (se separan cada vez que haya un espacio)
palabrasSeparadas = frase.split(" ")
print(palabrasSeparadas)
#usamos len() para ver la cantidad de elementos que hay en la lista
cantidadPalabras = len(palabrasSeparadas)


#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidadPalabras > 120:
    print("Ya para elvis tampoco te pedi un testamento")

#calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"Dijiste {cantidadPalabras} palabras, y tardarias {cantidadPalabras/2} segundo en decirlo")
print(f"Elvis lo diria en {cantidadPalabras *100 // 2*1.3 / 100} segundos")