# Sistema de Gestión de Productos

##  Alcance del proyecto

Este proyecto consiste en un sistema de gestión de productos por consola, desarrollado en Python.
El usuario puede elegir entre distintas opciones para administrar productos:

* Dar de alta un producto
* Dar de baja un producto
* Modificar un producto
* Buscar producto por código
* Ver la lista de productos con diferentes filtros y ordenamientos:
    * Ordenados por stock actual
    * Ordenados por stock mínimo
    * Reporte según unidad de medida
    * Reporte de stocks mínimos
* Contador de productos por unidad de medida
* Salir del programa

---

##  Funcionalidades

###  Dar de alta un producto

Al registrar un producto, se realizan distintas validaciones:

* El código no puede repetirse
* Los primeros caracteres del código deben ser letras (`isalpha()`)
* Los últimos caracteres deben ser números (`isnumeric()`)
* El nombre del producto no puede repetirse
* La unidad de medida debe ser una de las válidas: kilos, litros, metros o unidades
* El stock actual debe ser mayor a 0
* El stock mínimo no puede ser mayor al stock actual
* El costo debe ser mayor a 0

---

###  Dar de baja un producto

Antes de eliminar un producto, el sistema solicita confirmación al usuario para evitar eliminaciones accidentales.

Luego, el producto se elimina utilizando el método `.pop()`.

---

###  Modificar un producto

La funcionalidad de modificación fue separada en funciones más pequeñas para:

* facilitar la lectura del código
* simplificar el mantenimiento
* detectar errores más fácilmente

El usuario puede elegir específicamente qué dato desea modificar.

---

###  Ver lista de productos

Permite visualizar todos los productos cargados en el sistema junto con su información.

---

### Buscar producto por código
 
Permite al usuario ingresar un código de producto para buscarlo. El sistema realiza una búsqueda secuencial y muestra todos los datos del producto si lo encuentra, o un mensaje informando que no existe. El proceso se repite hasta que el usuario ingrese `-1` para finalizar.
 
---
 
### Listado ordenado por stock actual
 
Genera un listado de todos los productos ordenados de menor a mayor según su stock actual. Se implementa el método de ordenamiento por selección sin utilizar funciones de Python como `sort()` o `sorted()`. El ordenamiento se aplica sobre todas las listas relacionadas para mantener la consistencia de los datos.
 
---
 
### Listado ordenado por costo unitario (descendente)
 
Genera un reporte de todos los productos ordenados de mayor a menor según su costo unitario. Se implementa el método de ordenamiento por burbujeo utilizando una lista de índices, de modo que las listas originales no se modifican.
 
---
 
### Reporte filtrado por unidad de medida
 
Permite al usuario seleccionar una unidad de medida (kilos, litros, metros o unidades) y muestra únicamente los productos que pertenecen a esa categoría. Si no se encuentran productos para la unidad seleccionada, se informa al usuario.
 
---
 
### Reporte de stock crítico
 
Muestra todos los productos cuyo stock actual es igual o inferior al stock mínimo definido. Estos productos requieren atención inmediata para reponer inventario. Si no hay productos en situación crítica, se informa al usuario.
 
---
 
### Contador de productos por unidad de medida
 
Permite al usuario seleccionar una unidad de medida y muestra la cantidad total de productos registrados bajo esa unidad. Si no hay productos para la unidad seleccionada, se informa al usuario.

---

###  Salir del programa

Finaliza la ejecución del sistema.

---

##  Tecnologías utilizadas

* Python

---

## ▶ Cómo ejecutar el proyecto

```bash
python main.py
```

---

##  Repositorio

GitHub:
https://github.com/Matilesbe1/UADE-TPO-1Cuatri-2026.git

