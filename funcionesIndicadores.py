def mostrarProd(codigo, nombre, stockA, indexEncontrado):
    '''Recibe las listas necesarias y el índice del producto que se desea mostrar. 
        Devuleve los valores correspondientes ordenados de forma visual y prolija'''
    print(f"  | Código: {codigo[indexEncontrado]:<10} | Nombre: {nombre[indexEncontrado]:<12} | Stock: {stockA[indexEncontrado]:<6}")

def contadorProductos(codigo):
    '''Recibe la lista de productos, los cuenta y devuelve su cantidad como int'''
    cont = 0
    for i in range(len(codigo)):
        cont += 1
    return cont

def valorTotalInventario(codigo, stockA, costo):
    '''Recibe las listas correspondientes, suma el stockA de cada uno de ellos y devuelve el total como int'''
    sumaTotal = 0
    sumaProd = 0 
    for i in range(len(codigo)):
        sumaProd = stockA[i] * costo[i]
        sumaTotal += sumaProd
    return sumaTotal

def promCostoUnitario(codigo, costo):
    '''Recibe las listas correspondientes y toma la cantidad de la funcion contadorProdcutos().
        Luego suma los costos de cada uno de ellos y realiza el promedio. Devuelve este último como int.'''
    cantTotal = contadorProductos(codigo) # TRAEMOS DE LA FUNCIÓN CONTADORA LA CANTIDAD TOTAL DE PRODUCTOS
    costoTotal = 0
    for i in range(len(costo)):
        costoTotal += costo[i]
    
    # EVITAMOS DIVISIÓN POR CERO SI EL INVENTARIO ESTÁ VACÍO
    if cantTotal > 0:
        promedio = int(costoTotal / cantTotal)
    else:
        promedio = 0
    return promedio

def prodMayorStockA(stockA):
    '''Recibe el stock actual de los prodcutos  y encuentra el máximo.
        Devuelve el índice del máximo encontrado para después ser mostrado por la dunción mostrarProd().'''
    maxStockA = 0
    indexEncontrado = -1
    for i in range(len(stockA)):
        if stockA[i] > maxStockA:
            maxStockA = stockA[i]
            indexEncontrado = i # GUARDAMOS EL ÍNDICE DEL MAYOR PARA LUEGO MOSTRARLO CON LA FUNCIÓN CORRESPONDIENTE
    return indexEncontrado

def prodMenorStockA(stockA):
    '''Recibe el stock actual de los prodcutos y encuentra el mínimo.
        Devuelve el índice del mínimo encontrado para después ser mostrado por la dunción mostrarProd().'''
    indexEncontrado = -1
    if len(stockA) > 0:
        minStockA = stockA[0]
        indexEncontrado = 0
        for i in range(len(stockA)):
            if stockA[i] < minStockA:
                minStockA = stockA[i]
                indexEncontrado = i # GUARDAMOS EL ÍNDICE MENOR PARA LUEGO MOSTRARLO CON OTRA FUNCIÓN
    return indexEncontrado

def prodStockCritico(stockA, stockM):
    '''Recibe las listas de stock y verifica si existen productos con stock critico (stock actual menor o igual al mínimo).
        Si existen prodcutos retorna su cantidad mediante la variable conr (int), de lo contrario devuelve un mensaje.'''
    cont = 0
    for i in range(len(stockA)):
        if stockA[i] <= stockM[i]:
            cont += 1
    if cont != 0: # VERIFICAMOS QUE HAYA ALGÚN STOCK CRÍTICO Y DEVOLVEMOS LA CANTIDAD, DE LO CONTRARIO DEVOLVEMOS UN MENSAJE.
        return cont
    else:
        return f"No se encontraron productos con stock crítico."
    
def cantUniMedida(unidad):
    '''Se crean dos listas relacionadas: una con las unidaes posibles y otras con sus respectivos contadores.
        Primero se cuentan la cantidad de cada unidad.
        Luego se busca el máximo entre los contadores.
        Con el máximo encontrado, se vuelve a iterar en busca de duplicados. Si los hay se los guarda en una lista de máximos.
        Se retorna un mensaje con la unidad de medida y su cantidad'''
    
    lstUnidades = ["kilos","litros","metros","unidades"]
    lstContadores = [0, 0, 0, 0]
    for i in range(len(unidad)): # ITERAMOS ENTRE LAS DISTINTAS UNIDADES Y LAS CONTABILIZAMOS
        for j in range(len(lstUnidades)):
            if unidad[i] == lstUnidades[j]:
                lstContadores[j] += 1

    maxCont = 0
    indexMax = -1
    for k in range(len(lstContadores)): # ITERAMOS ENTRE LOS CONTADORES Y BUSCAMOS EL MÁXIMO
        if lstContadores[k] > maxCont:
            maxCont = lstContadores[k]
            indexMax = k
    lstMax = []
    for l in range(len(lstContadores)): # ITERAMOS PARA VERIFICAR SI HAY DUPLICADOS DEL MÁXIMO
        if maxCont == lstContadores[l] and maxCont > 0:
            lstMax.append(lstUnidades[l])

    if maxCont == 0:
        return "No hay unidades registradas todavía."

    return f"La unidad de medida más utilizada fue: {lstMax} | Cantidad: {lstContadores[indexMax]}"

def mostrarReporte(codigo, nombre, unidad, stockA, stockM, costo):
    '''Muestra el reporte estadístico general del inventario con diseño visual mejorado'''
    print("") # DESPEJA LA CONSOLA
    print("=" * 80)
    print(f"{'REPORTE ESTADÍSTICO GENERAL DEL INVENTARIO':^80}")
    print("=" * 80)
    
    cantProd = contadorProductos(codigo)
    print(f"  | CANTIDAD TOTAL DE PRODUCTOS REGISTRADOS: {cantProd}")
    print("-" * 80)
    
    if cantProd == 0:
        print(f"  [!] No se encontraron productos. Verifique su inventario o ingrese nuevos.")
        print("=" * 80)
    else:
        # BLOQUE 1: REPORTE FINANCIERO Y MONETARIO
        print(f"{'--- RESUMEN FINANCIERO ---':^80}")
        print(f"  | VALOR TOTAL DEL INVENTARIO : ${valorTotalInventario(codigo, stockA, costo):,}")
        print(f"  | PROMEDIO COSTOS UNITARIOS  : ${promCostoUnitario(codigo, costo):,}")
        print("")
        
        # BLOQUE 2: ALERTAS DE LOGÍSTICA Y STOCK
        print(f"{'--- LOGÍSTICA Y NIVELES DE STOCK ---':^80}")
        print("  [+] PRODUCTO CON MAYOR STOCK:")
        indiceMayor = prodMayorStockA(stockA)
        mostrarProd(codigo, nombre, stockA, indiceMayor)
        print("")
        
        print("  [-] PRODUCTO CON MENOR STOCK:")
        indiceMenor = prodMenorStockA(stockA)
        mostrarProd(codigo, nombre, stockA, indiceMenor)
        print("")
        
        print("  [!] PRODUCTOS CON STOCK CRÍTICO:")
        print(f"  | Cantidad detectada: {prodStockCritico(stockA, stockM)}")
        print("")
        
        # BLOQUE 3: MÉTRICAS DE OPERACIÓN
        print(f"{'--- MÉTRICAS DE OPERACIÓN ---':^80}")
        print(f"  | {cantUniMedida(unidad)}")
        print("=" * 80)