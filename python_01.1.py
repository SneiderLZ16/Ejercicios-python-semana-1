import math

"""
# Solicitar dos valores al usuario
valor1 = input("Introduce el primer valor: ")
valor2 = input("Introduce el segundo valor: ")

# Intercambiar los valores
valor1, valor2 = valor2, valor1

# Imprimir los valores intercambiados
print("Después de intercambiar:")
print("Primer valor:", valor1)
print("Segundo valor:", valor2)
    """
    
    
    
    
"""
# Solicitar un número de tres cifras al usuario
numero = int(input("Introduce un número de tres cifras: "))

# Extraer centenas, decenas y unidades
centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10

# Invertir el orden de las cifras
numero_invertido = (unidades * 100) + (decenas * 10) + centenas

# Imprimir el número invertido
print("El número invertido es:", numero_invertido)
"""

"""
# Solicitar al usuario un número de segundos
segundos_totales = int(input("Introduce un número de segundos: "))

# Calcular horas, minutos y segundos
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

# Imprimir el resultado
print(f"{segundos_totales} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")

"""
"""
# Solicitar día, mes y año al usuario
dia = input("Introduce el día (DD): ")
mes = input("Introduce el mes (MM): ")
anio = input("Introduce el año (AAAA): ")

# Imprimir la fecha en los dos formatos
print(f"{dia}/{mes}/{año}")
print(f"{año}-{mes}-{dia}")

"""

"""
# Solicitar una temperatura en Fahrenheit al usuario
fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))

# Convertir a Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Imprimir el resultado
print(f"{fahrenheit}°F son equivalentes a {celsius:.2f}°C.")

"""
"""
# Solicitar el costo de la comida al usuario
costo_comida = float(input("Introduce el costo de la comida: "))

# Calcular las propinas
propina_10 = costo_comida * 0.10
propina_15 = costo_comida * 0.15
propina_20 = costo_comida * 0.20

# Calcular los totales a pagar
total_10 = costo_comida + propina_10
total_15 = costo_comida + propina_15
total_20 = costo_comida + propina_20

# Imprimir los resultados
print(f"Con una propina del 10%: ${total_10:.2f}")
print(f"Con una propina del 15%: ${total_15:.2f}")
print(f"Con una propina del 20%: ${total_20:.2f}")

"""
"""
# Solicitar un número de cuatro cifras al usuario
numero = int(input("Introduce un número de cuatro cifras: "))

# Extraer cada dígito
miles = numero // 1000
centenas = (numero % 1000) // 100
decenas = (numero % 100) // 10
unidades = numero % 10

# Imprimir los dígitos separados por coma
print(f"{miles},{centenas},{decenas},{unidades}")

"""

"""
# Solicitar un precio al usuario
precio = float(input("Introduce un precio: "))

# Imprimir el precio con dos decimales y símbolo de moneda
print(f"${precio:.2f}")

"""

"""
# Solicitar una cantidad de minutos al usuario
minutos_totales = int(input("Introduce una cantidad de minutos: "))

# Calcular días, horas y minutos
dias = minutos_totales // 1440
horas = (minutos_totales % 1440) // 60
minutos = minutos_totales % 60

# Imprimir el resultado
print(f"{minutos_totales} minutos son {dias} días, {horas} horas y {minutos} minutos.")

"""


# Solicitar el radio del círculo al usuario
radio = float(input("Introduce el radio del círculo: "))

# Calcular el área y el perímetro (circunferencia)
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

# Imprimir los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
