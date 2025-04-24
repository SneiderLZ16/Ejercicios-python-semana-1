
"""
#Ejercicio 1   
# Solicitar el nombre y la edad del usuario
nombre = input("Por favor, ingresa tu nombre: ")
edad = input("Por favor, ingresa tu edad: ")

# Mostrar el mensaje con el nombre y la edad
print(f" Hola {nombre}, tienes {edad} años.")
"""

"""
#Ejercicio 2
# Solicitar dos números enteros al usuario
numero1 = int(input("Por favor, ingresa el primer número entero: "))
numero2 = int(input("Por favor, ingresa el segundo número entero: "))

# Calcular y mostrar la suma de ambos números
suma = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es {suma}.")

"""
"""
#Ejercicio 3
# Solicitar dos números decimales al usuario
decimal1 = float(input("Por favor, ingresa el primer número decimal: "))
decimal2 = float(input("Por favor, ingresa el segundo número decimal: "))

# Calcular y mostrar la multiplicación de ambos números
multiplicacion = decimal1 * decimal2
print(f"La multiplicación de {decimal1} y {decimal2} es {multiplicacion}.")

"""
"""
#Ejercicio 4
# Solicitar un número entero al usuario
numero = int(input("Por favor, ingresa un número entero: "))

# Calcular el doble y el triple del número
doble = numero * 2
triple = numero * 3

# Mostrar el doble y el triple separados por coma
print(f"El doble de {numero} es {doble}, y el triple es {triple}.")
"""


#Ejercicio 5
# Solicitar una palabra y un número entero al usuario
palabra = input("Por favor, ingresa una palabra: ")
repeticiones = int(input("Por favor, ingresa cuantas veces quiere se repita la palabra: "))

rp=((palabra+ " ") * repeticiones)
# Mostrar la palabra repetida el número de veces indicado
print(rp)



"""
#Ejercicio 6
# Solicitar dos números al usuario
numerador = float(input("Por favor, ingresa el numerador: "))
denominador = float(input("Por favor, ingresa el denominador: "))

# Verificar que el denominador no sea cero antes de dividir
if denominador != 0:
    division = numerador / denominador
    print(f"El resultado de dividir {numerador} entre {denominador} es {division}.")
else:
    print("No se puede dividir entre cero.")

"""

"""
#Ejercicio 7
# Solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")
con=nombre.split(" ")
# Crear una cadena vacía para almacenar el resultado
cad = ""
cad= cad.join(con)
# Calcular la cantidad de letras en el nombre
cantidad_letras = len(cad)

# Mostrar la cantidad de letras
print(f"Tu nombre, {nombre}, tiene {cantidad_letras} letras.")
"""

"""
#Ejercicio 8
# Solicitar dos números enteros al usuario
numero1 = int(input("Por favor, ingresa el primer número entero: "))
numero2 = int(input("Por favor, ingresa el segundo número entero: "))

# Verificar que el segundo número no sea cero antes de realizar las operaciones
if numero2 != 0:
    division_entera = numero1 // numero2
    modulo = numero1 % numero2
    print(f"La división entera de {numero1} entre {numero2} es {division_entera}.")
    print(f"El módulo de {numero1} entre {numero2} es {modulo}.")
else:
    print("No se puede realizar la división entera ni calcular el módulo con un divisor igual a cero.")
"""

"""
#Ejercicio 9
# Solicitar dos números al usuario
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

# Calcular las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Verificar que el segundo número no sea cero antes de dividir
if numero2 != 0:
    division = numero1 / numero2
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")
else:
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: No se puede dividir entre cero")
"""

"""
#Ejercicio 10
# Solicitar un número entero al usuario
numero = int(input("Por favor, ingresa un número entero: "))

# Calcular el número elevado a la 2 y a la 3
cuadrado = numero ** 2
cubo = numero ** 3

# Mostrar los resultados usando f-strings
print(f"El número {numero} elevado a la 2 es {cuadrado}, y elevado a la 3 es {cubo}.")
"""

"""
#Ejercicio 11
# Solicitar un número decimal al usuario
numero_decimal = float(input("Por favor, ingresa un número decimal: "))

# Mostrar solo la parte entera del número
parte_entera = int(numero_decimal)
print(f"La parte entera de {numero_decimal} es {parte_entera}.")

"""

"""
#Ejercicio 12

# Solicitar la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si es mayor de 18
es_mayor = edad >= 18

# Mostrar si es mayor de 18
print(f"¿Eres mayor de 18 años? {es_mayor}")
"""

"""
#Ejercicio 13
# Solicitar dos números enteros al usuario
numero1 = int(input("Por favor, ingresa el primer número entero: "))
numero2 = int(input("Por favor, ingresa el segundo número entero: "))

# Verificar si los números son iguales
son_iguales = numero1 == numero2

# Mostrar si los números son iguales
print(f"¿Los números {numero1} y {numero2} son iguales? {son_iguales}")
"""

"""
#Ejercicio 14
# Solicitar dos números al usuario
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

# Verificar si el primero es mayor que el segundo
es_mayor = numero1 > numero2

# Mostrar si el primer número es mayor que el segundo
print(f"¿El número {numero1} es mayor que {numero2}? {es_mayor}")
"""

"""
#Ejercicio 15
# Solicitar dos números al usuario
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

# Verificar si el primero es menor o igual que el segundo
es_menor_o_igual = numero1 <= numero2

# Mostrar si el primer número es menor o igual que el segundo
print(f"¿El número {numero1} es menor o igual que {numero2}? {es_menor_o_igual}")
"""

"""
#Ejercicio 16
# Solicitar dos números al usuario
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

# Verificar si ambos números son mayores que 10
ambos_mayores = numero1 > 10 and numero2 > 10

# Mostrar si ambos números son mayores que 10
print(f"¿Ambos números son mayores que 10? {ambos_mayores}")
"""

"""
#Ejercicio 17
# Solicitar dos números al usuario
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

# Verificar si al menos uno de los números es mayor que 10
al_menos_uno_mayor = numero1 > 10 or numero2 > 10

# Mostrar si al menos uno de los números es mayor que 10
print(f"¿Al menos uno de los números es mayor que 10? {al_menos_uno_mayor}")

"""

"""
#Ejercicio 18
# Solicitar dos números al usuario
numero1 = int(input("Por favor, ingresa el primer número: "))
numero2 = int(input("Por favor, ingresa el segundo número: "))

# Verificar si el primero no es igual al segundo
no_son_iguales = not (numero1 == numero2)

# Mostrar si el primero no es igual al segundo
print(f"¿El número {numero1} no es igual al número {numero2}? {no_son_iguales}")
"""

"""
#Ejercicio 19
# Solicitar tres números al usuario
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
numero3 = float(input("Por favor, ingresa el tercer número: "))

# Calcular el promedio
promedio = (numero1 + numero2 + numero3) / 3

# Mostrar el promedio
print(f"El promedio de los números ingresados es {promedio}.")
"""

"""
#Ejercicio 20
# Solicitar un número entero al usuario
numero = int(input("Por favor, ingresa un número entero: "))

# Verificar si el número es divisible entre 5
es_divisible = numero % 5 == 0

# Mostrar si el número es divisible entre 5
print(f"¿El número {numero} es divisible entre 5? {es_divisible}")
"""

