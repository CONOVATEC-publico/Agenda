import tkinter as tk
from tkinter import messagebox
from metodos import *
#from Test import *

class AgregarVista:
    def __init__(self, parent, enlace):
        self.root = tk.Toplevel(parent)
        self.root.wait_visibility()
        self.root.grab_set()
        self.root.transient(parent)

        self.root.title("Agregar button")
        self.root.geometry("335x200+350+250")
        self.root.resizable(width=False, height=False)

        self.enlace = enlace

        self.nombreLabel_AV = tk.Label(self.root)
        self.nombreLabel_AV["text"] = "Nombre"
        self.nombreLabel_AV.place(x=30, y=10, width=70, height=25)

        self.apellidoLabel_AV = tk.Label(self.root)
        self.apellidoLabel_AV["text"] = "Apellido"
        self.apellidoLabel_AV.place(x=30, y=40, width=70, height=25)

        self.telefonoLabel_AV = tk.Label(self.root)
        self.telefonoLabel_AV["text"] = "Teléfono"
        self.telefonoLabel_AV.place(x=30, y=70, width=70, height=25)

        self.nombreEntry_AV = tk.Entry(self.root)
        self.nombreEntry_AV["text"] = ""
        self.nombreEntry_AV.place(x=100, y=10, width=200, height=25)

        self.apellidoEntry_AV = tk.Entry(self.root)
        self.apellidoEntry_AV["text"] = ""
        self.apellidoEntry_AV.place(x=100, y=40, width=200, height=25)

        self.telefonoEntry_AV = tk.Entry(self.root)
        self.telefonoEntry_AV["text"] = ""
        self.telefonoEntry_AV.place(x=100, y=70, width=200, height=25)

        self.cancelarButton_AV = tk.Button(self.root)
        self.cancelarButton_AV["text"] = "Cancelar"
        self.cancelarButton_AV.place(x=40, y=120, width=70, height=25)
        self.cancelarButton_AV["command"] = self.CancelarButton_command_AV

        self.guardarButton_AV = tk.Button(self.root)
        self.guardarButton_AV["text"] = "Guardar"
        self.guardarButton_AV.place(x=230, y=120, width=70, height=25)
        self.guardarButton_AV["command"] = self.GuardarButton_command_AV

        self.nombreEntry_AV.insert(0, self.enlace[0])
        self.apellidoEntry_AV.insert(0, self.enlace[1])
        self.telefonoEntry_AV.insert(0, self.enlace[2])

        self.root.protocol("WM_DELETE_WINDOW", self.CancelarButton_command_AV)

    def CancelarButton_command_AV(self):
        nuevo_Nombre = self.nombreEntry_AV.get().strip()
        nuevo_Apellido = self.apellidoEntry_AV.get().strip()
        nuevo_Telefono = self.telefonoEntry_AV.get().strip()

        if (nuevo_Nombre != self.enlace[0]
                or nuevo_Apellido != self.enlace[1]
                or nuevo_Telefono != self.enlace[2]):

            msg_box = messagebox.askquestion('No se guardaron los cambios',
                                             '¿Estás seguro que quieres cancelar?',
                                             icon='warning')
        else:
            msg_box = 'yes'

        if msg_box == 'yes':
            self._salir()

    def GuardarButton_command_AV(self):
        self.enlace = [self.nombreEntry_AV.get().strip(),
                         self.apellidoEntry_AV.get().strip(),
                         self.telefonoEntry_AV.get().strip()]
        
        self._salir()

        nombre_AV = self.nombreEntry_AV.get().strip()
        if nombre_AV == '':
            self.nombreEntry_AV.focus()
            return
        
        apellido_AV = self.apellidoEntry_AV.get().strip()
        if apellido_AV == '':
            self.apellidoEntry_AV.focus()
            return
        
        telefono_AV = self.telefonoEntry_AV.get().strip()
        if telefono_AV == '':
            self.telefonoEntry_AV.focus()
            return
        
        agregar(self.agenda, nombre_AV, apellido_AV, telefono_AV)
        self.rellenaTreeview()

    def _salir(self):
        self.root.grab_release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AgregarVista(root, ["nombre", "apellido", "telefono"])
    root.mainloop()
