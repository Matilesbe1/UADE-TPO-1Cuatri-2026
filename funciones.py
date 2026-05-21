# FUNCIONES PARA MODIFICAR PRODUCTOS
def mostrarMenuModif():
    '''Muestra las opciones del menú de modificaciones'''
    print("-"*80)
    print("1: Nombre")
    print("2: Unidad de medida")
    print("3: Stock actual")
    print("4: Stock mínimo")
    print("5: Costo unitario")
    print("-"*80)

def modifNombre(index,nombres):
    '''Recibe el index del producto seleccionado y cambia su nombre por el elegido'''
    nombres[index] = input("Ingrese el nuevo nombre: ")
    while nombres[index] == " " or nombres[index] == "":
        print("El nombre no puede quedar vacío")
        nombres[index] = input("Ingrese el nuevo nombre: ")

def modifUnidad(index,unidad):
    '''Recibe el index del producto seleccionado y cambia su unidad de medida por la elegido'''
    unidadesValidas = ["kilos", "unidades", "litros", "metros"]
    unidad[index] = input("Ingrese la nueva unidad de medida (unidades, kilos, litros, metros): ")
    while unidad[index] not in unidadesValidas:
        print("Error. Ingrese una unidad válida: kilos, litros, metros o unidades.")
        unidad[index] = input("Ingrese la nueva unidad de medida: ")

def modifStock(index, stockA, stockM, tipoStock):
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

def modifCosto(index,costo):
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

def modificarProducto(codigos,nombres,unidad,stockActual,stockMinimo,costo):
    '''Recibe todas las listas y da a elegir entre las modificaciones establecidas'''
    codigoInput = int(input("Ingrese el código del producto a modificar: "))
    indexCodigoInput = 0
    while codigoInput not in codigos:
        print("No se encontró el código seleccionado. Intente nuevamente.")
        codigoInput = int(input("Ingrese el código del producto a modificar: "))
    for i in range(len(codigos)):
        if codigos[i] == codigoInput:
            indexCodigoInput = i
    print(codigos[indexCodigoInput],nombres[indexCodigoInput],unidad[indexCodigoInput],stockActual[indexCodigoInput],stockMinimo[indexCodigoInput],costo[indexCodigoInput])
    mostrarMenuModif()
    op = int(input("Producto encontrado. ¿Qué desea modificar?: "))
    while op < 1 or op > 5:
        print("Error. Elija entre las opciones establecidas (1-5)")
        op = input("¿Qué desea modificar?: ")
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
def bajaProducto(codigos,nombres,unidades,stockActual,stockMinimo,costos):
    codigoInput = int(input("Ingrese el código del producto que quiere dar de baja: "))
    indexCodigoInput = 0
    while codigoInput not in codigos:
        print("No se encontró el código seleccionado. Intente nuevamente.")
        codigoInput = int(input("Ingrese el código del producto que quiere dar de baja: "))
    for i in range(len(codigos)):
        if codigos[i] == codigoInput:
            indexCodigoInput = i
    print("Producto encontrado")
    print(codigos[indexCodigoInput],nombres[indexCodigoInput],unidades[indexCodigoInput],stockActual[indexCodigoInput],stockMinimo[indexCodigoInput],costos[indexCodigoInput])
    op = input("Está seguro que quiere dar de baja el prodcuto seleccionado (Y/N)?: ")
    while op != "Y" and op != "N":
        print("Error. Ingresó una respuesta inválida. Responda con Y (si lo desea) o N (si no lo desea)")
        op = input("Está seguro que quiere dar de baja el prodcuto seleccionado (Y/N)?: ")
    if op == "N":
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
def altaDeProducto(codigo, nombre, unidad, stockA, stockM, costo):
    '''Recibe los nuevos datos que se quieren ingresar, los valida y los agrega a las listas'''
    codigoN=input('escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ')
    while len(codigoN)!=7:
        codigoN=input('ERROR: intente otra vez (no cumple con os requisitos): ') 
    if len(codigoN)==7:
        while not codigoN[:3].isalpha():
            codigoN=input('ERROR: intente otra vez (no cumple con os requisitos): ')
        while not codigoN[3:].isnumeric():
            codigoN=input('ERROR: intente otra vez (no cumple con os requisitos): ') 
        codigo.append(codigoN)
    nombreN=input('escriba el nombre del nuevo producto: ')
    while len(nombreN)==0:
        nombreN=input('ERROR: escriba el nombre del nuevo producto: ')
    nombre.append(nombreN)
    unidadN=input('escriba la unidad de medida del producto (kilos, litros, metros, unidades): ')
    while unidadN!= 'kilos' and unidadN!= 'litros' and  unidadN!= 'metros' and unidad!='unidades':
        unidadN=input('ERROR: escriba una unidad de medida valida (kilos, litros, metros): ')
    unidad.append(unidadN)
    stockAN=int(input('escriba el stock actual del producto: '))
    while stockAN<=0:
        stockAN=int(input('ERROR: escriba un stock valido: '))
    stockA.append(stockAN)
    stockMN=int(input('escriba el stock minimo requerido para el producto: '))
    while stockMN<=0:
        stockMN=int(input('ERROR: escriba un stock minimo valido: '))
    if stockMN>stockAN:
        stockMN=int(input('ERROR: el stock minimo no puede ser mayor que el stock actual, intente otra vez:  '))
    stockM.append(stockMN)
    costoN=int(input('escriba el costo unitario del producto: '))
    while costoN<=0:
        costoN=int(input('ERROR: escriba un costo por unidad valido: '))
    costo.append(costoN)

#FUNCIONES MOSTRAR LISTADO
def mostrarListado(codigo, nombre, unidad, stockA, stockM, costo):
    """ Muestra el listado de productos con sus respectivos datos """
    print(f'{'Codigo':<10} | {'Nombre':<10} | {'Unidad':<10} | {'Stock Actual':<10} | {'Stock minimo':<10} | {'Costo':<10}')
    print("-" * 80)
    for i in range (len(codigo)):
        print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
