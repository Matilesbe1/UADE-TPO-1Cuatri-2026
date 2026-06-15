def mostrarOpciones(codigo, nombre, unidad, stockA, stockM, costo): #Matias Lesbegueris
    '''Muestra las opciones del menú principal'''
    print("-"*80)
    print("1: Alta de producto")
    print("2: Modificar producto")
    print("3: Baja de producto")
    print("4: Listado de productos")
    print("5: Buscar producto por codigo")
    print("6: Lista ordenada por Stock Actual")
    print("7: Reporte por unidad de medida")
    print("8: Orden de costo de productos descendente")
    print("9: Reporte de Stock Critico")
    print("10:Contador de productos por unidad de medida")
    print("0: Salir")
    print("-"*80)
    opcion=int(input("Ingrese una opcion (0 para finalizar): "))
    ejecutarOpcion(opcion)

def ejecutarOpcion(codigo,nombre,unidad,stockA,stockM,costo, opcion): #Matias Lesbegueris
    while opcion < 0 or opcion > 10:
        print("Error. Elija una opcion valida.")
        opcion=int(input("Ingrese una opcion (0 para finalizar): "))
    if opcion == 1:
        altaDeProducto(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 2:
        modificarProducto(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 3:
        bajaProducto(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 4:
        mostrarListado(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 5:
        buscarProductoXCodigo(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion== 6:
        ordenarStockActual(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 7:
        filtrarMedida(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 8:
        ordenDescendente(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 9:
        stockCritico(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion == 10:
        contadorMedida(codigo,nombre,unidad,stockA,stockM,costo)
    elif opcion ==0:
        print("Gracias por usar el programa")
        return 0

# FUNCIONES PARA MODIFICAR PRODUCTOS
def mostrarMenuModif(): #Lorenzo Rossi
    '''Muestra las opciones del menú de modificaciones'''
    print("-"*80)
    print("1: Nombre")
    print("2: Unidad de medida")
    print("3: Stock actual")
    print("4: Stock mínimo")
    print("5: Costo unitario")
    print("-"*80)

def modifNombre(index,nombres): #Lorenzo Rossi
    '''Recibe el index del producto seleccionado y cambia su nombre por el elegido'''
    nombres[index] = input("Ingrese el nuevo nombre: ")
    while nombres[index] == " " or nombres[index] == "":
        print("El nombre no puede quedar vacío")
        nombres[index] = input("Ingrese el nuevo nombre: ")
        print('nombre modificado')

def modifUnidad(index,unidad): #Lorenzo Rossi
    '''Recibe el index del producto seleccionado y cambia su unidad de medida por la elegido'''
    unidadesValidas = ["kilos", "unidades", "litros", "metros"]
    unidad[index] = input("Ingrese la nueva unidad de medida (unidades, kilos, litros, metros): ")
    while unidad[index] not in unidadesValidas:
        print("Error. Ingrese una unidad válida: kilos, litros, metros o unidades.")
        unidad[index] = input("Ingrese la nueva unidad de medida: ")
        print('unidad modificada')

def modifStock(index, stockA, stockM, tipoStock): #Lorenzo Rossi
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
        cantResta = int(input("Ingrese al cantidad a restar. El stock no puede quedar negativo"))
        if tipoStock == "actual":
            while cantResta < 0 or ((stockA[index]-cantResta) < 0):
                print(f"Error. Ingresó un valor negativo o un valor mayor al stock {tipoStock}.")
                cantResta = int(input("Ingrese al cantidad a restar. El stock no puede quedar negativo"))
            stockA[index] -= cantResta
        else:
            while cantResta < 0 or ((stockM[index]-cantResta) < 0):
                print(f"Error. Ingresó un valor negativo o un valor mayor al stock {tipoStock}.")
                cantResta = int(input("Ingrese al cantidad a restar. El stock no puede quedar negativo"))
            stockM[index] -= cantResta
    print('stock modificado')

def modifCosto(index,costo): #Lorenzo Rossi
    '''Recibe el producto elegido y la lista de costos. Realiza las operaciones de suma o resta correspondientes validando que el vallor final no sea 0.'''
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
        cantResta = int(input("Ingrese la cantidad a restar. El valor final no puede terminar en 0"))
        while cantResta < 0 or ((costo[index] - cantResta <= 0)):
            print("Error. Ingresó un valor negativo o un valor que convierte al costo en 0.")
            cantResta = int(input("Ingrese la cantidad a restar. El valor final no puede terminar en 0"))
        costo[index] -= cantResta
    print('costo modificado')

def modificarProducto(codigos,nombres,unidad,stockActual,stockMinimo,costo): #Lorenzo Rossi
    '''Recibe todas las listas y da a elegir entre las modificaciones establecidas'''
    codigoInput = input("Ingrese el código del producto a modificar: ")
    indexCodigoInput = 0
    while codigoInput not in codigos:
        print("No se encontró el código seleccionado. Intente nuevamente.")
        codigoInput = input("Ingrese el código del producto a modificar: ")
    for i in range(len(codigos)):
        if codigos[i] == codigoInput:
            indexCodigoInput = i
    print(codigos[indexCodigoInput],nombres[indexCodigoInput],unidad[indexCodigoInput],stockActual[indexCodigoInput],stockMinimo[indexCodigoInput],costo[indexCodigoInput])
    mostrarMenuModif()
    op = int(input("Producto encontrado. ¿Qué desea modificar?: "))
    while op < 1 or op > 5:
        print("Error. Elija entre las opciones establecidas (1-5)")
        op = int(input("¿Qué desea modificar?: "))
    if op == 1:
        modifNombre(indexCodigoInput,nombres)
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

#FUNCIONES BAJA DE PRODCUTO
def bajaProducto(codigos,nombres,unidades,stockActual,stockMinimo,costos): #Lorenzo Rossi
    codigoInput = input("Ingrese el código del producto que quiere dar de baja: ")
    indexCodigoInput = 0
    while codigoInput not in codigos:
        print("No se encontró el código seleccionado. Intente nuevamente.")
        codigoInput = input("Ingrese el código del producto que quiere dar de baja: ")
    for i in range(len(codigos)):
        if codigos[i] == codigoInput:
            indexCodigoInput = i
    print("Producto encontrado")
    print(codigos[indexCodigoInput],nombres[indexCodigoInput],unidades[indexCodigoInput],stockActual[indexCodigoInput],stockMinimo[indexCodigoInput],costos[indexCodigoInput])
    op = input("Está seguro que quiere dar de baja el prodcuto seleccionado (y/n)?: ")
    while op != "y" and op != "n":
        print("Error. Ingresó una respuesta inválida. Responda con y (si lo desea) o n (si no lo desea)")
        op = input("Está seguro que quiere dar de baja el prodcuto seleccionado (y/n)?: ")
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

#FUNCIONES ALTA DE PRODUCTO
def altaDeProducto(codigo, nombre, unidad, stockA, stockM, costo): #Matias Lesbegueris
    '''Recibe los nuevos datos que se quieren ingresar, los valida y los agrega a las listas'''
    validarCodigoProducto(codigo)
    validarNombre(nombre)
    validarUnidad(unidad)
    validarStock(stockA, stockM)
    validarCosto(costo)

#RECIBE EL NUEVO CODIGO
def validarCodigoProducto(codigo):
    codigoN=input('escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ')
    while not codigoN[:3].isalpha() or not codigoN[3:].isnumeric() or len(codigoN)!=7:
        for i in range (len(codigo)):
            while codigoN==codigo[i] or not codigoN[:3].isalpha() or not codigoN[3:].isnumeric() or len(codigoN)!=7:
                print('ERROR: el codigo ya existe o no cumple con los requisitos. ')
                codigoN=input('escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ')
        
    codigo.append(codigoN)

#RECIBE EL NUEVO NOMBRE
def validarNombre(nombre): #Matias Lesbegueris
    nombreN=input('escriba el nombre del nuevo producto: ')
    for i in range (len(nombre)):
        while nombreN==nombre[i]:
            print('ERROR: ya hay un producto con ese nombre. ')
            nombreN=input('escriba el nombre del nuevo producto: ')
    while len(nombreN)==0:
        nombreN=input('ERROR: escriba el nombre del nuevo producto: ')
    nombre.append(nombreN)
#RECIBE LA NUEVA UNIDAD
def validarUnidad(unidad):#Matias Lesbegueris
    unidadN=input('escriba la unidad de medida del producto (kilos, litros, metros, unidades): ')
    while unidadN.lower()!= 'kilos' and unidadN.lower()!= 'litros' and  unidadN.lower()!= 'metros' and unidadN.lower()!='unidades':
        unidadN=input('ERROR: escriba una unidad de medida valida (kilos, litros, metros, unidades): ')
    unidad.append(unidadN)
#RECIBE EL NUEVO STOCK
def validarStock(stockA, stockM):#Matias Lesbegueris
    stockAN=int(input('escriba el stock actual del producto: '))
    while stockAN<=0:
        stockAN=int(input('ERROR: escriba un stock valido: '))
    stockA.append(stockAN)
#RECIBE EL STOCK MINIMO
    stockMN=int(input('escriba el stock minimo requerido para el producto: '))
    while stockMN<=0:
        stockMN=int(input('ERROR: escriba un stock minimo valido: '))
    while stockMN>stockAN:
        stockMN=int(input('ERROR: el stock minimo no puede ser mayor que el stock actual, intente otra vez:  '))
    stockM.append(stockMN)
#RECIBE EL COSTO
def validarCosto(costo):#Matias Lesbegueris
    costoN=int(input('escriba el costo unitario del producto: '))
    while costoN<=0:
        costoN=int(input('ERROR: escriba un costo por unidad valido: '))
    costo.append(costoN)
    print('producto dado de alta')

#FUNCIONES MOSTRAR LISTADO
def mostrarListado(codigo, nombre, unidad, stockA, stockM, costo): #Matias Lesbegueris
    """ Muestra el listado de productos con sus respectivos datos """
    print(f'{"Codigo":<10} | {"Nombre":<10} | {"Unidad":<10} | {"Stock Actual":<10} | {"Stock minimo":<10} | {"Costo":<10}')
    print("-" * 80)
    for i in range (len(codigo)):
        print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')

# CREO LA FUNCIÓN PARA MOSTRAR LOS PRODUCTOS FILTRADOS
def listadoMedida (codigo, nombre, unidad, stockA, stockM, costo, busqueda):
    '''Recorre la lista e imprime los productos que coinciden con la medida elegida'''

    encontrados = 0 
    print("=" * 76)
    for i in range (len(unidad)):
        if unidad[i] == busqueda:
            print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
            encontrados += 1
    print("=" * 76)

    # SI EL CONTADOR QUEDÓ EN CERO, INFORMA QUE NO HUBO COINCIDENCIAS
    if encontrados == 0:
        print(f"No se encontraron productos con la unidad de medida: {busqueda}")
            
# FUNCIÓN FILTRADO POR UNIDAD DE MEDIDA
def filtrarMedida(codigo, nombre, unidad, stockA, stockM, costo): #Uriel Aguilera Martínez
    '''Permite elegir una unidad de medida y muestra los productos que la usan'''

    # MUESTRA EL MENÚ Y PIDE LA OPCIÓN
    print ("¿Que unidad de medida desea mostrar?: ")
    print ("1 | Kilos")
    print ("2 | Litros")
    print ("3 | Unidades")
    print ("4 | Metros")
    opcion=int(input("Ingrese una opción: "))

    # VALIDO LA OPCIÓN
    while opcion < 1 or opcion > 4:
        print("Error. Elija una opción valida.")
        print ("1 | Kilos")
        print ("2 | Litros")
        print ("3 | Unidades")
        print ("4 | Metros")
        opcion=int(input("Ingrese una opción: "))
    
    # GUARDA LA PALABRA SEGÚN LA OPCIÓN ELEGIDA
    if opcion == 1:
        busqueda = "kilos"
    elif opcion == 2:
        busqueda = "litros"
    elif opcion == 3:
        busqueda = "unidades"
    else:
        busqueda = "metros"

    #LLAMO A LA FUNCIÓN PARA LISTAR LOS PRODUCTOS
    listadoMedida (codigo, nombre, unidad, stockA, stockM, costo, busqueda)

# LISTADO DE PRODUCTOS POR ORDENAMIENTO DESCENDENTE 
def ordenDescendente (codigo, nombre, unidad, stockA, stockM, costo): #Uriel Aguilera Martínez
    """Nos muestra los productos ordenados de mayor a menor"""

    #HACEMLOS UNA LISTA CON LA CANIDAD DE PRODCUTOS
    cantidad = len(costo)
    indices = []
    for i in range(cantidad):
        indices.append(i)
    
    #HACEMOS UN CONTADOR PARA IR PASANDO EN LA LISTA
    pasada = 0
    while pasada < cantidad:
        for i in range(cantidad - 1):
            
            #CADA VEZ QUE REITERAMOS SUMAMOS 1 AL INDICE PARA COMPARAR NUEVAMENTE
            pos_actual = indices[i]
            pos_siguiente = indices[i+1]
            
            #NOS FIJAMOS SI LA POSICION ACTUAL ES MENOR QUE LA SIGUIENTE
            if float(costo[pos_actual]) < float(costo[pos_siguiente]):
                indices[i], indices[i+1] = indices[i+1], indices[i]
                
        pasada += 1
    
    #MOSTRAMOS EN PANTALLA LA LISTA ORDENADA SEGUN NUESTRO INDICE
    print("REPORTE DE COSTOS (MAYOR A MENOR)")
    print("=" * 76)
    if pasada == 0:
        print("No hay productos para mostrar")
        print("=" * 76)
    for i in range(cantidad):
        pos = indices[i]
        print(f'{codigo[pos]:<10} | {nombre[pos]:<10} | {unidad[pos]:<10} | {stockA[pos]:<12} | {stockM[pos]:<12} | {costo[pos]:<10}')
    print("=" * 76)

# LISTADO DE PRODUCTOS CON STOCK IGUAL O INFERIOR AL STOCK MINIMO
def stockCritico (codigo, nombre, unidad, stockA, stockM, costo): #Uriel Aguilera Martínez
    """Muestra el stock en condiciones iguales o inferiores al stock minimo"""
    
    #DEFINIMOS CANTIDAD DE PRODUCTOS
    cantidad = len(costo)

    #CREAMOS VARIABLE PRODUCTOS PARA VER SI AL MENOS ENCONTRO UNO
    productos = 0
    print("=" * 76)
    print(f"{'REPORTE DE STOCK CRÍTICO':^76}")
    print("=" * 76)

    #RECORRE LA LISTA COMPARANDO EL STOCKA CON EL STOCKM Y LO MUESTRA EN PANTALLA
    for i in range(cantidad):
        if int(stockA[i]) <= int(stockM[i]):
            print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
            productos = 1

    #SI NO ENCONTRO NINGUN PRODUCTO MUESTA EL MENSAJE 
    if productos != 1 :
        print("No hay productos con stock critico")

# CREO LA FUNCIÓN PARA MOSTRAR LOS PRODUCTOS FILTRADOS
def calcularTotal (codigo, nombre, unidad, stockA, stockM, costo, busqueda):
    '''Recorre la lista y suma los productos de una unidad de medida a elección'''

    #VARIABLE QUE CUENTA LOS PRODUCTOS DE UNA MIDA UNIDAD DE MEDIDA
    totalProductos = 0 
    print("=" * 76)

    #RECORRE LA LISTA BUSCANDO PRODUCTOS CON MISMA UNIDAD Y LO SUMA A LA VARIABLE
    for i in range (len(unidad)):
        if unidad[i] == busqueda:
            totalProductos += 1
                
    # SI EL CONTADOR QUEDÓ EN CERO, INFORMA QUE NO HUBO COINCIDENCIAS
    if totalProductos == 0:
        print(f"No se encontraron productos con la unidad de medida: {busqueda}")
    else:
        print(f"Cantidad total de productos en {busqueda}: {totalProductos}")  
    print("=" * 76)

#  CONTADOR DE PRODUCTOS POR UNIDAD DE MEDIDA
def contadorMedida (codigo, nombre, unidad, stockA, stockM, costo): #Uriel Aguilera Martínez
    """Cuenta la cantidad de productos de una medida en especifico"""

    # MUESTRA EL MENÚ Y PIDE LA OPCIÓN
    print ("Seleccione la unidad de medida para calcular el total de productos: ")
    print ("1 | Kilos")
    print ("2 | Litros")
    print ("3 | Unidades")
    print ("4 | Metros")
    opcion=int(input("Ingrese una opción: "))

    # VALIDO LA OPCIÓN
    while opcion < 1 or opcion > 4:
        print("Error. Elija una opción valida.")
        print ("1 | Kilos")
        print ("2 | Litros")
        print ("3 | Unidades")
        print ("4 | Metros")
        opcion=int(input("Ingrese una opción: "))

    # GUARDA LA PALABRA SEGÚN LA OPCIÓN ELEGIDA
    if opcion == 1:
        busqueda = "kilos"
    elif opcion == 2:
        busqueda = "litros"
    elif opcion == 3:
        busqueda = "unidades"
    else:
        busqueda = "metros"

    #LLAMO A LA VARIABLE PARA MOSTRAR EN PANTALLA EL TOTAL DE PRODUCTOS DE UNA UNIDAD DE MEDIDA
    calcularTotal (codigo, nombre, unidad, stockA, stockM, costo, busqueda)

#FUNCION ORDENAMIENTO DE STOCK ACTUAL, DE MENOR A MAYOR 
def ordenarStockActual(codigo, nombre, unidad, stockA, stockM, costo): #Lorenzo Rossi
    '''Ordena la lista stockA de menor a mayor. También sus listas relacionadas.
        Se utiliza el método de ordenamiento por selección.'''
    for i in range(0,len(stockA)-1):
        index_min = i
        for j in range(i+1,len(stockA)):
            if stockA[index_min] > stockA[j]:
                index_min = j
        #intercambio stock actual
        aux = stockA[i]
        stockA[i] = stockA[index_min]
        stockA[index_min] = aux

        #intercambio codigo
        aux = codigo[i]
        codigo[i] = codigo[index_min]
        codigo[index_min] = aux

        #intercambio nombre
        aux = nombre[i]
        nombre[i] = nombre[index_min]
        nombre[index_min] = aux

        #intercambio unidad
        aux = unidad[i]
        unidad[i] = unidad[index_min]
        unidad[index_min] = aux

        #intercambio stock minimo
        aux = stockM[i]
        stockM[i] =stockM[index_min]
        stockM[index_min] = aux

        #intercambio costo
        aux = costo[i]
        costo[i] = costo[index_min]
        costo[index_min] = aux
    print("-" * 80)
    print("PRODUCTOS ORDENADOS POR STOCK ACTUAL")
    print("-" * 80)
    mostrarListado(codigo, nombre, unidad, stockA, stockM, costo)

def buscarProductoXCodigo(codigo, nombre, unidad, stockA, stockM, costo): #Matias Lesbegueris
    buscado=input('Ingrese el codigo del producto que quiera buscar (-1 para finalizar): ')
    indexEncontrado = 0
    while buscado!='-1':
        encontrado = False
        for i in range (len(codigo)):
            if codigo[i]==buscado:
                encontrado=True
                indexEncontrado = i
        if encontrado==True:
            print('El producto existe.')
            print(f'{"Codigo":<10} | {"Nombre":<10} | {"Unidad":<10} | {"Stock Actual":<10} | {"Stock minimo":<10} | {"Costo":<10}')
            print("-" * 80)
            print(f'{codigo[indexEncontrado]:<10} | {nombre[indexEncontrado]:<10} | {unidad[indexEncontrado]:<10} | {stockA[indexEncontrado]:<12} | {stockM[indexEncontrado]:<12} | {costo[indexEncontrado]:<10}')
        else:
            print('El producto no fue encontrado.')
        buscado=input('Ingrese el codigo del producto que quiera buscar (-1 para finalizar): ')
    return 


