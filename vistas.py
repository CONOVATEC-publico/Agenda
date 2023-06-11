from tkinter import *
from tkinter import ttk
from metodos import *
from detalle import *
from agregar import AgregarVista
from eliminar import EliminarVista


class App:
    def __init__(self, agenda, ventana) -> None:
        self.editId = ""
        self.ventana = ventana
        self.agenda = agenda

        ventana.geometry("925x538+50+50")

        self.agregarButton = Button(ventana, text="Agregar")
        self.agregarButton[COMMAND] = self.AgregarContacto
        self.agregarButton.place(x=825, y=400, width=70)

        self.eliminarButton = Button(ventana, text="Eliminar")
        self.eliminarButton[COMMAND] = self.eliminarContactoAgenda
        self.eliminarButton.place(x=10, y=400)

        self.detalleButton = Button(ventana, text="Ver detalle")
        self.detalleButton[COMMAND] = self.verDetalleContacto
        self.detalleButton.place(x=825, y=35, width=70)

        self.treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3"), selectmode="browse")
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("col1", text="Nombre")
        self.treeview.heading("col2", text="Apellido")
        self.treeview.heading("col3", text="Teléfono")
        self.treeview.bind('<Double-1>', self.treeview_doubleclic)
        self.treeview.place(x=10, y=70, width=900, height=320)

        self.scrollbar = Scrollbar(self.treeview, orient=VERTICAL)
        self.scrollbar.config(command=self.treeview.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        # FILTROS
        self.filtrarLabel = Label(ventana, text='Filtrar por:')
        self.filtrarLabel.place(x=135, y=435)

        self.idFiltrarLabel = Label(ventana, text='ID:')
        self.idFiltrarLabel.place(x=170, y=460)

        self.idFiltrarEntry = Entry(ventana)
        self.idFiltrarEntry.place(x=193, y=460)

        self.nombreFiltrarLabel = Label(ventana, text='Nombre:')
        self.nombreFiltrarLabel.place(x=325, y=460)

        self.nombreFiltrarEntry = Entry(ventana)
        self.nombreFiltrarEntry.place(x=378, y=430+30)

        self.telefonoFiltrarLabel = Label(ventana, text='Telefono:')
        self.telefonoFiltrarLabel.place(x=510, y=460)

        self.telefonoFiltrarEntry = Entry(ventana)
        self.telefonoFiltrarEntry.place(x=565, y=460)

        self.agregarFiltrarButton = Button(ventana, text="Aplicar filtros")
        self.agregarFiltrarButton[COMMAND] = self.filtrarContactos
        self.agregarFiltrarButton.place(x=695, y=455, width=90)

        self.agregarFiltrarButton = Button(ventana, text="Limpiar filtros")
        self.agregarFiltrarButton[COMMAND] = self.limpiarFiltros
        self.agregarFiltrarButton.place(x=695, y=485, width=90)

        self.rellenaTreeview()

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        ventana.mainloop()

    def eliminarContactoAgenda(self):

        selection = self.treeview.selection()

        if len(selection) > 0:
            id = selection[0]
            contacto = self.treeview.item(id, "values")

            eliminarVista = EliminarVista(self.ventana, contacto)
            self.ventana.wait_window(eliminarVista.root)   # <<< NOTE

            contactoEditado = eliminarVista.contacto

            if (contacto[0] != contactoEditado[0]
                    or contacto[1] != contactoEditado[1]
                    or contacto[2] != contactoEditado[2]):

                index = self.treeview.item(id, "text")

                eliminarContacto(index, self.agenda)
                self.rellenaTreeview()

    def rellenaTreeview(self, idFiltro='', nombreFiltro='', telefonoFiltro=''):
        self.treeview.delete(*self.treeview.get_children())
        for contacto in self.agenda:
            agrega = True

            if idFiltro != '':
                if not idFiltro in str(contacto['id']):
                    agrega = False

            if nombreFiltro != '':
                if not nombreFiltro.lower() in contacto['nombre'].lower():
                    agrega = False

            if telefonoFiltro != '':
                if not telefonoFiltro.lower() in contacto['telefono'].lower():
                    agrega = False

            if agrega:
                self.treeview.insert("",
                                     END,
                                     text=contacto['id'],
                                     values=(contacto['nombre'],
                                             contacto['apellido'],
                                             contacto['telefono']))

    def treeview_doubleclic(self, event):
        self.verDetalleContacto()

    def verDetalleContacto(self):
        selection = self.treeview.selection()

        if len(selection) > 0:
            id = selection[0]
            contacto = self.treeview.item(id, "values")

            detalleVista = DetalleVista(self.ventana, contacto)
            self.ventana.wait_window(detalleVista.root)   # <<< NOTE

            contactoEditado = detalleVista.contacto

            if (contacto[0] != contactoEditado[0]
                    or contacto[1] != contactoEditado[1]
                    or contacto[2] != contactoEditado[2]):

                index = self.treeview.item(id, "text")

                modificarContacto(self.agenda, int(index),
                                  contactoEditado[0], contactoEditado[1], contactoEditado[2])
                self.rellenaTreeview()

    def filtrarContactos(self):
        id = self.idFiltrarEntry.get().strip()
        nombre = self.nombreFiltrarEntry.get().strip()
        telefono = self.telefonoFiltrarEntry.get().strip()

        self.rellenaTreeview(id, nombre, telefono)

    def limpiarFiltros(self):
        self.idFiltrarEntry.delete(0, END)
        self.nombreFiltrarEntry.delete(0, END)
        self.telefonoFiltrarEntry.delete(0, END)

        self.rellenaTreeview()

    def AgregarContacto(self):
        agregarVista = AgregarVista(self.ventana)
        self.ventana.wait_window(agregarVista.root)   # <<< NOTE

        contactoAgregado = agregarVista.contacto

        if (contactoAgregado[0] != ''
                or contactoAgregado[1] != ''
                or contactoAgregado[2]) != '':

            agregar(self.agenda, contactoAgregado[0],
                    contactoAgregado[1], contactoAgregado[2])
            self.rellenaTreeview()
