import tkinter as tk
from metodos import *
from vistas import *


class EliminarVista:
    def __init__(self, parent, contacto):
        # --------------Ventana Eliminar-----------------
        self.root = tk.Toplevel(parent)
        self.root.wait_visibility()
        self.root.grab_set()
        self.root.transient(parent)
        #self.root.configure(background='mint cream')

        self.root.title("                                      Eliminar                         ")
        self.root.geometry("335x120+350+250")
        self.root.resizable(width=False, height=False)
        # -----------------------------------------------
        self.contacto = contacto

        self.nombreEntry_EV = tk.Entry(self.root)
        self.nombreEntry_EV["text"] = " "

        self.apellidoEntry_EV = tk.Entry(self.root)
        self.apellidoEntry_EV["text"] = " "

        self.telefonoEntry_EV = tk.Entry(self.root)
        self.telefonoEntry_EV["text"] = " "

        self.nombreEntry_EV.insert(0, self.contacto[0])
        self.apellidoEntry_EV.insert(0, self.contacto[1])
        self.telefonoEntry_EV.insert(0, self.contacto[2])

        # -------Etiquetas de la ventana eliminar--------
        self.mensajeLabel1 = tk.Label(self.root)
        self.mensajeLabel1["text"] = "¿Está seguro que quiere eliminar este contacto"
        self.mensajeLabel1.place(x=40, y=10, width=250, height=25)

        self.mensajeLabel2 = tk.Label(self.root)
        self.mensajeLabel2["text"] = "de su agenda telefónica?"
        self.mensajeLabel2.place(x=40, y=30, width=250, height=25)

        # --------------------Botones--------------------
        self.Button_SI = tk.Button(self.root)
        self.Button_SI["text"] = "Si"
        self.Button_SI.place(x=80, y=70, width=30, height=25)
        self.Button_SI["command"] = self.Button_SI_command

        self.Button_NO = tk.Button(self.root)
        self.Button_NO["text"] = "No"
        self.Button_NO.place(x=225, y=70, width=30, height=25)
        self.Button_NO["command"] = self.Button_NO_command

        self.root.protocol("WM_DELETE_WINDOW", self.Button_NO_command)
        self.Button_SI.focus()

    def _salirVentana(self):
        self.root.grab_release()
        self.root.destroy()

    def Button_NO_command(self):
        self._salirVentana()

    def Button_SI_command(self):
        # print("¡La clase EliminarVista cumple con su función de manera satisfactoria!")
        self.contacto = [self.nombreEntry_EV.get().strip(),
                         self.apellidoEntry_EV.get().strip(),
                         self.telefonoEntry_EV.get().strip()]
        self._salirVentana()


if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarVista(root, ["nombre", "apellido", "telefono"])
    root.mainloop()
