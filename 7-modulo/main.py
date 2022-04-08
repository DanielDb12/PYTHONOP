
'''
para llamar un modulo hay que colocarle import y asu vez llamado como se
llama .modulo

siempre que busquemos con sys la ruta se colocara sys

paquete es una coleccion de modulos y paquete en un paquete podemos tener mas paquetes

Python debe tener un fichero especial para llamar un paquete

place holder __pycache__ escribir __all__ ['sumador'.'resta']

import * para llamar todos los paquetes almacenado en el placeholder

'''
#para buscar
import sys

#arreglar de forma vertical
import pprint

'''
def main():
	op = o.Operador()
	print(op.multiplicacion(6,7))
	res = o.suma(6,7)
	resresta = o.resta(7,120)

	print(o.PI)

'''

import operaciones.sumador.sumador
import operaciones.resta.resta


def main():
	#pprint.pprint(sys.path)

	'''sumar = operaciones.suma.suma(6,5)
	print(sumar)

	ml = operaciones.suma.Multiplicador()
	print(ml.multiplica(6,5))
	'''

	sm = operaciones.sumador.sumador.suma(6,5)
	print(sm)

	rs = operaciones.resta.resta.resta(80,60)
	print(rs)


if __name__ == '__main__':
	main()


#modificar una variable por su glovbals tabla de simbolossimbolo

variable = 5
print(variable)

globals()['variable'] = 6 
print(variable)

#locals 

def prueba(inicial):
	valor = 5
	estado = False
	pprint.pprint(locals())

prueba(0)

#diferencia de globals nos muestra el estado global y locals el estado local de la funcion


	