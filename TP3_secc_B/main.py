"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""
from producto import Producto
from empleado import Empleado
from empresa import Empresa

# Ejercicio 10

empresa1 = Empresa("Siamo fuori")
empresa2 = Empresa("Ferreteria Passo")

empleado1 = Empleado("Carlo", "Magno")
empleado2 = Empleado("Gio", "Cufaro")
empleado3 = Empleado("Dario", "Sinagra")
empleado4 = Empleado("Vincenzo", "Beretta")
empleado5 = Empleado("Giuseppe", "Mazzini")
empleado6 = Empleado("Mario", "Volpe")

producto1 = Producto("Camisa")
producto2 = Producto("Pantalon")
producto3 = Producto("Martillo")
producto4 = Producto("Destornillador")

empresa1.altaEmpleado(empleado1)
empresa1.altaEmpleado(empleado2)
empresa1.altaEmpleado(empleado3)
empresa2.altaEmpleado(empleado4)
empresa2.altaEmpleado(empleado5)
empresa2.altaEmpleado(empleado6)

empresa1.agregarProducto(producto1)
empresa1.agregarProducto(producto2)
empresa2.agregarProducto(producto3)
empresa2.agregarProducto(producto4)

print(empresa1)
print(empresa2)

empresa1.bajaEmpleado(empleado1)
empresa1.bajaEmpleado(empleado2)


print(empresa1)
print(empresa2)


