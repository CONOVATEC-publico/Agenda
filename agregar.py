import tkinter as tk
from tkinter import messagebox, ttk
import re 
agenda=[]

dicPaises= {
    "+51":"Perú", 
    "+57":"Colombia",
    "+54": "Argentina",
    "+55": "Brasil"
}

codigoPaises = list(dicPaises.keys())
def seleccionPais(event):
    paisSeleccionado = f' País : {dicPaises[cboCodigoPostal.get()]}\n Código Postal : {cboCodigoPostal.get()} '
    messagebox.showinfo(
        title="País seleccionado",
        message= paisSeleccionado
    )
def mensajeError(campo,mensaje): 
    messagebox.showinfo(f"Error campo {campo}",f"El campo {campo} debe contener solo {mensaje}")

def validacionCampos():
    nombreValidado=re.findall("[a-záéíóúñ]{1,}", nomb.get().strip().lower())
    apellidoValidado= re.findall("[a-záéíóúñ]{1,}", apellido.get().strip().lower())
    telefonoValidado= re.findall("[9][0-9]{8}", telefono.get().strip().lower())

    if not nombreValidado:
        mensajeError("nombre","letras\n debe contener al menos 1 letra.")
        return False
    elif not apellidoValidado:
        mensajeError("apellido","letras\n debe contener al menos 1 letra.")
        return False
    elif not telefonoValidado:
        mensajeError("telefono","números\nEl primer digito del telefono debe ser 9\nAsi mismo,el telefono debe contener 9 dígitos.")
        return False
    else:
        return True

def mensajeConfirmacion():
    messagebox.showinfo("Confirmación", "Se guardo correctamente")
    nomb.delete(0 ,'end')
    apellido.delete(0 ,'end')
    telefono.delete(0 ,'end')
    nomb.focus()

def guardarContacto():
    if validacionCampos():
        iterador = 1 if len(agenda)==0 else len(agenda)+1
        telefonoCodigo= cboCodigoPostal.get()+telefono.get()
        contacto={"id": iterador , 'nombre': nomb.get(),'apellido':apellido.get(), 'telefono': telefonoCodigo }
        agenda.append( contacto)
        print(agenda)
        mensajeConfirmacion()
        

ventan=tk.Tk()
ventan.title("Agenda")
ventan.geometry("400x200")

lblNombre= tk.Label(text="Ingrese nombre")
lblNombre.grid(column=0, row=0)
nomb=tk.Entry(ventan, width=20)
nomb.grid(column=1, row=0)

lblApellido= tk.Label(text="Ingrese apellido")
lblApellido.grid(column=0, row=1)
apellido=tk.Entry(ventan, width=20)
apellido.grid(column=1, row=1)

lblTelefono= tk.Label(text="Ingrese telefono")
lblTelefono.grid(column=0, row=2)
cboCodigoPostal= ttk.Combobox(ventan, width="5", values= codigoPaises, state="readonly")
cboCodigoPostal.current(0)
cboCodigoPostal.bind("<<ComboboxSelected>>", seleccionPais)
cboCodigoPostal.grid(column=1, row=2)
telefono=tk.Entry(ventan, width=10)
telefono.grid(column=2, row=2)

btnGuardarContacto= tk.Button(ventan, text="Guardar",
 command=guardarContacto)
btnGuardarContacto.grid(column=0, row=3)


ventan.mainloop() 