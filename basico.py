

# AND -> True, false

#print(True and True)
#print(True and False)
#print(False and True)
#print(False and False)

#resultado = (a > b and b < a)
#resultado = (False and c < 7)
#resultado = (False and False)
#resultado = (False)


#OR -> TRUE FALSE : UNO DE LOS DOS SEA TRUE
#print(True or True)
#print(True or False)
#print(False or True)
#print(False or False)

a = 7
b = 6
c = 5

resultado = (a >= 5 or c > 7)
resultado = (True or False)
resultado = (True)


resultado = ((a >= 5 or c < 3) and (b == 8))
resultado = ((True or False) and (False))
resultado =(True  and False)
resultado = (False)



# a > b
# (a > b) and (c >= b) and (a > c or b >= c)
#(false) and (true) and false
#fakse and true and false
#fakse and false
#false

a = 3
b = 6

#if a >=5 and b <= 6:
	#print("a es mayor o igual que 5 y b es igual o mayor que 6")
#elif a >= 6:
	#print("A es mayor igual que 6")
#else:
	#print("NO SE CUMPLE LA CONDICION")

#BLUCLE CONDICIONAL

#while mientras la condicion sea True
#se ejecuta

contador = 1

while contador <= 10:
	if contador % 2 == 0:
		#print(contador,"es un numero par")
	if contador % 3 == 0:
		#print(contador, "es un numero impar")
	contador += 1

#iteracion es el cuerpo del bucle
#como romper  las iteraciones



lista = [1,2,3,'a',5]
tupla =(1,2,3,'c','d')
longitud = len(lista)


for numero in range(5,18):


lista =[3,4,1,2,5]


listaOrdenada = sorted(lista, reverse = True)


#funcion python
def nombre():
	print("Nombre")

nombre()

