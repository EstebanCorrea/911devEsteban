
Nombre1 = 'Valentina'
PI = 3.14159

print()

"""
Ejercicio 2: Operaciones básicas
Declara dos variables numéricas y realiza las operaciones de suma, resta, multiplicación y división.
Imprime el resultado de cada operación.
"""

valor1 = 5
valor2 = 97

suma = valor1 + valor2
resta = valor1 -valor2
multiplicacion = valor1 * valor2
division= valor1/valor2

print("La suma de estos valores es: " + str(suma)) 
print("La resta de estos valores es: " + str(resta)) 
print("La multiplicacion de estos valores es: " + str(multiplicacion)) 
print("La division de estos valores es: " + str(division)) 
print()
""" 
Ejercicio 3: Listas
Crea una lista con los números del 1 al 5 y luego agrega el número 6 al final de la lista.
"""

Numeros = [1,2,3,4,5]
ListaCompleta = Numeros + [6]

print("La lista es: " + str(ListaCompleta))
print()
"""
Ejercicio 4: Diccionarios
Crea un diccionario con tres elementos: 'nombre', 'edad' y 'ciudad'. Luego, imprime el valor de 'nombre'.
"""
Elementos = {
    'Nombre' : 'Valentina Correa',
    'Edad' : 22,
    'Ciudad' : 'Medellín'
}

print("Mi nombre es " + Elementos['Nombre'])
print()


"""
Ejercicio 5: Condicionales
Escribe un condicional que imprima "Mayor de edad" si la edad es mayor o igual a 18, y "Menor de edad" en caso contrario.
"""
if Elementos['Edad'] >= 18:
    print("Es mayor de edad")
    print()
else:
    print("Es menor de edad")

    print()

"""
Ejercicio 6: Bucles
Escribe un bucle que imprima los números del 1 al 10.
"""

for numeros in range(1,11):
    print(numeros)
    

"""     Investiga sobre los paradigmas de programación . trae como mínimo 3 
ejemplos de paradigmas de programación y explica en qué consisten. 
(Pueden hacer ejemplos con código) aplicados a python. """

""" Paradigma Imperativo (Ejemplo: Python, C, JavaScript)

Se basa en dar órdenes secuenciales al computador, modificando el estado del programa paso a paso. """
print()
x = 5
y = 3
resultado = x + y
print(resultado)  # Imprime 8

""" Paradigma Orientado a Objetos (OOP) (Ejemplo: Python, Java, C++)

Organiza el código en clases y objetos que tienen atributos (datos) y métodos (acciones). """

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"

p = Persona("Valentina")
print(p.saludar())  # Imprime "Hola, mi nombre es Valentina"

""" Paradigma Funcional 

Usa funciones como bloques fundamentales, evitando modificar variables y usando recursión en lugar de bucles.
"""
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)  # Imprime 8