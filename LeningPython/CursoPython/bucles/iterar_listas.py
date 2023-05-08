animales = ["perro", "loro", "caballo"]
numeros = [2, 10, 15]


#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")


#recorriendo la lista de numero y multiplicandola por 10
for numero in numeros:
    resultado = numero*10
    print(resultado)
    
    
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {animales}")
    print(f"recorriendo lista 2: {numeros}")
    

for num in range(10, 50):
    print(num)
    
#envitando que muestre un elemento con la sentencia continue
for animal in animales:
    if animal == "loro":
        continue
    print(f"Me gusta el: {animal}")
    
    
frutas = ["manzana", "mandarina", "naranja", "pera", "uva", "mango"]

    
#envitando que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me comi: {fruta}")
    if fruta == "pera":
        break
print("ya deja de comer")


#for en una sola linea de codigo (duplicamos los numeros)
numeroS = [5, 10, 30]
numeros_duplicados = [x*2 for x in numeroS]
print(numeros_duplicados)
    