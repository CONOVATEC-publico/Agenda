# importando metodos

"""

Diseñar un programa que gestione una agenda telefónica con los nombres y los números de contacto de los clientes de una organización. El programa incorporará que presentará el siguiente menú:
Agenda telefónica de ABC SA
==========================
1 - Consultar un número de contacto.
2 - Añadir un número de contacto.
3 - Eliminar un número de contacto.
4 - Crear la agenda.
0 - Terminar. 


"""
# Contacto base
agenda=[]
contacto={'id':'1','nombre': 'Juan','apellido':'Perez', 'telefono': '956123456'}
agenda.append(contacto)

from tkinter import *
from tkinter import ttk
from vistas import mostrarAgenda

contacto = {'id': '2', 'nombre': 'Pedro', 'apellido': 'Ramirez', 'telefono': '965876541'}
agenda.append(contacto)
for x in range(3, 25):
    contacto = {'id': x, 'nombre': 'Pedro' + str(x), 'apellido': 'Ramirez' + str(x), 'telefono': x}
    agenda.append(contacto)

# print(agenda)
ventana = Tk()
ventana.title("Agenda")

mostrarAgenda(agenda, ventana)
