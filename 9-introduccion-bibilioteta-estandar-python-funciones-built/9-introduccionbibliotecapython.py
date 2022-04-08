#python standard python

#Funcione Multihilo

#FUNCION PARALELA

'''import _thread

import time



def horaActual(nombre_thread, tiempo_de_espera):
	count = 0

	while count < 5:
		time.sleep(tiempo_de_espera)
		count += 1
		print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')



_thread.start_new_thread(horaActual, ('_thread_uno',0))
_thread.start_new_thread(horaActual, ('_thread_dos', 2))

print("he disparado hilo")

while True:
	time.sleep(0.1)

'''
#LOGGING
import logging
'''
logging.basicConfig(level=logging.INFO)
logging.info("Arrancando programa")
logging.warning('hace calor')
logging.error('test')
logging.critical('adios')
'''
#FILTER extrae los valores de la lista si se cumple

'''
numeros = [1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
	if x % 2 == 0:
		return True


	return False

resultado = filter(lambda x: x%2 == 0, numeros)
resultado2 = filter(lambda x: str(x).startswith("pep"), ["pepe","pepito","juan"])
print(list(resultado2))

'''
'''
#MAP APLICA UNA FUNCION A TODOS LOS ELEMENTOS DE UNA LISTA

def cuadrado(x):
	return x * x



resultado = map(cuadrado,[1,2,3,4,5])
resultado2 = map(lambda x: x*x, [1,2,3,4,5] )
print(list(resultado2))

'''

'''
#REDUCE VA A EJECUTAR DE MANERA RECURSIVA LA LISTA HASTA QUE SE QUEDE CON UN UNICO ELEMENTO
#reduce se usa con parametros
from functools import reduce

def suma(a,b):
	print(f'a {a} b {b}')
	return a + b


res = reduce(suma,[1,2,3,4,5])
print(res)

'''
'''
#ZIP AREGA ITERABLES UNA TUPLA Y LOS DEVUELVE

cursos = ['python','java']
valor = [10,15,30]
demo = zip(cursos,valor)
print(list(demo))

'''
'''
#ALL Y ANY() PARA VERIFICAR QUE TODAS LA CONDICIONES SE CUMPLAN O TODAS LAS CONDICIONES DE UNA LISTA SE CUMPLA

listaA = [1==1,2==2,3==4]
res = any(listaA)
print(res)

'''
#ROUND REDONDEAR
'''
a =5.5
b = 5.4
c = 5.6
print(round(a))
'''
#min buscar el menor
print(min(5,3,4))

#pow elevar
print(pow(2,4))

#sorted ordenar lista
'''
lista =["x","c","d","a"]
ordenar = sorted(lista, reverse=True, key=lambda x: str(x).startswith('a'))
print(ordenar)

'''

#funciones
#input sirve para preguntar datos al usuario
'''
from getpa30
ss import getpass
a = input("como te llmas?")
passw = getpass('PASSWORD: ')
print(a, passw)
'''
secreto = 50
valor = 0

while valor != secreto:
	valor = int(input("introduce un numero"))

	if valor > secreto:
		print('te volaste')
		continue

	if valor < secreto:
		print('es muy bajo')
		continue


print('Acertaste')

