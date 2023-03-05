from tkinter import *
from tkinter import ttk
from metodos import *


class App:
    def __init__(self, agenda, ventana) -> None:    
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

        self.eliminarButton = Button(ventana, text="Eliminar")
        self.eliminarButton[COMMAND] = self.eliminarContactoAgenda
        self.eliminarButton.place(x=20, y=400)

        self.treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3"))
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("col1", text="Nombre")
        self.treeview.heading("col2", text="Apellido")
        self.treeview.heading("col3", text="Telefono")
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
        item = self.treeview.item(self.treeview.focus())
        if item["text"] != '':
            eliminarContacto(item["text"], self.agenda)
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
