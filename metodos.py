# Método para añadir contacto





# Método para eliminar contacto
def eliminarContacto(id, agenda):
    for contacto in agenda:
        if contacto['id'] == id:
            agenda.remove(contacto)
            return





# Método para buscar contacto


