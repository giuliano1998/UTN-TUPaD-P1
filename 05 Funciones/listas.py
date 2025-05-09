# Trabajo Práctico 5 - Listas - UTN a Distancia

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiplos = list(range(4, 101, 4))
print("1) Múltiplos de 4:", multiplos)

# 2) Crear una lista con cinco elementos y mostrar el penúltimo
gustos = ['música', 'pizza', 'deporte', 'viajar', 'leer']
print("2) Penúltimo elemento:", gustos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante
lista_vacia = []
lista_vacia.append("uno")
lista_vacia.append("dos")
lista_vacia.append("tres")
print("3) Lista con append:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con "loro" y "oso"
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista animales modificada:", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza

#el siguiente codigo crea una lista la cual se llama "numeros" con cinco valores enteros, Luego, con la función max(numeros) se busca el valor máximo dentro de esa lista.La función remove() elimina la primera aparición del valor indicado. [22].Por ultimo se imprimi la nueva lista [8, 15, 3, 7]


# 6) Crear lista del 10 al 30 (incluido) haciendo saltos de 5 y mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("6) Dos primeros elementos:", numeros[:2])

# 7) Reemplazar los valores centrales (índices 1 y 2) de la lista "autos"
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["civic", "corolla"]
print("7) Lista autos modificada:", autos)

# 8) Crear lista "dobles" y agregar el doble de 5, 10 y 15 usando append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista dobles:", dobles)

# 9) Modificar lista anidada "compras"
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")               # a) agregar "jugo" al tercer cliente
compras[1][1] = "tallarines"            # b) reemplazar "fideos" por "tallarines"
compras[0].remove("pan")                # c) eliminar "pan"
print("9) Lista compras modificada:", compras)

# 10) Crear una lista anidada llamada "lista_anidada" con estructura dada
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10) Lista anidada:", lista_anidada)
