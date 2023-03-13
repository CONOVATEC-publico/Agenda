# importando metodos
from tkinter import *
from tkinter import ttk
from vistas import App #mostrarAgenda
from metodos import agregar
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
contacto={'id': 1,'nombre': 'Juan','apellido':'Perez', 'telefono': '956123456'}
agenda.append(contacto)
# print(agenda)


contacto = {'id': 2,'nombre': 'Pedro','apellido':'Ramirez', 'telefono': '965876541'}
agenda.append(contacto)
for x in range(3,7):
    contacto = {'id': x,'nombre': 'Miguel_' + str(x),'apellido':'Grau_' + str(x), 'telefono': x+925059890}
    agenda.append(contacto)

# print(agenda)
ventana = Tk()
ventana.title("Agenda Telefónica")

agregar(agenda,"Carl F.","Gauss","988888821")

App(agenda, ventana) #mostrarAgenda(agenda, ventana)