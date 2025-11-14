"""
la Formula de un looping es:
    for "Interable" 

    Accion a realizar
    

"""

# Ejemplo 1: Iterar sobre una lista

magicians = ["ron", "harry", "snape", "hermione", "draco"]


for magician in magicians:
    print(magician)
    print(magician.upper())
    print(magician.swapcase())
    print(f"{magician.title()} Ese es un gran hechizo!.")
    print("\n")

print("Gracias a todos por participar en el show de magia!")


"""
   Identacion.
    python usa la identacion para definir bloques de codigo.
    basicamente se utilizan 4 espacios  en blanco para obligarlos a escribir codigo
    ordenado y estructurado.
    
    """

# no olvidemos identar (donde se necesita)
# ejemplo

magicians = ["alice", "david", "jorge"]
for magician in magicians:
#print(magician) # error de identacion
    print(magician) #solucion

# identacion error
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
#print(f"great {magician}!, i can't wait to see your next trick.") # error de identacion
    print(f"great {magician}!, i can't wait to see your next trick.") # solucion    
    
#identacion innecesaria
message = "hola charly"
    #print(message) # error de identacion
print(message) # solucion
 
"""
 la identacion solo es necesaria dentro de los bloques de codigo como por ejemplo los loops
  y los condicionales ademas de las funciones
 
 """

#logical error
magicians = ["alice", "david", "jorge"]
for magician in magicians:
    print(magician)
    print(f"great {magician}!, i can't wait to see your next trick.")
    #print("thank you everyone, that was a great magic show!") error logico
print("thank you everyone, that was a great magic show!") # solucion

#Error de sintaxis
magicians = ["alice", "david", "jorge"]
for magician in magicians: #un error de sintaxis es olvidar los dos puntos
    print(magician)
    print(f"great {magician}!, i can't wait to see your next trick.")





