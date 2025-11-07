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
        EL metodo insert() requiere dos argumentos: el indice del lugar donde se desea agregar el nuevo elemento 
            y el valor del nuevo elemento

       -append(): agrega un elemento al final de la lista
       El elemento agregado con append() siempre se agrega al final de la lista       
       La diferencia entre append() e insert() es que insert() permite especificar la posicion del nuevo elemento
       y la formula general es: list.insert(index, element)
       en el caso de append() es: list.append(element)
       otros metodos para agregar elementos a una lista son extend() y + operator
       los cuales tienen formulas como: list1.extend(list2) y list3 = list1 + list2
       y ambos agregan los elementos de list2 al final de list1
       ejemplo:
       list1 = [1, 2, 3] 
       list1.extend([4, 5])
           print(list1)  # Salida [1, 2, 3, 4, 5]

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

""""
eliminar elementos de una lista
  - del: elimina un elemento en una posicion especifica de la lista
  la declaracion del index elimina el elemento en la posicion especificada


"""
print("\nEliminar elementos de una lista: declaracion del index\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[2]
print(motorcycles)  # Salida ['honda', 'yamaha', 'ducati']


"""
    eliminar elementos de una lista
     - pop(): elimina el ultimo elemento de la lista y lo devuelve
     el metodo pop() es util cuando se desea utilizar el elemento eliminado despues de eliminarlo
     el metodo pop() no requiere argumentos


"""

print("\nEliminar elementos de una lista: method pop()\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki', 'ducati']
popped_motorcycle = motorcycles.pop()
print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki']
print(f'La motocicleta que fue eliminada es {popped_motorcycle.title()}.')
# Salida La motocicleta que fue eliminada es Ducati.

"""
tambien pop es util para eliminar elementos en cualquier posicion de la lista
ejemplo:
   - pop(index): elimina el elemento en la posicion especificada y lo devuelve
 formula general: list.pop(index)

"""

"""
  eliminar elementos de una lista
     - remove(): elimina la primera ocurrencia de un valor especifico en la lista
     el metodo remove(value) toma un argumento: el valor del elemento que se desea eliminar 

"""


print("\nEliminar elementos de una lista: method remove()\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'yamaha']
print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki', 'ducati', 'yamaha']
motorcycles.remove('yamaha')
print(motorcycles)  # Salida ['honda', 'suzuki', 'ducati', 'yamaha']

print("\nEliminar elementos de una lista: method remove() con mensaje\n")

names = ['alice', 'bob', 'charly', 'david', 'charly']
print(names)  
del_name = input('Ingrese el nombre que desea eliminar de la lista: ').lower()
names.remove(del_name)
print(f'{del_name.title()} fue eliminado de la lista.')
print(names)

"""
ahora si quisiera que el usuario pudiera eliminar otro aparte de charly, podria hacer lo siguiente:
"""

print("\nEliminar elementos de una lista: method remove() con mensaje mejorado\n")

names = ['alice', 'bob', 'charly', 'david', 'charly']
print(names)
del_name = input('Ingrese el nombre que desea eliminar de la lista: ').lower()
if del_name in names:
    names.remove(del_name)
    print(f'{del_name.title()} fue eliminado de la lista.')
else:
    print(f'El nombre {del_name.title()} no se encuentra en la lista.')
print(names)


"""
ordenar una lista
   metodo de ordenar lista: sort()
   lo que hace es ordenar la lista de forma permanente en orden alfabetico
    
  """

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nOrdenar una lista: method sort()\n")

print(cars)

cars.sort(reverse=True)

print(cars)  # Salida ['audi', 'bmw', 'subaru', 'toyota']

"""
Metodo reverse()

"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print("\nInvertir el orden de una lista: method reverse()\n")
print(motorcycles)  # Salida ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.reverse()
print(motorcycles)  # Salida ['ducati', 'suzuki', 'yamaha', 'honda']

"""
cantidad de elementos en una lista
   Metodo built-in len()
"""
cars = ['bmw', 'audi', 'toyota']

print("\nCantidad de elementos en una lista: method len()\n")
print(cars)  # Salida ['bmw', 'audi', 'toyota']
print(len(cars))  # Salida 3
print(f'La cantidad de elementos en la lista es: {len(cars)}')  

"""
Metodo built-in

sorted()
   .sorted() permite ordenar una lista temporalmente sin modificar el orden original de la lista

"""

Names = ['Charlie', 'Alice', 'Bob', 'David']

print("\nOrdenar una lista temporalmente: method sorted()\n")

print(Names)  # Salida ['Charlie', 'Alice', 'Bob', 'David']
print(sorted(Names))  
print("Los nombres ordenados temporalmente son:")
print(sorted(Names))  
print("Los nombres en su orden original son:")
print(Names)  

