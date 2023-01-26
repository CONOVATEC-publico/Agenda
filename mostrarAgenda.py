from tkinter import *
from tkinter import ttk


def mostrarAgenda(agenda):
    ventana = Tk()
    ventana.title("Agenda")

    # ventana.geometry("420x260")
    # ventana.minsize(width=275, height=200)
    # ventana.maxsize(width=275, height=200)
    # ventana.resizable(width=0, height=0)

    treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3"))
    treeview.pack(side=LEFT, fill='both')

    treeview.heading("#0", text="Id")
    treeview.heading("col1", text="Nombre")
    treeview.heading("col2", text="Apellido")
    treeview.heading("col3", text="Telefono")

    scrollbar = Scrollbar(ventana, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    treeview.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=treeview.yview)

    for contacto in agenda:
        treeview.insert("", END, text=contacto['id'], values=(contacto['nombre'], contacto['apellido'], contacto['telefono']))

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    ventana.mainloop()
