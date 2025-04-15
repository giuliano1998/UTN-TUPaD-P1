# TP 3 - Condicionales
# Giuliano Raschetti
# UTN - Tecnicatura Universitaria en Programación a Distancia

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# 1. Edad - Mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
# Si la edad ingresada es mayor a 18, se muestra el mensaje

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# 2. Nota - Aprobado/Desaprobado
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# Se usa if-else para controlar el resultado según la condición

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# 3. Número par obligatorio
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
# El operador % devuelve el resto; si el resto de dividir por 2 es 0, es par sino solcita ingresar un numero par 

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

# 4. Clasificación por edad
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
# Uso de elif para comparar múltiples rangos

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# 5. Validación de contraseña por longitud
contraseña = input("Ingrese su contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# len() calcula la cantidad de caracteres del string

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números.

# 6. Estadística: moda, mediana y media
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
m = mean(numeros_aleatorios)
me = median(numeros_aleatorios)
mo = mode(numeros_aleatorios)

print("Media:", m)
print("Mediana:", me)
print("Moda:", mo)

if m > me and me > mo:
    print("Sesgo positivo")
elif m < me and me < mo:
    print("Sesgo negativo")
elif m == me == mo:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# 7. String termina en vocal
texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)
# Se analiza el último carácter usando texto[-1] y se pasa a minúscula

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# 8. Transformar nombre según opción
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (MAY), 2 (min), o 3 (Primera letra MAY): "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# 9. Clasificación de terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año. Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# 10. Determinar estación según hemisferio, mes y día
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Mes (1-12): "))
dia = int(input("Día: "))

# Para facilitar el cálculo, convertimos mes y día a un número "día del año"
from datetime import date
fecha = date(2023, mes, dia)

if hemisferio == "N":
    if date(2023, 12, 21) <= fecha or fecha <= date(2023, 3, 20):
        print("Invierno")
    elif date(2023, 3, 21) <= fecha <= date(2023, 6, 20):
        print("Primavera")
    elif date(2023, 6, 21) <= fecha <= date(2023, 9, 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if date(2023, 12, 21) <= fecha or fecha <= date(2023, 3, 20):
        print("Verano")
    elif date(2023, 3, 21) <= fecha <= date(2023, 6, 20):
        print("Otoño")
    elif date(2023, 6, 21) <= fecha <= date(2023, 9, 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio no válido")
