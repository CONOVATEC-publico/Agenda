# Agenda

## Acerca del Proyecto

Este proyecto se basa en la creación de una agenda telefónica utilizando como lenguaje de programación a python y empleando como herramienta principal a la librería tkinter.

## Autores

- [Adrian Capcha](https://github.com/adriancapchaq)
- [Ever Terrazas](https://github.com/ETERRAZAS21PE)
- [Mario Calderón](https://github.com/mjcald)

## Tecnologías Empleadas

- Python

## Programa del Proyecto

- [x] Definición de la agenda telefónica
- [x] Ejecución del programa
- [x] Resultado

#### Definición de la agenda
Se desarrollará un programa en el que se agregará, filtrará y eliminará datos de contactos, al añadir la información se generará un id a fin de ubicar los datos del contacto en la agenda.

#### Ejecución del programa
Para ejecutar el programa nos ubicamos desde la terminal, en la carpeta principal (Agenda) y ejecutar el siguiente comando:

    python Test.py

#### Resultado:
En la primera etapa del proyecto se cargaron usuarios random al programa tal como se muestra en la Figura 1. Para agregar más usuarios se debe alimentar información por medio de los widgets Nombre, Apellido y Teléfono. 

![](https://i.ibb.co/rfB0Wp4/23-03-06-005700-Agenda-Telef-nica.png)
> Figura 1. Entorno gráfico con tkinter en python.

En una siguiente etapa se volvió a definir los elementos de la agenda por medio de los botones *Agregar*, *Eliminar* y *Ver detalle* a fin de editar los contactos mostrados en la Figura 2. También podemos observar la funcionalidad de la agenda mediante los filtros de contactos por ID, Nombre y Teléfono.

En la Figura 3.1 podemos observar el resultado de agregar un contacto sin seleccionar los elementos de la agenda. En la Figura 3.2 se ha definido un método para el botón *Cancelar* generando un messagebox del tipo 'askquestion'.

En la Figura 4 se observa el resultado de eliminar los contactos de la agenda donde se mostrará una ventana preguntando al usuario si está seguro de eliminar al contacto seleccionado.

Continuando con la descripción de los resultados, en la Figura 5 se mostrará la ventana *Ver detalle button* cuyo objetivo es modificar un contacto de la agenda, con el botón *Regresar* se retornará a la ventana principal y con el botón *Guardar* se modificarán los widgets Nombre, Apellido y Teléfono del contacto seleccionado.

Finalmente, en la Figura 6 se muestra el resultado del filtro de contactos o búsqueda de un contacto ya sea por su ID, Nombre o Teléfono, una vez ingresado la información a filtrar se dará acción al botón *Aplicar filtros* realizando la búsqueda correspondiente, si se desea realizar otra búsqueda se deberá accionar el botón *Limpiar filtros*.

![](https://i.ibb.co/SnxPvGN/23-05-22-201800-Agenda-Telef-nica.png)
> Figura 2. Nuevo entorno gráfico del proyecto con tkinter en python.

![](https://i.ibb.co/8mGYDW8/23-05-22-202900-Agenda-Telef-nica-Bot-n-Agregar-Bot-n-Guardar.png)
> Figura 3.1. Entorno gráfico para guardar o agregar contacto en la ventana Agregar button.

![](https://i.ibb.co/vvCgCNp/23-05-22-202300-Agenda-Telef-nica-Bot-n-Agregar-Bot-n-Cancelar.png)
> Figura 3.2. Entorno gráfico para cancelar la ventana Agregar button.

![](https://i.ibb.co/5kBrNCs/23-05-22-203400-Agenda-Telef-nica-Bot-n-Eliminar.png)
> Figura 4. Entorno gráfico para eliminar contactos de la agenda.

![](https://i.ibb.co/MMLNy2m/23-05-22-203700-Agenda-Telef-nica-Bot-n-Ver-detalle.png)
> Figura 5. Entorno gráfico para modificar contactos de la agenda.

![](https://i.ibb.co/HB3CMym/23-05-22-204400-Agenda-Telef-nica-Filtrar-por-ID.png)
> Figura 6. Entorno gráfico para buscar contactos de la agenda.