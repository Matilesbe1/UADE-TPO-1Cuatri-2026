# FUNCIONES *branch lolo1*
def mostrarMenuModif():
    '''Muestra las opciones del menú de modificaciones'''
    print("1: Nombre")
    print("2: Unidad de medida")
    print("3: Stock actual")
    print("4: Stock mínimo")
    print("5: Costo unitario")

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
        modifStock(indexCodigoInput, stockActual,tipoStock)
    elif op == 4:
        tipoStock = "minimo"
        modifStock(indexCodigoInput, stockActual, stockMinimo , tipoStock)
    else:
        modifCosto(indexCodigoInput, costo)
