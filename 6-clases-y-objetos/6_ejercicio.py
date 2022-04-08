'''class Vehiculo:

	Color = "Rojo"
	Ruedas = 5
	Puertas  = 4

class Coche(Vehiculo):
	Velocidad = 6
	Cilindrada = 1600	


p = Coche()
print("Carro:",p.Color,
	"Ruedas:",p.Ruedas,"Puertas" ,p.Puertas,
	 "Velocidad", p.Velocidad,
	 "Cilindrada", p.Cilindrada)
	'''
'''En este segundo ejercicio, tendréis que crear un programa que 
tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Deberéis de definir 
los métodos para inicializar sus atributos, imprimirlos 
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''
class Alumno:
	Nombre = "Daniel"
	Nota = 20

	def alumno(self, nombre):
		self.Nombre = nombre

	def calificacion(self, nota):
		self.Nota = nota
		if nota <= 9:
			print(nota, "no apruebas")
		else:
			print(nota,"apruebas la materia" )
		


		

al = Alumno()
al.alumno("Fernando")
print(al.Nombre)
al.calificacion(8)
