def matematica(a,b):
	def suma(a,b):
		print(a + b)

	def resta(a,b):
		print(a - b)

 
	suma(a,b)
	resta(a,b)
	

matematica(5,6)

def suma(a=1, b=2, c=3):
	print(a + b + c)

suma(b=5,c=3,a=5)

def fun():
	print(a + b + c)

suma(b=5,c=3,a=5)

#*tupla |**diccionario

def funcion1(**kwargs):
	for key,value in kwargs.items():
		print(key, "=", value)


funcion1(vivienda="piso",coche="rojo")

#NAME PARAMETER
#IN PARA BUSCAR

def funcion0(**kwargs):
	#if 'COCHE' in kwargs and kwargs['COCHE'] == 'BONITO':
	#	in sirve para saber si hay una cosa dentro de otra
	# busca la palabra coche dentro de kargs and(y exites) 
	if 'coche' in kwargs and kwargs['coche'] == 'bonito':
		return

	if kwargs['coche'] == 'bonito':
		print("Tu coche es bonito")	


funcion2()

def funcion2(**kwargs):
	#if 'COCHE' in kwargs and kwargs['COCHE'] == 'BONITO':
	#	print("TU COCHE ES BONITO")
	if 'coche' not in kwargs:
		return

	if kwargs['coche'] == 'bonito':
		print("Tu coche es bonito")	


funcion2()

#metodo 1 return
def funcion3(a, b):
	 return a + b, a-b, a* b, a/b


resultado = funcion3(2,4)
print(resultado[0])

#metodo 2 return
def funcion4(a, b):
	 return a + b, a-b, a* b, a/b


suma,resta,multi,divi = funcion4(5,6)
print(suma)
print(resta)
print(multi)
print(divi)

#_ guion bajo para ignorar un valor

def funcion5(**kwargs):
	 inicial = kwargs['inicial']
	 final = kwargs['final']

	 resultado = 0

	 for x in range(inicial, final + 1):
	 	resultado += x

	 return resultado

	

print(funcion5(inicial=15, final=30))


#operador ternario

def funcion5(**kwargs):

	 inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
	 final = kwargs['final'] if 'final' in kwargs else inicial

	 resultado = 0

	 for x in range(inicial, final + 1):
	 	resultado += x

	 return resultado

	

print(funcion5())

#funciones anonima o landa

anonima = lambda nombre, nombre2: print("hola",nombre, "adios", nombre2)
anonima("daniel", "duarte")

sumatoria = lambda x: x+x
print(sumatoria(2))


