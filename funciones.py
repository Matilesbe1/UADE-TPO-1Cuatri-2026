import funcionesIndicadores

def mostrarOpciones(codigo, nombre, unidad, stockA, stockM, costo): # Matias Lesbegueris
    '''Muestra las opciones del menú principal divididas por categorías claras'''
    print("=" * 80)
    print(f"{'SISTEMA DE GESTIÓN DE PRODUCTOS':^80}")
    print("=" * 80)
    
    # SECCIÓN DE ACCIONES
    print(f"{'--- ACCIONES ---':^80}")
    print("1  | Alta de producto")
    print("2  | Modificar producto")
    print("3  | Baja de producto")
    print("") 
    
    # SECCIÓN DE CONSULTAS
    print(f"{'--- CONSULTAS ---':^80}")
    print("4  | Listado de productos")
    print("5  | Buscar producto por codigo")
    print("") 
    
    # SECCIÓN DE ORDENAMIENTOS Y REPORTES
    print(f"{'--- ORDENAMIENTOS Y REPORTES ---':^80}")
    print("6  | Lista ordenada por Stock Actual")
    print("7  | Reporte por unidad de medida")
    print("8  | Orden de costo de productos descendente")
    print("9  | Reporte de Stock Critico")
    print("10 | Contador de productos por unidad de medida")
    print("11 | Estadistica del Inventario")
    print("") 
    
    # SALIDA
    print("0  | Salir")
    print("=" * 80)
    
    opcion = int(input("Ingrese una opcion (0 para finalizar): "))
    while opcion < 0 or opcion > 11:
        print("Error. Elija una opcion valida.")
        opcion = int(input("Ingrese una opcion (0 para finalizar): "))
    if opcion == 1:
        altaDeProducto(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 2:
        modificarProducto(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 3:
        bajaProducto(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 4:
        mostrarListado(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 5:
        buscarProductoXCodigo(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 6:
        ordenarStockActual(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 7:
        filtrarMedida(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 8:
        ordenDescendente(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 9:
        stockCritico(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 10:
        contadorMedida(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 11:
        funcionesIndicadores.mostrarReporte(codigo, nombre, unidad, stockA, stockM, costo)
    elif opcion == 0:
        print("Gracias por usar el programa")
        return 0

# FUNCIONES PARA MODIFICAR PRODUCTOS
def mostrarMenuModif(): # Lorenzo Rossi
    '''Muestra las opciones del menú de modificaciones'''
    print("=" * 80)
    print(f"{'MENU DE MODIFICACIONES':^80}")
    print("=" * 80)
    print("1 | Nombre")
    print("2 | Unidad de medida")
    print("3 | Stock actual")
    print("4 | Stock mínimo")
    print("5 | Costo unitario")
    print("=" * 80)

def modifNombre(index, nombres): # Lorenzo Rossi
    '''Recibe el index del producto seleccionado y cambia su nombre por el elegido'''
    nombres[index] = input("Ingrese el nuevo nombre: ")
    while nombres[index] == " " or nombres[index] == "":
        print("El nombre no puede quedar vacío")
        nombres[index] = input("Ingrese el nuevo nombre: ")
    print('nombre modificado')

def modifUnidad(index, unidad): # Lorenzo Rossi
    '''Recibe el index del producto seleccionado y cambia su unidad de medida por la elegido'''
    nuevaUnidad = input("Ingrese la nueva unidad de medida (unidades, kilos, litros, metros): ")
    while nuevaUnidad != "kilos" and nuevaUnidad != "unidades" and nuevaUnidad != "litros" and nuevaUnidad != "metros":
        print("Error. Ingrese una unidad válida: kilos, litros, metros o unidades.")
        nuevaUnidad = input("Ingrese la nueva unidad de medida: ")
    unidad[index] = nuevaUnidad
    print('unidad modificada')

def modifStock(index, stockA, stockM, tipoStock): # Lorenzo Rossi
    '''Recibe el index del producto seleccionado y dependendiendo del valor de "tipoStock", que fue precargado anteriormente,
        da a elegir si sumar o restar stock en el minimo o en el actual. Siempre validando que el valor final no sea negativo.'''
    op = int(input(f"Desea sumar (1) o restar (2) stock al {tipoStock}: "))
    while op < 1 or op > 2:
        print("Error. Ingrese una opción válida: sumar (1) o restar (2).")
        op = int(input(f"Desea sumar (1) o restar (2) stock al {tipoStock}: "))
    if op == 1:
        cantSuma = int(input("Ingrese la cantidad que desea sumar: "))
        while cantSuma < 0:
            print("Error. Ingrese solo números positivos.")
            cantSuma = int(input("Ingrese la cantidad que desea sumar: "))
        if tipoStock == "actual":
            stockA[index] += cantSuma
        else:
            stockM[index] += cantSuma
    elif op == 2:
        cantResta = int(input("Ingrese la cantidad a restar. El stock no puede quedar negativo: "))
        if tipoStock == "actual":
            while cantResta < 0 or ((stockA[index] - cantResta) < 0):
                print(f"Error. Ingresó un valor negativo o un valor mayor al stock {tipoStock}.")
                cantResta = int(input("Ingrese la cantidad a restar: "))
            stockA[index] -= cantResta
        else:
            while cantResta < 0 or ((stockM[index] - cantResta) < 0):
                print(f"Error. Ingresó un valor negativo o un valor mayor al stock {tipoStock}.")
                cantResta = int(input("Ingrese la cantidad a restar: "))
            stockM[index] -= cantResta
    print('stock modificado')

def modifCosto(index, costo): # Lorenzo Rossi
    '''Recibe el producto elegido y la lista de costos. Realiza las operaciones de suma o resta correspondientes validando que el valor final no sea 0.'''
    op = int(input("Desea incrementar (1) el costo unitario o decrementarlo (2)?: "))
    while op < 1 or op > 2:
        print("Elija entre las opciones válidas: 1 para sumar o 2 para restar.")
        op = int(input("Desea incrementar (1) el costo unitario o decrementarlo (2)?: "))
    if op == 1:
        cantSuma = int(input("Ingrese la cantidad a sumar: "))
        while cantSuma < 0:
            print("Error. Ingrese un valor positivo.")
            cantSuma = int(input("Ingrese la cantidad a sumar: "))
        costo[index] += cantSuma
    else:
        cantResta = int(input("Ingrese la cantidad a restar. El valor final no puede terminar en 0: "))
        while cantResta < 0 or ((costo[index] - cantResta <= 0)):
            print("Error. Ingresó un valor negativo o un valor que convierte al costo en 0.")
            cantResta = int(input("Ingrese la cantidad a restar: "))
        costo[index] -= cantResta
    print('costo modificado')

def modificarProducto(codigos, nombres, unidad, stockActual, stockMinimo, costo): # Lorenzo Rossi
    '''Recibe todas las listas y da a elegir entre las modificaciones establecidas'''
    print("") # DESPEJA LA CONSOLA
    print("=" * 80)
    print(f"{'MODIFICACIÓN DE PRODUCTO':^80}")
    print("=" * 80)
    codigoInput = input("Ingrese el código del producto a modificar: ")
    
    indexCodigoInput = -1
    for i in range(len(codigos)):
        if codigos[i] == codigoInput:
            indexCodigoInput = i
            
    while indexCodigoInput == -1:
        print("No se encontró el código seleccionado. Intente nuevamente.")
        codigoInput = input("Ingrese el código del producto a modificar: ")
        for i in range(len(codigos)):
            if codigos[i] == codigoInput:
                indexCodigoInput = i
                
    # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
    mostrarEncabezadoTabla()
    print(f'{codigos[indexCodigoInput]:<10} | {nombres[indexCodigoInput]:<10} | {unidad[indexCodigoInput]:<10} | {stockActual[indexCodigoInput]:<12} | {stockMinimo[indexCodigoInput]:<12} | {costo[indexCodigoInput]:<10}')
    print("=" * 80)
    mostrarMenuModif()
    op = int(input("Producto encontrado. ¿Qué desea modificar?: "))
    while op < 1 or op > 5:
        print("Error. Elija entre las opciones establecidas (1-5)")
        op = int(input("¿Qué desea modificar?: "))
    if op == 1:
        modifNombre(indexCodigoInput, nombres)
    elif op == 2:
        modifUnidad(indexCodigoInput, unidad)
    elif op == 3:
        tipoStock = "actual"
        modifStock(indexCodigoInput, stockActual, stockMinimo, tipoStock)
    elif op == 4:
        tipoStock = "minimo"
        modifStock(indexCodigoInput, stockActual, stockMinimo, tipoStock)
    else:
        modifCosto(indexCodigoInput, costo)

# FUNCIONES BAJA DE PRODUCTO
def bajaProducto(codigos, nombres, unidades, stockActual, stockMinimo, costos): # Lorenzo Rossi
    print("") # DESPEJA LA CONSOLA
    print("=" * 80)
    print(f"{'BAJA DE PRODUCTO':^80}")
    print("=" * 80)
    codigoInput = input("Ingrese el código del producto que quiere dar de baja: ")
    
    indexCodigoInput = -1
    for i in range(len(codigos)):
        if codigos[i] == codigoInput:
            indexCodigoInput = i
            
    while indexCodigoInput == -1:
        print("No se encontró el código seleccionado. Intente nuevamente.")
        codigoInput = input("Ingrese el código del producto que quiere dar de baja: ")
        for i in range(len(codigos)):
            if codigos[i] == codigoInput:
                indexCodigoInput = i
                
    # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
    mostrarEncabezadoTabla()
    print(f'{codigos[indexCodigoInput]:<10} | {nombres[indexCodigoInput]:<10} | {unidades[indexCodigoInput]:<10} | {stockActual[indexCodigoInput]:<12} | {stockMinimo[indexCodigoInput]:<12} | {costos[indexCodigoInput]:<10}')
    print("=" * 80)
    op = input("Está seguro que quiere dar de baja el producto seleccionado (y/n)?: ")
    while op != "y" and op != "n":
        print("Error. Ingresó una respuesta inválida. Responda con y o n")
        op = input("Está seguro que quiere dar de baja el producto seleccionado (y/n)?: ")
    if op == "n":
        print("Ha seleccionado NO, por lo tanto el producto no fue dado de baja.")
    else:
        codigos.pop(indexCodigoInput)
        nombres.pop(indexCodigoInput)
        unidades.pop(indexCodigoInput)
        stockActual.pop(indexCodigoInput)
        stockMinimo.pop(indexCodigoInput)
        costos.pop(indexCodigoInput)
        print("Ha seleccionado SI, por lo tanto el producto fue dado de baja.")

# FUNCIONES ALTA DE PRODUCTO
def altaDeProducto(codigo, nombre, unidad, stockA, stockM, costo): # Matias Lesbegueris
    '''Recibe los nuevos datos que se quieren ingresar, los valida y los agrega a las listas'''
    print("") # DESPEJA LA CONSOLA
    print("=" * 80)
    print(f"{'ALTA DE NUEVO PRODUCTO':^80}")
    print("=" * 80)
    validarCodigoProducto(codigo)
    validarNombre(nombre)
    validarUnidad(unidad)
    validarStock(stockA, stockM)
    validarCosto(costo)

# RECIBE EL NUEVO CODIGO
def validarCodigoProducto(codigo):
    codigoN = input('Escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ')
    valido = 0
    while valido == 0:
        formatoOk = 0
        if len(codigoN) == 7 and codigoN[:3].isalpha() and codigoN[3:].isnumeric():
            formatoOk = 1
            
        coincidencias = 0
        for i in range(len(codigo)):
            if codigo[i] == codigoN:
                coincidencias += 1
                
        if formatoOk == 1 and coincidencias == 0:
            valido = 1
        else:
            print('ERROR: El codigo ya existe o no cumple con los requisitos. ')
            codigoN = input('Escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ')
    codigo.append(codigoN)

# RECIBE EL NUEVO NOMBRE
def validarNombre(nombre): # Matias Lesbegueris
    nombreN = input('Escriba el nombre del nuevo producto: ')
    repetido = 1
    while repetido == 1 or len(nombreN) == 0:
        coincidencias = 0
        for i in range(len(nombre)):
            if nombre[i] == nombreN:
                coincidencias += 1
        if coincidencias == 0 and len(nombreN) > 0:
            repetido = 0
        else:
            print('ERROR: Ya hay un producto con ese nombre o está vacío. ')
            nombreN = input('Escriba el nombre del nuevo producto: ')
    nombre.append(nombreN)

# RECIBE LA NUEVA UNIDAD
def validarUnidad(unidad): # Matias Lesbegueris
    unidadN = input('Escriba la unidad de medida del producto (kilos, litros, metros, unidades): ')
    while unidadN.lower() != 'kilos' and unidadN.lower() != 'litros' and unidadN.lower() != 'metros' and unidadN.lower() != 'unidades':
        unidadN = input('ERROR: Escriba una unidad de medida valida (kilos, litros, metros, unidades): ')
    unidad.append(unidadN)

# RECIBE EL NUEVO STOCK
def validarStock(stockA, stockM): # Matias Lesbegueris
    stockAN = int(input('Escriba el stock actual del producto: '))
    while stockAN <= 0:
        stockAN = int(input('ERROR: Escriba un stock valido: '))
    stockA.append(stockAN)
    
    # RECIBE EL STOCK MINIMO
    stockMN = int(input('Escriba el stock minimo requerido para el producto: '))
    while stockMN <= 0:
        stockMN = int(input('ERROR: Escriba un stock minimo valido: '))
    while stockMN > stockAN:
        stockMN = int(input('ERROR: El stock minimo no puede ser mayor que el stock actual, intente otra vez:  '))
    stockM.append(stockMN)

# RECIBE EL COSTO
def validarCosto(costo): # Matias Lesbegueris
    costoN = int(input('Escriba el costo unitario del producto: '))
    while costoN <= 0:
        costoN = int(input('ERROR: Escriba un costo por unidad valido: '))
    costo.append(costoN)
    print('El producto fue dado de alta')

# FUNCIONES MOSTRAR LISTADO
def mostrarListado(codigo, nombre, unidad, stockA, stockM, costo): # Matias Lesbegueris
    """ Muestra el listado de productos con sus respectivos datos """
    print("") 
    print("=" * 80)
    print(f"{'LISTADO TOTAL DE PRODUCTOS':^80}")
    
    # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
    mostrarEncabezadoTabla()
    for i in range(len(codigo)):
        print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
    print("=" * 80)

# CREO LA FUNCIÓN PARA MOSTRAR LOS PRODUCTOS FILTRADOS
def listadoMedida(codigo, nombre, unidad, stockA, stockM, costo, busqueda): # Uriel Aguilera Martínez
    '''Recorre la lista e imprime los productos que coinciden con la medida elegida'''
    encontrados = 0 
    print("=" * 80)
    print(f"{'RESULTADOS FILTRADOS POR MEDIDA':^80}")
    
    # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
    mostrarEncabezadoTabla()
    for i in range(len(unidad)):
        if unidad[i] == busqueda:
            print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
            encontrados += 1
    print("=" * 80)
    
    # SI EL CONTADOR QUEDÓ EN CERO, INFORMA QUE NO HUBO COINCIDENCIAS
    if encontrados == 0:
        print(f"No se encontraron productos con la unidad de medida: {busqueda}")
            
# FUNCIÓN FILTRADO POR UNIDAD DE MEDIDA
def filtrarMedida(codigo, nombre, unidad, stockA, stockM, costo): # Uriel Aguilera Martínez
    '''Permite elegir una unidad de medida y muestra los productos que la usan'''
    print("") 
    print("¿Que unidad de medida desea mostrar?: ")
    busqueda = pedirUnidadDeMedida() 
    listadoMedida(codigo, nombre, unidad, stockA, stockM, costo, busqueda)

# LISTADO DE PRODUCTOS POR ORDENAMIENTO DESCENDENTE 
def ordenDescendente(codigo, nombre, unidad, stockA, stockM, costo): # Uriel Aguilera Martínez
    """Nos muestra los productos ordenados de mayor a menor"""
    
    # HACEMOS UNA LISTA CON LA CANTIDAD DE PRODUCTOS
    cantidad = len(costo)
    indices = []
    for i in range(cantidad):
        indices.append(i)
    
    # HACEMOS UN CONTADOR PARA IR PASANDO EN LA LISTA
    pasada = 0
    while pasada < cantidad:
        for i in range(cantidad - 1):
            
            # CADA VEZ QUE REITERAMOS SUMAMOS 1 AL INDICE PARA COMPARAR NUEVAMENTE
            posActual = indices[i]
            posSiguiente = indices[i+1]
            
            # NOS FIJAMOS SI LA POSICION ACTUAL ES MENOR QUE LA SIGUIENTE
            if float(costo[posActual]) < float(costo[posSiguiente]):
                indices[i], indices[i+1] = indices[i+1], indices[i]
        pasada += 1
    
    # MOSTRAMOS EN PANTALLA LA LISTA ORDENADA SEGUN NUESTRO INDICE
    print("") 
    print("=" * 80)
    print(f"{'REPORTE DE COSTOS (MAYOR A MENOR)':^80}")
    
    # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
    mostrarEncabezadoTabla()
    for i in range(cantidad):
        pos = indices[i]
        print(f'{codigo[pos]:<10} | {nombre[pos]:<10} | {unidad[pos]:<10} | {stockA[pos]:<12} | {stockM[pos]:<12} | {costo[pos]:<10}')
    print("=" * 80)

# LISTADO DE PRODUCTOS CON STOCK IGUAL O INFERIOR AL STOCK MINIMO
def stockCritico(codigo, nombre, unidad, stockA, stockM, costo): # Uriel Aguilera Martínez
    """Muestra el stock en condiciones iguales o inferiores al stock minimo"""
    
    # DEFINIMOS CANTIDAD DE PRODUCTOS
    cantidad = len(costo)

    # CREAMOS VARIABLE PRODUCTOS PARA VER SI AL MENOS ENCONTRO UNO
    productos = 0
    
    print("") 
    print("=" * 80)
    print(f"{'REPORTE DE STOCK CRÍTICO':^80}")

    # RECORRE LA LISTA COMPARANDO EL STOCKA CON EL STOCKM Y LO MUESTRA EN PANTALLA
    for i in range(cantidad):
        if int(stockA[i]) <= int(stockM[i]):
            productos = 1
            
    # SI NO ENCONTRO NINGUN PRODUCTO MUESTRA EL MENSAJE
    if productos == 0:
        print("-" * 80)
        print("No hay productos con stock critico")
    else:
        # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
        mostrarEncabezadoTabla()
        for i in range(cantidad):
            if int(stockA[i]) <= int(stockM[i]):
                print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
        print("=" * 80)

# CREO LA FUNCIÓN PARA MOSTRAR LOS PRODUCTOS FILTRADOS
def calcularTotal(codigo, nombre, unidad, stockA, stockM, costo, busqueda): # Uriel Aguilera Martínez
    '''Recorre la lista y suma los productos de una unidad de medida a elección'''
    
    # VARIABLE QUE CUENTA LOS PRODUCTOS DE UNA MISMA UNIDAD DE MEDIDA
    totalProductos = 0 
    print("=" * 80)
    print(f"{'TOTALIZADOR POR MEDIDA':^80}")
    print("=" * 80)
    
    # RECORRE LA LISTA BUSCANDO PRODUCTOS CON MISMA UNIDAD Y LO SUMA A LA VARIABLE
    for i in range(len(unidad)):
        if unidad[i] == busqueda:
            totalProductos += 1
            
    # SI EL CONTADOR QUEDÓ EN CERO, INFORMA QUE NO HUBO COINCIDENCIAS
    if totalProductos == 0:
        print(f"No se encontraron productos con la unidad de medida: {busqueda}")
    else:
        print(f"Cantidad total de productos en {busqueda}: {totalProductos}")  
    print("=" * 80)

# MOSTRAR MENU DE OPCIONES DE UNIDAD DE MEDIDA
def pedirUnidadDeMedida(): # Uriel Aguilera Martínez
    '''Muestra el menú de unidades, valida la opción y retorna la opcion elegida'''
    print("=" * 80)
    print(f"{'OPCIONES DE MEDIDA':^80}")
    print("=" * 80)
    
    # MUESTRA EL MENÚ Y PIDE LA OPCIÓN
    print("1 | Kilos")
    print("2 | Litros")
    print("3 | Unidades")
    print("4 | Metros")
    print("=" * 80)
    opcion = int(input("Ingrese una opción: "))
    
    # VALIDACIÓN DE ELECCIÓN
    while opcion < 1 or opcion > 4:
        print("Error. Elija una opción valida.")
        print("=" * 80)
        print("1 | Kilos")
        print("2 | Litros")
        print("3 | Unidades")
        print("4 | Metros")
        print("=" * 80)
        opcion = int(input("Ingrese una opción: "))
        
    # GUARDA LA PALABRA SEGÚN LA OPCIÓN ELEGIDA
    if opcion == 1:
        resultado = "kilos"
    elif opcion == 2:
        resultado = "litros"
    elif opcion == 3:
        resultado = "unidades"
    else:
        resultado = "metros"
    
    return resultado

# CONTADOR DE PRODUCTOS POR UNIDAD DE MEDIDA
def contadorMedida(codigo, nombre, unidad, stockA, stockM, costo): # Uriel Aguilera Martínez
    """Cuenta la cantidad de productos de una medida en especifico"""
    print("") 
    print("Seleccione la unidad de medida para calcular el total de productos: ")
    busqueda = pedirUnidadDeMedida()
    
    # LLAMO A LA VARIABLE PARA MOSTRAR EN PANTALLA EL TOTAL DE PRODUCTOS DE UNA UNIDAD DE MEDIDA
    calcularTotal(codigo, nombre, unidad, stockA, stockM, costo, busqueda)

# TITULARES DE PANTALLA
def mostrarEncabezadoTabla(): # Uriel Aguilera Martínez
    '''Muestra el encabezado de titulos por pantalla'''
    print("=" * 80)
    print(f'{"Codigo":<10} | {"Nombre":<10} | {"Unidad":<10} | {"Stock Actual":<12} | {"Stock Minimo":<12} | {"Costo":<10}')
    print("-" * 80)

# FUNCION ORDENAMIENTO DE STOCK ACTUAL, DE MENOR A MAYOR 
def ordenarStockActual(codigo, nombre, unidad, stockA, stockM, costo): # Lorenzo Rossi
    '''Ordena la lista stockA de menor a mayor. También sus listas relacionadas. Se utiliza el método de ordenamiento por selección.'''
    for i in range(0, len(stockA) - 1):
        indexMin = i
        for j in range(i + 1, len(stockA)):
            if stockA[indexMin] > stockA[j]:
                indexMin = j
                
        # INTERCAMBIO STOCK ACTUAL
        aux = stockA[i]
        stockA[i] = stockA[indexMin]
        stockA[indexMin] = aux

        # INTERCAMBIO CODIGO
        aux = codigo[i]
        codigo[i] = codigo[indexMin]
        codigo[indexMin] = aux

        # INTERCAMBIO NOMBRE
        aux = nombre[i]
        nombre[i] = nombre[indexMin]
        nombre[indexMin] = aux

        # INTERCAMBIO UNIDAD
        aux = unidad[i]
        unidad[i] = unidad[indexMin]
        unidad[indexMin] = aux

        # INTERCAMBIO STOCK MINIMO
        aux = stockM[i]
        stockM[i] = stockM[indexMin]
        stockM[indexMin] = aux

        # INTERCAMBIO COSTO
        aux = costo[i]
        costo[i] = costo[indexMin]
        costo[indexMin] = aux
        
    print("") 
    print("=" * 80)
    print(f"{'ORDENAMIENTO POR STOCK ACTUAL':^80}")
    mostrarListado(codigo, nombre, unidad, stockA, stockM, costo)

def buscarProductoXCodigo(codigo, nombre, unidad, stockA, stockM, costo): # Matias Lesbegueris
    print("") # DESPEJA LA CONSOLA
    print("=" * 80)
    print(f"{'BÚSQUEDA DE PRODUCTO':^80}")
    print("=" * 80)
    buscado = input('Ingrese el codigo del producto que quiera buscar (-1 para finalizar): ')
    while buscado != '-1':
        indexEncontrado = -1
        for i in range(len(codigo)):
            if codigo[i] == buscado:
                indexEncontrado = i
                
        if indexEncontrado != -1:
            print('El producto existe.')
            # LLAMAMOS AL ENCABEZADO PROPIO DE LA TABLA
            mostrarEncabezadoTabla()
            print(f"{codigo[indexEncontrado]:<10} | {nombre[indexEncontrado]:<10} | {unidad[indexEncontrado]:<10} | {stockA[indexEncontrado]:<12} | {stockM[indexEncontrado]:<12} | {costo[indexEncontrado]:<10}")
            print("-" * 80)
        else:
            print('El producto no fue encontrado.')
        buscado = input('Ingrese el codigo del producto que quiera buscar (-1 para finalizar): ')
    