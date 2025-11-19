













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

"""
try: 
    # código que puede generar una excepción
    do something
 exept:
    # código para manejar la excepción
    handle exception
"""
age = 0

try:
  age = int(input("\n Please enter your age: "))
        
except: 

    print("Invalid input. Please enter a valid age.")
   
    if age > 100:
     print("your have lived a long life!")

    elif age >= 18 and age <= 100:
     print("You are old enough to vote!")

    elif age < 18 and age >= 0:
     print("You are not old enough to vote yet.")
        
    elif age < 0:
        
     print("Invalid age. Age cannot be negative.")

print("hola charly")


"""
Hacer un programa que pregunte la edad de una persona
y responda lo siguiente:
   - si la edad es menor a 4 la entrada es gratis
    - si la edad es entre 4 y 18 el precio es 200 rupias
    - si la edad es mayor a 18 el precio es 400 rupias

"""
#Multiple if
guisos = ["pollo", "res", "vegetariano", "pescado"]
if "pollo" in guisos:
    print("Si hay pollo")
else:
    print("No hay pollo")
if "res" in guisos:
    print("Si hay res")
else:
    print("No hay res")
if "vegetariano" in guisos:
    print("Si hay vegetariano")
else:
    print("No hay vegetariano")
if "pescado" in guisos:
    print("Si hay pescado")
else:
    print("No hay pescado")