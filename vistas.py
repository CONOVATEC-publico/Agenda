from tkinter import *
from tkinter import ttk
from metodos import *


def mostrarAgenda(agenda, ventana: Tk):
    ventana.geometry("1024x600+50+50")

    nombreLabel = Label(ventana, text='Nombre:')
    nombreLabel.place(x=20, y=10)

    nombreEntry = Entry(ventana)
    nombreEntry.place(x=100, y=10)

    apellidoLabel = Label(ventana, text='Apellido:')
    apellidoLabel.place(x=20, y=40)

    apellidoEntry = Entry(ventana)
    apellidoEntry.place(x=100, y=40)

    telefonoLabel = Label(ventana, text='Telefono:')
    telefonoLabel.place(x=20, y=70)

    telefonoEntry = Entry(ventana)
    telefonoEntry.place(x=100, y=70)

    agregarButton = Button(ventana, text="Agregar")
    agregarButton[COMMAND] = lambda: agregarContactoAgenda(
        nombreEntry.get(), apellidoEntry.get(), telefonoEntry.get(), treeview, agenda)
    agregarButton.place(x=230, y=65, width=70)

    eliminarButton = Button(ventana, text="Eliminar")
    eliminarButton[COMMAND] = lambda: eliminarContactoAgenda(treeview, agenda)
    eliminarButton.place(x=20, y=400)

    treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3"))
    treeview.heading("#0", text="Id")
    treeview.heading("col1", text="Nombre")
    treeview.heading("col2", text="Apellido")
    treeview.heading("col3", text="Telefono")
    treeview.place(x=10, y=100, width=900, height=300)

    scrollbar = Scrollbar(treeview, orient=VERTICAL)
    scrollbar.config(command=treeview.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    treeview.config(yscrollcommand=scrollbar.set)

    rellenaTreeview(treeview, agenda)

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    ventana.mainloop()


def eliminarContactoAgenda(treeview: ttk.Treeview, agenda):
    item = treeview.item(treeview.focus())
    if item["text"] != '':
        eliminarContacto(item["text"], agenda)
        rellenaTreeview(treeview, agenda)


def rellenaTreeview(treeview: ttk.Treeview, agenda):
    treeview.delete(*treeview.get_children())
    for contacto in agenda:
        treeview.insert("",
                        END,
                        text=contacto['id'],
                        values=(contacto['nombre'],
                                contacto['apellido'],
                                contacto['telefono']))


def agregarContactoAgenda(nombre, apellido, telefono, treeview: ttk.Treeview, agenda):
    agregar(agenda, nombre, apellido, telefono)
    rellenaTreeview(treeview, agenda)
