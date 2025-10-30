"""
    un string es de manera sencilla una serie de caracteres.
    en python todo lo que este adentro de comillas simples o doble comillas es considerado in string.
    " ''  

    " Esto es un string "
    ' Esto es un string'

    'Le dije a un amigo, "python es mi lenguaje fav"'
    "El lenguaje 'python' lleva el nombre por monty python, no por la serpiente"
    

"""

name = "clase de programadcion"
print(name)
print(name.title())
print(name)

"""
un metodo es una accion que python puede realizar
en un fragmentode datos o sobre una variable

El punto . despues de una variable seguida del metodo title() dice que se tiene que ejecutar 
el metodo title() de la variable name.

Todos los metodos estan seguidos de parentesis por que en ocasiones necesitan informacion adicional para funcionar
en esta ocasion el metodo title() no requiere info adicional.

otro ejemplo seria:

"""
print(name.upper())
print(name.lower())



# concatenacion de STRINGS

print("CONCATENACION DE STRINGS")
first_name = "armando"
last_name = "vallejo"
full_name = first_name +" "+ last_name
print(full_name)


print("Hola, " + full_name.title() + "!")

