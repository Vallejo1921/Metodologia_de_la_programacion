#Tema list comprehension
"""
   Una list comprehension combina el for loop y la creacion de nuevos elementos en una sola linea de codigos y tambien
   automaticamente agrega el nuevo elemento a la lista es decir sin tilizar el ".append"

"""

squares=[value**2 for value in range (1, 11)]
print(f"Los numeros de la lista son", (squares))
print("\n")

# Numeros pares con el rango 

even_number_0_100_range = list(range(0,101,2))
print(even_number_0_100_range)
print("\n")

#Numeros pares utilizando list comprehension
even_list_compre = [value for value in range(0,101) if value%2 == 0]
print(even_list_compre)
print("\n")

# SLICING
player = ["cr7", 'messi', 'tavis', 'chicha', 'corona']
print(player[0:3])

"""
un slicing es trabajar con un grupo especifico de una lista

"""
print(player[1:4])
print(player[:4])
print(player[2:])


print(player[-3:-1])

## slicing en for

players = ["axel", 'ignacio', 'travis', 'chicha', 'corona', 'jorge']

print(player)
first_three_player = player[0:3]
print("first three player: ", first_three_player)
print("\n")
print("Aqui vienen los tres mejores del salon:")

for player in players[0:3]:
     print(player.upper())

# Copia de lista
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
#copy_of_food = my_food #Manera erronea de copiar una lista
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

#Modificacion elementos

cars = ["bwm", "porch", "masda", "totoya", "ford"]

print(cars)


cars[0] = "bmw"
cars[1] = "porshe"
cars[2] = "mazda"
cars[3] = "toyota"

print("\n")
print(cars)
