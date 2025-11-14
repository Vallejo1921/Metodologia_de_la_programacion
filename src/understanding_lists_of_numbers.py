"""


"""

#La funcion range() me genera una lista de numeros
# en un rango especifico
#Por ejemplo la funcion range(5) me genera una lista de numeros

numeros = list(range(10))
print(numeros)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numeros))  # Salida: <class 'list'>

#podemos generar lo mismo con un for loop
for num in range(10):
    print(num)
    print(type(num))  

for num in range(1, 5):
    print(num)  

print("\n")

print("Numeros impares:")
for num in range(1, 10, 2):  #numeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))

print("\n")

print("Numeros pares:")
for num in range(2, 11, 2):  #numeros pares del 2 al 8
    print(num)
even_numbers = list(range(2, 11, 2))
print("\n")

## podemos crear cualquier lista de numeros con range()
## utilizando range() y list() 
print("\n Primeros 10 numeros al cuadrado:")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares) # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("\n")

#metodos build-in para listas de numeros
print("\n Metodos buil-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Listas de digitos: {digits}")
print("valor minimo:", min(digits))

print("valor maximo:", max(digits))
print("suma de todos los digitos:", sum(digits))

# List 
