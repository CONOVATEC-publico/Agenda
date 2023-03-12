# Método para añadir contacto

indice = 1

def agregar(agenda, nombre, apellido, telefono):
    global indice

    # global contacto
    contacto = {
        "id":indice,
        "nombre":nombre,
        "apellido":apellido,
        "telefono":telefono
    }
    indice += 1

    agenda.append(contacto)



# Método para eliminar contacto
def eliminarContacto(id, agenda):
    for contacto in agenda:
        if contacto['id'] == id:
            agenda.remove(contacto)
            return


# Método para editar/modificar un contacto
def modificarContacto(agenda, index, nombre, apellido, telefono):
    contacto = {
        "id":index,
        "nombre":nombre,
        "apellido":apellido,
        "telefono":telefono
    }
    agenda[index] = contacto



# Método para buscar contacto

#pip install phonenumbers en caso que no se pueda importar la librería phonenumbers
import phonenumbers
from phonenumbers import carrier, geocoder

def ExaminarNumero(movil):
    data = []
    numero = phonenumbers.parse(movil)
    data.append(geocoder.description_for_number(numero,"es"))
    data.append(carrier.name_for_number(numero,"es"))
    return data

movil = input("Ingrese un número telefónico: ")
print(ExaminarNumero(movil))


