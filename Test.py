# importando metodos
from tkinter import *
from tkinter import ttk
from vistas import App # mostrarAgenda
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
agenda = []
contacto = {'id': '0', 'nombre': 'Juan',
            'apellido': 'Perez', 'telefono': '956123456'}
agenda.append(contacto)

for x in range(1, 5+1):
    agregar(agenda, 'nombre' + str(x), 'apellido' +
            str(x), 'telefono' + str(x))

# print(agenda)
ventana = Tk()
ventana.title("Agenda Telefónica")
detalleVista = App(agenda, ventana)
# agregarVista = App(agenda, ventana) # No se observan cambios en la presentación de la agenda telefónica.