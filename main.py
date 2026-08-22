#punto numero 1 parte B de las cosngnas 
def realizar_calculo():

    operacion = input("Ingrese la operación matemática que quiere hacer(suma, resta, multiplicacion, division):  ")

    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    if operacion == "suma":
        resultado = primer_numero + segundo_numero

    elif operacion == "resta":
        resultado = primer_numero - segundo_numero

    elif operacion == "multiplicacion":
        resultado = primer_numero * segundo_numero

    elif operacion == "division":
        resultado = primer_numero / segundo_numero

    else:
        print("Operación no válida")
        return

    print("El resultado es: ", resultado)


realizar_calculo()

#ej2


def numeros_orden_ascendente():
    pedir_numero = int(input("Ingrese un numero: "))

    # Pasarlo a string para poder iterar los números
    for i in range(len(str(pedir_numero)) - 1):
        if str(pedir_numero)[i] > str(pedir_numero)[i + 1]:
            return False

    return True


resultado = numeros_orden_ascendente()
print(resultado)

#ejer3
def numeros_impares_juntos(numeros):
    numeros_impares = [] 

    for numero in numeros:
        if numero % 2 != 0:
            numeros_impares.append(str(numero))

    return ",".join(numeros_impares)


numeros_ingresados = []

for i in range(5):
    numero = int(input("ingresa un numero: "))
    numeros_ingresados.append(numero)


resultado_impares = numeros_impares_juntos(numeros_ingresados)
print("Los numeros impares que fueron ingresados son: " + resultado_impares)

#Ejercicio N.4
print("Ejercicio N. 4")

def lista_elementos_en_comun(lista1,lista2):
    lista_nueva = []
    for n in lista1:
        if n in lista2:
            if n not in lista_nueva:
                lista_nueva.append(n)
    print(lista_nueva)

lista_elementos_en_comun(['p','o','t','u'], ['p','w','t','p','u'])

#Ejercicio N.5
print("Ejercicio N. 5")

def clave_valida(clave):
    
    if 6<= len(clave)<=20 and " " not in clave:
        for c in clave:
            if c.isdigit():
                return True
    return False

print(clave_valida("1sdfwer"))

#Ejercicio N.6
print("Ejercicio N. 6")

def persona_mayor_de_edad(edad):
    return edad>=18

print(persona_mayor_de_edad(20))