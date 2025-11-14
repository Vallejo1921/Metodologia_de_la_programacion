













# Condicional False
car = "Audi"
print(car == 'audi')

# Posible solución a entradas del usuario usando .lower()
car = "Audi"
print(car.lower() == 'audi') # True

# Operador relacional != para determinar desigualdad
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # True
    print("Hold the anchovies")

# Comparaciones numéricas

age = 18 # Entero
print(age == 18)  # True    

anwer = 17
if anwer != 42:  # True
    print("That is not the correct answer. Please try again!")
    

age = 17
print(age < 21)  # True
print(age <= 21) # True    
print(age > 21)  # False
print(age >= 21) # False

# Multiples condiciones
age_0 = 22
age_1 = 18
print( age_0 >= 21 and age_1 >= 21 ) # False
print( age_0 >= 21 or age_1 >= 21 )  # True
# operacion or
age_0 = 22
age_1 = 18
print( age_0 >= 21 or age_1 >= 21 )  # True
print( age_0 >= 21 or age_1 < 18 )   # False
# operacion and
age_0 = 22

age_1 = 18

print( age_0 >= 21 and age_1 >= 21 ) # False
print( age_0 >= 21 and age_1 < 18 )  # True

"""
para pregunarnos si un valor especifico
esta en una lista, podemos utilizar el siguiente comparardor:

value in list
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
moto_charly_wants = "italica"
print(moto_charly_wants in motorcycles)  # False
print("honda" in motorcycles)              # True
print("ducati" not in motorcycles)         # True

"""
para pregunarnos si un valor especifico
no esta en una lista, podemos utilizar el siguiente comparardor:
value not in list

"""
banned_students = ['jorge', 'carlos', 'moyra', 'gus', 'hots']
user = "mauro"
print(user not in banned_students)  # True
print("jorge" not in banned_students)  # False

## Validación del tipo booleano
game_active = True
can_edit = False


"""
if statement 

sintax:
if condition:
    # código a ejecutar si la condición es verdadera
     do something

if condition:
    # código a ejecutar si la condición es falsa
     do something else

if condition:
    do something
else:
    do something 


"""

age = input("\n Please enter your age: ")
print(age)


if int(age) >= 18:
    print("You are old enough to vote!")
    
else:
    print("You are not old enough to vote yet.")

    