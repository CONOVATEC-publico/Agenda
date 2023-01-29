from tkinter import *
from tkinter import ttk
from metodos import *


def mostrarAgenda(agenda, ventana: Tk):
    ventana.geometry("1024x600+100+100")
    
    idLabel = Label(ventana, text='Id:')
    idLabel.place(x=20, y=20)

    idEntry = Entry(ventana)
    idEntry.place(x=40, y=20)

    agregarButton = Button(ventana, text="Agregar")
    agregarButton.place(x=20, y=70)

    eliminarButton = Button(ventana, text="Eliminar",
                            command=lambda: eliminarContactoAgenda(treeview, agenda))
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
        treeview.insert("", END, text=contacto['id'], values=(
            contacto['nombre'], contacto['apellido'], contacto['telefono']))
