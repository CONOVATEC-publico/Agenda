import tkinter as tk
from tkinter import *
from tkinter import ttk
from metodos import *
from detalle import *
from agregar import AgregarVista
from eliminar import EliminarVista
import tkinter # Invocamos esta librería en esta línea para la ventana agregar

class App:
    def __init__(self, agenda, ventana) -> None:
        self.editId = ""
        self.ventana = ventana
        self.agenda = agenda

        ventana.geometry("925x538+50+50") #ventana.geometry("1024x600+50+50")

        #self.nombreLabel = Label(ventana, text='Nombre:')
        #self.nombreLabel.place(x=20, y=10)

        #self.nombreEntry = Entry(ventana)
        #self.nombreEntry.place(x=100, y=10)

        #self.apellidoLabel = Label(ventana, text='Apellido:')
        #self.apellidoLabel.place(x=20, y=40)

        #self.apellidoEntry = Entry(ventana)
        #self.apellidoEntry.place(x=100, y=40)

        #self.telefonoLabel = Label(ventana, text='Teléfono:')
        #self.telefonoLabel.place(x=20, y=70)

        #self.telefonoEntry = Entry(ventana)
        #self.telefonoEntry.place(x=100, y=70)

        self.agregarButton = Button(ventana, text="Agregar")
        self.agregarButton[COMMAND] = self.AgregarContacto
        self.agregarButton.place(x=825, y=400, width=70)

        #self.guardarButton = Button(ventana, text="Guardar")
        #self.guardarButton[COMMAND] = self.guardarContactoAgenda

        self.cancelarButton = Button(ventana, text="Cancelar")
        self.cancelarButton[COMMAND] = self.cancelarGuardar

        self.eliminarButton = Button(ventana, text="Eliminar")
        self.eliminarButton[COMMAND] = self.eliminarContactoAgenda
        self.eliminarButton.place(x=10, y=400)

        #self.modificarButton = Button(ventana, text="Modificar")
        #self.modificarButton[COMMAND] = lambda: self.treeview_doubleclic(None)
        #self.modificarButton.place(x=100, y=400)

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

    def agregarContactoAgenda(self): # A este método se le ha dado de baja.
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
        contacto = self.treeview.item(id, "values")
        self.contacto.delete(0, END)
        
        #self.telefonoEntry.delete(0, END)

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
        selection = self.treeview.selection()

        if len(selection) > 0:
            id = selection[0]
            enlace = self.treeview.item(id, "values")
            
            agregarVista = AgregarVista(self.ventana, enlace)
            self.ventana.wait_window(agregarVista.root)   # <<< NOTE

            contactoAgregado = agregarVista.enlace

            if (enlace[0] != contactoAgregado[0]
                    or enlace[1] != contactoAgregado[1]
                    or enlace[2] != contactoAgregado[2]):

                index = self.treeview.item(id, "text")

                agregar(self.agenda, contactoAgregado[0],
                         contactoAgregado[1], contactoAgregado[2])
                self.rellenaTreeview()
            
        else:
            # ----------------Ventana Agregar-------------------
            ventana_agregar = tkinter.Tk()
            ventana_agregar.attributes('-topmost', True)
            ventana_agregar.attributes('-toolwindow', True)
            ventana_agregar.title("Agregar button")
            ventana_agregar.geometry("335x200+190+250")
            ventana_agregar.resizable(0, 0)
            ventana_agregar.configure(background='mint cream')

            # ---------Etiquetas de la ventana agregar-----------
            nombre_Label = tkinter.Label(ventana_agregar, text="Nombre:", fg='black')
            nombre_Label.pack()
            nombre_Label.place(x=30, y=10, width=70, height=25)

            apellido_Label = tkinter.Label(ventana_agregar, text="Apellido:", fg='black')
            apellido_Label.pack()
            apellido_Label.place(x=30, y=40, width=70, height=25)

            telefono_Label = tkinter.Label(ventana_agregar, text="Teléfono:", fg='black')
            telefono_Label.pack()
            telefono_Label.place(x=30, y=70, width=70, height=25)

            # ----------Entradas de la ventana agregar-----------
            nombre_Entry = tkinter.Entry(ventana_agregar, text="")
            nombre_Entry.pack()
            nombre_Entry.place(x=100, y=10, width=200, height=25)

            apellido_Entry = tkinter.Entry(ventana_agregar, text="")
            apellido_Entry.pack()
            apellido_Entry.place(x=100, y=40, width=200, height=25)

            telefono_Entry = tkinter.Entry(ventana_agregar, text="")
            telefono_Entry.pack()
            telefono_Entry.place(x=100, y=70, width=200, height=25)

            # -------Métodos para los comandos de botones--------
            def CancelarButton_command():
                msg_box = messagebox.askquestion('No se guardaron los cambios',
                                             '¿Estás seguro que quieres cancelar?',
                                             icon='warning')
                
                if msg_box == 'yes':
                    _salir_VA()
                        
            def GuardarButton_command():
                contacto = [nombre_Entry.get().strip(),
                         apellido_Entry.get().strip(),
                         telefono_Entry.get().strip()]
                
                agregar(self.agenda, contacto[0],
                         contacto[1], contacto[2])
                self.rellenaTreeview()
                
                _salir_VA()
            
            def _salir_VA():
                ventana_agregar.grab_release()
                ventana_agregar.destroy()

            # ----------------------Botones----------------------
            cancelarButton = tkinter.Button(ventana_agregar, text="Cancelar",
                                             command=CancelarButton_command)
            cancelarButton.pack()
            cancelarButton.place(x=40, y=120, height=25, width=70)

            guardarButton = tkinter.Button(ventana_agregar, text="Guardar",
                                             command=GuardarButton_command)
            guardarButton.pack()
            guardarButton.place(x=230, y=120, width=70, height=25)

            nombre_Entry.insert(0, enlace[0])
            apellido_Entry.insert(0, enlace[1])
            telefono_Entry.insert(0, enlace[2])
        
            ventana_agregar.protocol("WM_DELETE_WINDOW", CancelarButton_command())
            ventana_agregar.mainloop()