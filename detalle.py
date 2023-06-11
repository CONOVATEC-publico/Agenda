import tkinter as tk
from tkinter import messagebox


class DetalleVista:
    def __init__(self, parent, contacto):

        # https://stackoverflow.com/q/16803686  How do I handle the window close event in Tkinter?
        self.root = tk.Toplevel(parent)
        self.root.wait_visibility()
        self.root.grab_set()
        self.root.transient(parent)

        self.root.title("Ver detalle")
        self.root.geometry("335x200+350+250")
        self.root.resizable(width=False, height=False)

        self.contacto = contacto

        self.detalleLabel = tk.Label(self.root)
        self.detalleLabel["text"] = " "
        self.detalleLabel.place(x=100, y=10, width=50, height=25)

        self.nombreLabel = tk.Label(self.root)
        self.nombreLabel["text"] = "Nombre:"
        self.nombreLabel.place(x=30, y=40, width=70, height=25)

        self.apellidoLabel = tk.Label(self.root)
        self.apellidoLabel["text"] = "Apellido:"
        self.apellidoLabel.place(x=30, y=70, width=70, height=25)

        self.telefonoLabel = tk.Label(self.root)
        self.telefonoLabel["text"] = "Teléfono:"
        self.telefonoLabel.place(x=30, y=100, width=70, height=25)

        self.nombreEntry = tk.Entry(self.root)
        self.nombreEntry["text"] = ""
        self.nombreEntry.place(x=100, y=40, width=200, height=25)

        self.apellidoEntry = tk.Entry(self.root)
        self.apellidoEntry["text"] = ""
        self.apellidoEntry.place(x=100, y=70, width=200, height=25)

        self.telefonoEntry = tk.Entry(self.root)
        self.telefonoEntry["text"] = ""
        self.telefonoEntry.place(x=100, y=100, width=200, height=25)

        self.regresarButton = tk.Button(self.root)
        self.regresarButton["text"] = "Regresar"
        self.regresarButton.place(x=40, y=150, width=70, height=25)
        self.regresarButton["command"] = self.RegresarButton_command

        self.guardarButton = tk.Button(self.root)
        self.guardarButton["text"] = "Guardar"
        self.guardarButton.place(x=230, y=150, width=70, height=25)
        self.guardarButton["command"] = self.guardarButton_command

        self.nombreEntry.insert(0, self.contacto[0])
        self.apellidoEntry.insert(0, self.contacto[1])
        self.telefonoEntry.insert(0, self.contacto[2])

        self.root.protocol("WM_DELETE_WINDOW", self.RegresarButton_command)

        self.nombreEntry.focus()

    def RegresarButton_command(self):
        nuevoNombre = self.nombreEntry.get().strip()
        nuevoApellido = self.apellidoEntry.get().strip()
        nuevoTelefono = self.telefonoEntry.get().strip()

        if (nuevoNombre != self.contacto[0]
                or nuevoApellido != self.contacto[1]
                or nuevoTelefono != self.contacto[2]):

            msg_box = messagebox.askquestion('No se guardaron los cambios',
                                             'No has guardado los cambios, ¿seguro que quieres regresar sin guardar?',
                                             icon='warning')
        else:
            msg_box = 'yes'

        if msg_box == 'yes':
            self._salir()

    def guardarButton_command(self):
        nombre = self.nombreEntry.get().strip()
        if nombre == '':
            self.nombreEntry.focus()
            return

        apellido = self.apellidoEntry.get().strip()
        if apellido == '':
            self.apellidoEntry.focus()
            return

        telefono = self.telefonoEntry.get().strip()
        if telefono == '':
            self.telefonoEntry.focus()
            return

        self.contacto = [nombre, apellido, telefono]
        self._salir()

    def _salir(self):
        self.root.grab_release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = DetalleVista(root, ["nombre", "apellido", "telefono"])
    root.mainloop()
