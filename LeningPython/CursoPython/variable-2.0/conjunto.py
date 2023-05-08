#conjunto con set()
conjunto = set(["dato 1", "dato 2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}
#print(conjunto2)


#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#verificando su es un subcconjunto?
resultado = conjunto2.issubset(conjunto1) 
'''es lo mismo su usamos:'''
resultado = conjunto2 <= conjunto1
#print(resultado)

#verificando su es un superconjunto?
resultado = conjunto2.issubset(conjunto1) 
'''es lo mismo su usamos:'''
resultado = conjunto2 > conjunto1
#print(resultado)

#verificar si hay un numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)