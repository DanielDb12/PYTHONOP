'''
#Reiniciar Cadenas
numero = 511
texto = "texto"
otromas = 1.2


print("El numero es %d y el texto es %s y tiene %f" % (numero,texto,otromas))

print("El numero es {1} y el texto es {0} y tiene {2}"
	 .format(texto,numero,otromas)
	 )

def suma(a,b):
	return a + b

print("El numero es {numero} y el texto es {texto} y tiene {otromas}"
	 .format(numero=numero,texto=texto,otromas=otromas)
	 )

#STRING 



print(f'el numero es {suma(numero,numero)} y el texto {texto} y tiene {otromas} ')

#Representaciones de una clase repr()

 diferencia str repr ambas muestrann texto pero no son iguales
	
	STR:
	*str no muestra una salida informal para el usuario final
	*Codigo de produccion

	REPR:
	*repr gener muestra una salida de desarrollo es decir una salida tecnica
	*Codigo depuracion o en desarrollo

	Clase no tiene str pero tiene repr se ejecuta repr
	Clase tiene str pero no tiene repr se ejecutara el comportamiento por defecto de python


	sobrecarga de metodo



class Juguete:
	nombre =""
	precio = 0.0

	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

	def __str__(self):
		return f'MI nombre es {self.nombre} y mi precio {self.precio}'

	def __str__(self):
		return f'Mi nombre es {self.nombre} y su precio {self.precio}'

	def __repr__(self):
		return f'Potato({self.nombre},{self.precio})'


j1 = Juguete("Potato",10.5)
demo = str(j1)
print(type(demo))
print(demo)


j1 = Juguete("Potato",20.5)
print(repr(j1))



cadena = "en un lugar del momente"
print(cadena.lower().count('a'))

cadena2 = "la granja del viejo juan"
print(cadena2.count("a"))

cadena3 = "en un lugar de la mancha"
numero = 'a21'
print(cadena3.isalnum())

cadena4 = "                en un lugar de la mancha"
numero = 'a21'
print(cadena4.strip())

cadena5 = "                en un lugar de la mancha"
numero = 'a21'
print(cadena5.lstrip())

cadena6 = "                en un lugar de la mancha"
numero = 'a21'
print(cadena6.rstrip())

cadena7 = "en un lugar de la mancha"
numero = 'a21'
print(cadena7.split('un'))

cadena8 = "en un lugar de la mancha"
numero = 'a21'
print(cadena8.lower().endswith('mancha'))
'''

#llamar un ficher llamas la funcion OPEN

#r: lectura
#a: append
#w: escritura
#x: create

#t: texto
#b: binary
#w+: abierta para escritura y lectura


f = open('/etc/passwd', 'r')

#datos = f.read(18)

#datos = f.readline()

'''datos = "a"

while len(datos) > 0:
	datos = f.readline()
	print(datos)



datos = f.readlines()

f.close()

print(datos)



'''

'''

def main():
	usuarios = listarUsuarios()
	print(usuarios)

	for usuario in usuarios:
		print(f'usuarios: {usuario} ')

def listarUsuarios():
	f = open('/etc/passwd', 'r')
	datos = f.readlines()
	f.close()

	resultado=[]



	for linea in datos:
		if linea[0] == '#':
			continue

		if linea[0] == '_':
			continue

		partes = linea.split(':')
		resultado.append(partes[0])

	return resultado



if __name__ == '__main__':
	main()
'''
'''

lista = [
	'una linea',
	'dos lineas',
	'tres lineas'
]



def escribe(fichero,datos):
	f = open(fichero,'w')

	for linea in datos:
		if not linea.endswith('\n'):
			linea = linea + '\n'
		f.write(linea)

	f.close()



lista = [
	"una linea",
	"dos lineas\n",
	"tres lineas"
]

escribe('mifichero.txt',lista)
'''

''' pickñe sedelizacion y sedializar datos de un objeto convierto un objeto o cualquier 
otra cosa a una secuencia de datos 
'''

import pickle

class Juguete:
	nombre = ""
	precio = 0.0

	def __init__(self,nombre,precio):
		self.nombre = nombre
		self.precio = precio

	def getNombre(self):
		return self.nombre
'''
j1 = Juguete("Potato", 10.5)
f = open('datos.bin', 'wb')
pickle.dump(j1,f)
f.close()
'''

f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()
print(type(potato))
print(potato.getNombre(), "precio: ", potato.precio)
