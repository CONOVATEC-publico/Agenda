from tkinter import *
from tkinter import ttk
from metodos import *


class App:
    def __init__(self, agenda, ventana) -> None:
        self.editId = ""

        self.agenda = agenda
        ventana.geometry("1024x600+50+50")

        self.nombreLabel = Label(ventana, text='Nombre:')
        self.nombreLabel.place(x=20, y=10)

        self.nombreEntry = Entry(ventana)
        self.nombreEntry.place(x=100, y=10)

        self.apellidoLabel = Label(ventana, text='Apellido:')
        self.apellidoLabel.place(x=20, y=40)

        self.apellidoEntry = Entry(ventana)
        self.apellidoEntry.place(x=100, y=40)

        self.telefonoLabel = Label(ventana, text='Telefono:')
        self.telefonoLabel.place(x=20, y=70)

        self.telefonoEntry = Entry(ventana)
        self.telefonoEntry.place(x=100, y=70)

        self.agregarButton = Button(ventana, text="Agregar")
        self.agregarButton[COMMAND] = self.agregarContactoAgenda
        self.agregarButton.place(x=230, y=65, width=70)

        self.guardarButton = Button(ventana, text="Guardar")
        self.guardarButton[COMMAND] = self.guardarContactoAgenda

        self.cancelarButton = Button(ventana, text="Cancelar")
        self.cancelarButton[COMMAND] = self.cancelarGuardar

        self.eliminarButton = Button(ventana, text="Eliminar")
        self.eliminarButton[COMMAND] = self.eliminarContactoAgenda
        self.eliminarButton.place(x=20, y=400)

        self.modificarButton = Button(ventana, text="Modificar")
        self.modificarButton[COMMAND] = lambda: self.treeview_doubleclic(None)
        self.modificarButton.place(x=100, y=400)

        self.treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3"), selectmode="browse")
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("col1", text="Nombre")
        self.treeview.heading("col2", text="Apellido")
        self.treeview.heading("col3", text="Telefono")
        self.treeview.bind('<Double-1>', self.treeview_doubleclic)
        self.treeview.place(x=10, y=100, width=900, height=300)

        self.scrollbar = Scrollbar(self.treeview, orient=VERTICAL)
        self.scrollbar.config(command=self.treeview.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        self.rellenaTreeview()

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        ventana.mainloop()

    def eliminarContactoAgenda(self):
        selection = self.treeview.selection()

        if len(selection) > 0:
            id = selection[0]
            index = self.treeview.item(id, "text")
            eliminarContacto(index, self.agenda)
            self.rellenaTreeview()

    def rellenaTreeview(self):
        self.treeview.delete(*self.treeview.get_children())
        for contacto in self.agenda:
            self.treeview.insert("",
                                 END,
                                 text=contacto['id'],
                                 values=(contacto['nombre'],
                                         contacto['apellido'],
                                         contacto['telefono']))

    def agregarContactoAgenda(self):
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

        agregar(self.agenda, nombre, apellido, telefono)
        self.rellenaTreeview()

        self.limpiarEntrys()
        self.nombreEntry.focus()

    def treeview_doubleclic(self, event):
        selection = self.treeview.selection()
        self.limpiarEntrys()

        if len(selection) > 0:
            self.editId = selection[0]
            contacto = self.treeview.item(self.editId, "values")

            self.nombreEntry.insert(0, contacto[0])
            self.apellidoEntry.insert(0, contacto[1])
            self.telefonoEntry.insert(0, contacto[2])

            self.nombreEntry.focus()

            self.guardarButton.place(x=230, y=65, width=70)
            self.cancelarButton.place(x=310, y=65, width=70)

    def cancelarGuardar(self):
        self.nombreEntry.focus()
        self.guardarButton.place_forget()
        self.cancelarButton.place_forget()
        self.limpiarEntrys()
        self.editId = ""

    def guardarContactoAgenda(self):
        if self.editId != "":
            index = self.treeview.item(self.editId, "text")

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
                
            modificarContacto(self.agenda, int(index), nombre, apellido, telefono)
            self.rellenaTreeview()

        self.nombreEntry.focus()
        self.guardarButton.place_forget()
        self.cancelarButton.place_forget()
        self.limpiarEntrys()

    def limpiarEntrys(self):
        self.nombreEntry.delete(0, END)
        self.apellidoEntry.delete(0, END)
        self.telefonoEntry.delete(0, END)
