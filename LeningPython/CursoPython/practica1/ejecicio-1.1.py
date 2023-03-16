otrosCursos_Min = 2.5
otrosCursos_Max = 7
otrosCursos_Promedio = 4
nustroCurso = 1.5

#Diferencia de crudos
crudo_promedio = 5
crudo_Nuestro = 3.5


#diferencia con Min
diferencia_con_Min = 100 - (nustroCurso / otrosCursos_Min * 100)
otrosCursos_Max = 100 - (nustroCurso * 1000 // otrosCursos_Max / 10)
diferencia_conPromedio = 100 - (nustroCurso / otrosCursos_Promedio * 100)

#Cantidad  de tiempo de vacio removido

tiempoVacio_promedio = 100 - (otrosCursos_Promedio * 1000 // crudo_promedio / 10)
tiempoVacio_nuestro = 100 - (nustroCurso * 1000 // crudo_Nuestro / 10)

print("------------------------------")
print("Nuestro curso dura")

print(f" - un {diferencia_con_Min}% menos que el mas rapido")
print(f" - un {otrosCursos_Max}% menos que el mas Lento")
print(f" - un {diferencia_conPromedio}% menos que el mas Promedio")
print("------------------------------")

#Mostrando la cantidad de espacios vacios que se remuven (ejecicios B)
print(f"El curso promedio elimina un {tiempoVacio_promedio}% del tiempo vacio")
print(f"Nuestro curso elimina un {tiempoVacio_nuestro}% del tiempo vacio")
print("------------------------------")

#mostrando diferencia de los cursos durante 10h
print(f"Ver 10 hora de este curso equivale a ver {otrosCursos_Promedio * 100 // nustroCurso / 10} horas de otros cursos")
print(f"Ver 10 hora de otros curso equivale a ver {nustroCurso * 100 // otrosCursos_Promedio / 10} horas de nuestro cursos")
print("------------------------------")
