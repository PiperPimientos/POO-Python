#Asi luce la sintaxis o definicion de una clase

class <nombre_de_la_clase>(<super_clase>): 

    def __init__(self, <params>): #Constructor
        <expression>

    def <nombre_del_metodo>(self, <params>):
        <expression>

#Ejemplo

class Person():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluuda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'

#Uso

>>> david = Persona('David', 35)
>>> erika = Persona('Erika', 32)

>>> david.saluda(erika)
'Hola Erika, me llamo David'

