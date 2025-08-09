#00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

## https://www.python.org/
## Lenguaje de programacion Python 

"""
 EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

variable = "Python"
GRAVITY = 9.81 #constante


texto= 'Victor'
numero_entero = 2  #int
numero_decimal = 3.0 #float
boleano = True  #boolean
bool2 = False  #boolean
my_other_string = "No tengo casa"
my_string = 'Maduro Dictador'

tuplas = (23, 'yuka', 'aviones',2)
print(tuplas) #--> (23, 'yuka', 'aviones', 2)
print(type(tuplas)) #--> <class 'tuple'>

lista1 = [1, 2, 3, 5] #--> <class 'list'>
print(lista1) #--> [1, 2, 3, 5]
print(type(lista1)) #--> <class 'list'>

sets_1 = {2,3,1} 
print(sets_1) #--> {1, 2, 3}
print(type(sets_1)) #-> <class 'set'>

dictionary = {
    'name' : 'victor',
    'last_name' : 'Hernandez'
}

print(dictionary) #--> {'name': 'victor', 'last_name': 'Hernandez'}
print(type(dictionary)) #--> <class 'dict'>



