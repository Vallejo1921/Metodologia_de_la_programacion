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

"""
#syntax error con strings

"""


message = "Una fortaleza de 'Python' es su comunidad"

#concatenacion con f-strings

famous_person = "charly mercury"

quote = "python is love"

message = famous_person +" una vez dijo "+ quote

print(message)

#concatenacion con fstrings

"""

"""

message_f_string = f"{famous_person} una vez dijo {quote}"

print(message_f_string)

#Actividad
"""
   1) elije un personaje famoso e igualalo a una variable
   del tipo string

   2) Elije una frase famosa que haya dicho e iguala a una varieble del tipo string

   3) Genera un mensaje con las dos variables utilizando f-string

   4) imprime el mensaje

"""

###whitespace

"""
whitespaces se refiere a cualquier caracter que no se imprime,
es decir, un tabulador y finales de lineas, los whitespaces
se utilizan comunmente para organizar las salidas (prints)
de tal manera que sea mmas amigable de leer o para los usuarios

"""

##Ejemplos

print("Python")
print("\tPython")
print("\t\tPython")

print("Yo: \n vavavava \n si \n fuaaa")