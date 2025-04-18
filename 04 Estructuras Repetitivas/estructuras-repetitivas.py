"# Actividades del TP" 
#Actividades
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):  # 101 porque el rango no incluye el final
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
numero = input("Ingresá un número entero: ")
print("Cantidad de dígitos:", len(numero.lstrip('-'))) #lstrip permite ignorar el simbolo "-" en caso de ser puesto por usuario


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))

# Aseguramos que a sea menor que b
inicio = min(a, b) + 1
fin = max(a, b)

suma = 0
for i in range(inicio, fin):
    suma += i

print("La suma es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado #cuando el usuario ingrese
#un 0.
total = 0
while True:
    numero = int(input("Ingresá un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print("Total acumulado:", total)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar #el número.
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break
    else:
        print("Incorrecto. Probá de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for i in range(100, -1, -1):  # de 100 a 0, paso -1
    if i % 2 == 0:
        print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
n = int(input("Ingresá un número positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print("La suma es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = impares = positivos = negativos = 0
cantidad = 100  # podés cambiar este número para testear

for _ in range(cantidad):
    num = int(input("Ingresá un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
cantidad = 100  # podés reducir este número para pruebas
suma = 0

for _ in range(cantidad):
    num = int(input("Ingresá un número: "))
    suma += num

media = suma / cantidad
print("La media es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresá un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
