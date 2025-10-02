i = 0
for i in range (1, 21):
    if i % 2 == 0:
        print(i, "Par")
    else:
        print(i, "Impar")
        
# calcula la suma de los número impares del 1 al 50usando un bucle for
suma = 0
for i in range(1, 51):
    if i % 2 != 0:
        suma += i
print("La suma de los números impares del 1 al 50 es:", suma)

#Tienes la lista de números [2, 5, 8, 3, 10] crea una nueva lista que contenga el cuadrdado de los número mayores que 5
numeros = [2, 5, 8, 3, 10]
cuadrados_mayores_5 = []
for n in numeros:
    if n > 5:
        cuadrados_mayores_5.append(n ** 2)  
print("Los cuadrados de los números mayores que 5 son:", cuadrados_mayores_5)

# tienes la lista words = ["cat", "elephant, "dog, "giraffe"] imprime solo las palabras con mas de 4 letras y cuantas letras tiene cada una
words = ["cat", "elephant", "dog", "giraffe"]
for word in words:
    if len(word) > 4:
        print(f"{word} tiene {len(word)} letras")


# tienes la lista numbers = [5, 12, 3, 20, 7] encuentra el número más grande y el más pequeño usando un bucles
numbers = [5, 12, 3, 20, 7]
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("El número más grande es:", max_num)
print("El número más pequeño es:", min_num)


# imprime un triángulo de 6 filas usando bucles anidados
filas = 6
for i in range(1, filas + 1):
    for j in range(i):
        print("*", end="")
    print()  # Salto de línea después de cada fila  
    
# pide al usuario un número y genera su tabla de multiplicar del 1 al 10 usando un bucle for
num = int(input("Introduce un número para generar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   
    
    