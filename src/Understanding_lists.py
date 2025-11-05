##Listas
# Una lista es una coleccion ordenada y mutable de elementos
# se pueden crear listas utilizando corchetes  y separando los elementos con comas

Frutas = ['manzana', 'banana', 'cereza']
print(Frutas) #Salida ['manzana', 'banana', 'cereza']

"""



"""
print(Frutas[0].upper())    #Salida manzana
print(Frutas[2].title())    #Salida cereza


# print(frutas[3]) # IndexError: list index out of range

# Acceder al ultimo elemento de una lista
print(Frutas[-1].capitalize())  # Salida cereza
print(Frutas[-2])  # Salida banana
print(Frutas[-3])  # Salida manzana

my_favorite_Fruit = Frutas[0].title()

message = f'Mi fruta favorita es {Frutas[0].title()}.'
print(message)  # Salida Mi fruta favorita es Manzana.



"""
agregar elementos a una lista

     - append(): agrega un elemento al final de la lista
     


"""
print("\nAgregar elementos a una lista: method append()\n")

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')

print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki', 'ducati']

"""
          Agregar elementos en a una lista
        - insert(): agrega un elemento en una posicion especifica de la lista
"""
print("\nAgregar elementos a una lista: method insert()\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)  # Salida ['ducati', 'honda', 'yamaha', 'suzuki']

"""
ejemplo_lista
"""

print(motorcycles)  # Salida ['ducati', 'honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'bmw')
print(motorcycles)  # Salida ['ducati', 'honda', 'bmw', 'yamaha', 'suzuki']

