""" Ejercicio 1: Variables y constantes
    Declara una variable llamada 'nombre' y asígnale tu nombre.
    Declara una constante llamada 'PI' y asígnale el valor de 3.14159."""
nombre = "Esteban"
PI = 3.14159265358979
"""
    Ejercicio 2: Operaciones básicas
    Declara dos variables numéricas y realiza las operaciones de suma, resta, multiplicación y división.
Imprime el resultado de cada operación.
"""
valorUno = 45
ValorDos = 82
suma = valorUno + ValorDos
resta = valorUno - ValorDos
multipl = valorUno * ValorDos
div = valorUno / ValorDos
print(f"El resultado de la suma es: {suma}, resta: {resta}, multiplicación: {multipl}, y división: {div}")

"""
    Ejercicio 3: Listas
    Crea una lista con los números del 1 al 5 y luego agrega el número 6 al final de la lista.
"""
ejemlist = [1,2,3,4,5]
ejemlist.append(6)
print(ejemlist)

"""
    Ejercicio 4: Diccionarios
    Crea un diccionario con tres elementos: 'nombre', 'edad' y 'ciudad'. Luego, imprime el valor de 'nombre'.
"""
dicpersona = {
    "nombre" : "Esteban",
    "edad":"24",
    "ciudad":"Medellin"
}
print(dicpersona["nombre"])

"""
    Ejercicio 5: Condicionales
    Escribe un condicional que imprima "Mayor de edad" si la edad es mayor o igual a 18, y "Menor de edad" en caso contrario.
"""
edad = int(input("Digite su edad: "))
if(edad<18):
    print("Mayor de edad")
else:
    print("Menor de edad")


"""     Ejercicio 6: Bucles
        Escribe un bucle que imprima los números del 1 al 10.
"""
for c in range(1,11):
    print(c)

"""
    Un paradigma de programación es un estilo o enfoque para escribir y
    organizar código en un lenguaje de programación. Define la forma en que l
    os programadores estructuran y solucionan problemas mediante la lógica del código.
"""
#Ejemplo1: Paradigma Orientado a objetos
#Se basa en el uso de clases y objetos para estructurar el código.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario:.2f}"

# Crear empleados
empleado1 = Empleado("Ana", 50000)
empleado2 = Empleado("Carlos", 60000)

# Aumentar salario y mostrar información
empleado1.aumentar_salario(10)
empleado2.aumentar_salario(5)

print(empleado1.mostrar_info())  # Empleado: Ana, Salario: $55000.00
print(empleado2.mostrar_info()) 

#Ejemplo 2:  Paradigma Funcional - Python
#Se basa en funciones puras, sin modificar variables globales.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

cuadrados = list(map(lambda x: x**2, pares))

print("Números pares:", pares)         # [2, 4, 6, 8, 10]
print("Cuadrados:", cuadrados)   

#Ejemplo 3: Paradigma Declarativo (SQL - Bases de Datos)
#Se basa en expresar qué se quiere hacer en lugar de cómo hacerlo.

""" SQL ejemplo
SELECT nombre, salario
FROM empleados
WHERE salario > 50000
ORDER BY salario DESC;
"""