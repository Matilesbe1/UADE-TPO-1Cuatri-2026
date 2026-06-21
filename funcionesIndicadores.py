# Funciones pertenecientes al reporte #2
## Indicadores Generales de Inventario

codigo=['abc1111','abc2222','abc3333','abc4444']
nombre=["azucar","cinta","moto","cerveza"]
unidad=['kilos',"metros", "unidades","litros"]
stockA=[50,5,5,10]
stockM=[5,10,1,2]
costo=[100,50,500,250]

# codigo=[]
# nombre=[]
# unidad=[]
# stockA=[]
# stockM=[]
# costo=[]


def mostrarProd(codigo, nombre, stockA, indexEncontrado):
    '''Recibe las listas necesarias y el índice del producto que se desea mostrar. 
        Devuleve los valores correspondientes ordenados de forma visual y prolija'''
    print(f"Código: {codigo[indexEncontrado]} \nNombre: {nombre[indexEncontrado]} \nStock actual: {stockA[indexEncontrado]} \n")

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
    cantTotal = contadorProductos(codigo) # traemos de la función contadora la cantidad total de productos
    costoTotal = 0
    for i in range(len(costo)):
        costoTotal += costo[i]
    promedio = costoTotal / cantTotal
    return promedio

def prodMayorStockA(stockA):
    '''Recibe el stock actual de los prodcutos  y encuentra el máximo.
        Devuelve el índice del máximo encontrado para después ser mostrado por la dunción mostrarProd().'''
    maxStockA = 0
    indexEncontrado = -1
    for i in range(len(stockA)):
        if stockA[i] > maxStockA:
            maxStockA = stockA[i]
            indexEncontrado = i #guardamos el índice del mayor para luego mostrarlo con la función correspondiente
    return indexEncontrado


def prodMenorStockA(stockA):
    '''Recibe el stock actual de los prodcutos  y encuentra el mínimo.
        Devuelve el índice del mínimo encontrado para después ser mostrado por la dunción mostrarProd().'''
    minStockA = stockA[0]
    indexEncontrado = -1
    for i in range(len(stockA)):
        if stockA[i] < minStockA:
            minStockA = stockA[i]
            indexEncontrado = i #guardamos el índice menor para luego mostrarlo con otra función
    return indexEncontrado

def prodStockCritico(stockA, stockM):
    '''Recibe las listas de stock y verifica si existen productos con stock critico (stock actual menor o igual al mínimo).
        Si existen prodcutos retorna su cantidad mediante la variable conr (int), de lo contrario devuelve un mensaje.'''
    cont = 0
    for i in range(len(stockA)):
        if stockA[i] <= stockM[i]:
            cont += 1
    if cont != 0: #verificamos que haya algún stock critico y devolvemos la cantidad, de lo contrario devolvemos un mensaje.
        return cont
    else:
        return f"No se encontraron prodcutos con stock crítico."
    
def cantUniMedida(unidad):
    '''Se crean dos listas relacionadas: una con las unidaes posibles y otras con sus respectivos contadores.
        Primero se cuentan la cantidad de cada unidad.
        Luego se busca el máximo entre los contadores.
        Con el máximo encontrado, se vuelve a iterar en busca de duplicados. Si los hay se los guarda en una lista de máximos.
        Se retorna un mensaje con la unidad de medida y su cantidad'''
    
    lstUnidades = ["kilos","litros","metros","unidades"]
    lstContadores = [0, 0, 0, 0]
    for i in range(len(unidad)): #iteramos entre las distintas unidades y las contabilizamos
        for j in range(len(lstUnidades)):
            if unidad[i] == lstUnidades[j]:
                lstContadores[j] += 1

    maxCont = 0
    indexMax = -1
    for k in range(len(lstContadores)): #iteramos entre los contadores y buscamos el máximo
        if lstContadores[k] > maxCont:
            maxCont = lstContadores[k]
            indexMax = k
    lstMax = []
    for l in range(len(lstContadores)): #iteramos para verificar si hay duplicados del máximo
        if maxCont == lstContadores[l]:
            lstMax.append(lstUnidades[l])


    return f"La unidad de medida más utilizada fue: {lstMax}. \nCantidad: {lstContadores[indexMax]}"




    
        
    
def main():
    print("-"*54)
    print(f"{"#"*5} REPORTE ESTADÍSTICO GENERAL DEL INVENTARIO {"#"*5}")
    print("-"*54)
    
    print("Cantidad de prodcutos:")
    print(f"{contadorProductos(codigo)}\n")

    if contadorProductos(codigo) == 0:
        print(f"No se encontraron prodcutos. Verifique su inventrio o ingrese nuevos productos.")
    else:
        print("Valor total inventario:")
        print(f"${valorTotalInventario(codigo, stockA, costo):,} \n")
     
        print("Promedio costos unitarios:")
        print(f"${promCostoUnitario(codigo, costo):,}\n")
        
        print("Producto con mayor stock:")
        indiceMayor = prodMayorStockA(stockA)
        mostrarProd(codigo, nombre, stockA, indiceMayor)
        
        print("Producto con menor stock:")
        indiceMenor = prodMenorStockA(stockA)
        mostrarProd(codigo, nombre, stockA, indiceMenor)
        
        print("Productos con stock crítico:")
        print(f"{prodStockCritico(stockA, stockM)}\n")
        
        print("Unidad(es) de medida más utilizada(s):")
        print(f"{cantUniMedida(unidad)}\n")
        

main()


