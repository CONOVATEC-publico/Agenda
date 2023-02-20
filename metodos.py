# Método para añadir contacto

<<<<<<< HEAD
#=======
indice=1
=======
indice=1

def agregar(agenda, nombre, apellido, telefono):
    global indice
    
    #global contacto
    contacto = {
        "id":indice,
        "nombre":nombre,
        "apellido":apellido,
        "telefono":telefono
    }
    indice += 1

    agenda.append(contacto)
>>>>>>> b403902b25ef4cf83126ee85c09dbf3d22761ebe

def agregar(agenda, nombre, apellido, telefono):
    global indice
    
    #global contacto
    contacto = {
        "id":indice,
        "nombre":nombre,
        "apellido":apellido,
        "telefono":telefono
    }
    indice += 1

    agenda.append(contacto)

agregar()    



# Método para eliminar contacto
def eliminarContacto(id, agenda):
    for contacto in agenda:
        if contacto['id'] == id:
            agenda.remove(contacto)
            return





# Método para buscar contacto


