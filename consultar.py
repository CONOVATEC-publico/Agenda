import tkinter as tk
from tkinter import messagebox, ttk
import re

agenda=[]
contacto={'id':1,'nombre': 'Juan','apellido':'Perez', 'telefono': '+51956123456'}
contacto1={'id':2,'nombre': 'Juan','apellido':'Perez', 'telefono': '+55946123456'}
contacto2={'id':3,'nombre': 'Ichihiro','apellido':'Gomez', 'telefono': '+56939523456'}
contacto3={'id':4,'nombre': 'Ivan','apellido':'Best', 'telefono': '+56969523456'}
agenda.append(contacto)
agenda.append(contacto1)
agenda.append(contacto2)
agenda.append(contacto3)


dicBusqueda={
    "ID":"1",
    "Nombre":"2",
    "Telefono":"3"
}
tiposBusqueda = list(dicBusqueda.keys())
def mensajeError(campo,mensaje): 
    messagebox.showinfo(f"Error campo {campo}",f"El campo {campo} debe contener solo {mensaje}")

def resultadoContacto(agenda,clave, opcionBuscar):
    for contacto in agenda:
        if(contacto[clave] == int(opcionBuscar)):
            return contacto


def resultadoContactos(agenda,clave, opcionBuscar):
    resultados=[]
    secuencia= f"^{opcionBuscar}"
    for contacto in agenda:
        if(re.findall(secuencia,contacto[clave].lower())):
            resultados.append(contacto)
    return resultados

def listarTabla(lista):
    for contacto in lista:
     tabla.insert("","end", text=contacto["id"] , values=(contacto["nombre"] , contacto["apellido"] ,contacto["telefono"] ))
                    
def limpiarTabla():
    for item in tabla.get_children():
        tabla.delete(item)
ventana1=tk.Tk()
ventana1.title("Agenda")
ventana1.geometry("1000x600")

label= tk.Label(text="Ingrese campo a buscar ")
label.grid(column=0, row=0)

txtBusqueda=tk.Entry(ventana1, width=20)
txtBusqueda.grid(column=0, row=1)

cboOpcionesBusqueda= ttk.Combobox(ventana1, width="10", values= tiposBusqueda, state="readonly")
cboOpcionesBusqueda.current(0)
cboOpcionesBusqueda.grid(column=1, row=1)

def buscar():
     opcion = ""
     opcion = dicBusqueda[cboOpcionesBusqueda.get()]
     clave = cboOpcionesBusqueda.get().lower()
     busqueda = txtBusqueda.get().strip()

     if(opcion=="1"):
       
        valorVerificado = re.findall("[0-9]{1,}", busqueda)
        if(valorVerificado) and int(busqueda)>0:
             contacto=resultadoContacto(agenda,clave, busqueda)
             if contacto:
              limpiarTabla()
              tabla.insert("","end", text=contacto["id"] , values=(contacto["nombre"] , contacto["apellido"] ,contacto["telefono"] ))
             else:
                messagebox.showinfo("Error ","No hay coincidencias")
                limpiarTabla()
        else: 
             mensajeError("busqueda","números y distintos a cero")
            

     if(opcion=="3"):
        valorVerificado = re.findall("[+][0-9]{2}[9][0-9]{8}", busqueda)
        if valorVerificado:
            contacto=resultadoContacto(agenda, clave, busqueda)
            if contacto:
                limpiarTabla()
                tabla.insert("","end", text=contacto["id"] , values=(contacto["nombre"] , contacto["apellido"] ,contacto["telefono"] ))
              
            else:
                messagebox.showinfo("Error ","No hay coincidencias")
                limpiarTabla()
               
        else:
            mensajeError("busqueda","telefonos de 9 digitos comenxando con 9")
       
     if( opcion=="2"):
        valorVerificado = re.findall("[a-záéíóúñ]{1,}", busqueda)
        print(valorVerificado)
        if valorVerificado:
            contactos = resultadoContactos(agenda,clave, busqueda)
            print(contactos)
            if contactos:
                limpiarTabla()
                listarTabla(contactos)
                
            else:
                 messagebox.showinfo("Error ","No hay coincidencias")
                 limpiarTabla()
                  
        else:
             mensajeError("","solo letras sin caracteres extraños")
    
        
boton= tk.Button(ventana1, text="Buscar", command=buscar)
boton.grid(column=3, row=1)
cols= ("col1", "col2","col3")
tabla = ttk.Treeview(ventana1, columns=cols)
tabla.grid(column=0, row=3)
tabla.heading("#0",text="Id")
tabla.heading("col1",text="Nombre")
tabla.heading("col2",text="Apellido")
tabla.heading("col3",text="Telefono")


lab= tk.Label(text="")
lab.grid(column=0, row=3)
ventana1.mainloop()