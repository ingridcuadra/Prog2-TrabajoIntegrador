"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""

from cancion import Cancion
from circulo import Circulo

#Ejercicio 2
print("Ejercicio 2")
cancion1 = Cancion("Worth fighting for", 264, "Metal")
cancion2 = Cancion("Thriller", 357, "Pop")
cancion3 = Cancion("The Sky is crying", 300, "Blues")

#Ejercicio 3
print("Ejercicio 3")
print(cancion1.obtenerGenero())
print(cancion2.obtenerGenero())
print(cancion3.obtenerGenero())


#Ejercicio 4
print("Ejercicio 4")
cancion2.establecerGenero("Jazz")
print(cancion2.obtenerGenero())

#Ejercicio 6
print("Ejercicio 6")
circulo1 = Circulo(7)
circulo2 = Circulo(9)
circulo3 = Circulo(4)

#Ejercicio 7
print("Ejercicio 7")
print(circulo1.obtenerDiametro())
print(circulo2.obtenerDiametro())
print(circulo3.obtenerDiametro())

#Ejercicio 8
print("Ejercicio 8")
print(circulo1.PI)
print(circulo2.PI)
print(circulo3.PI)

#Ejercicio 9
print("Ejercicio 9")
circulo4 = Circulo(5)
circulo5 = Circulo(5)
print(circulo4 == circulo5)

#Ejercicio 10
print("Ejercicio 10")
print(circulo4.obtenerPerimetro() == circulo5.obtenerPerimetro())
