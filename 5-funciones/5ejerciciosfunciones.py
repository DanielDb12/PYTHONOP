#Escribe una función que calcule el área de un triángulo, 
#recibiendo la altura y la base como parámetros  

from math import pi

def triangulo(alt ,base ,c):
	return alt + base // c


resultado = triangulo(5,6,7)
#print(resultado)


#que calcule el área de un círculo recibiendo el radio del mismo.

def circulo(radio):
	return pi * radio ** 2


resultado2 = circulo(60)
#print(resultado2)


#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def primo(a):
	
	if a % 2 == 0:
		print("primo")
	else:
		print("no es primo")


#primo(5)










#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(año):
	if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
		print("es bisiesto")

	else:
		print("no es bisiesto")	
	



#bisiesto(1700)

	