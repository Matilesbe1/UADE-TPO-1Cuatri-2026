def ValidarProducto(codigo, nombre, unidad, stockActual, stockMinimo, costo):
    
    if nombre.length==0:
        print('ERROR: el nombre del producto esta vacio')
    if unidad!= 'kg' or unidad!= 'lt'or unidad!= 'mts':
        print('ERROR: la unidad de medida no es valida')
    if stockActual<=0:
        print('el stock actual es invalido')
    if stockMinimo<=0:
        print('el stock minimo es invalido')
    if costo<=0:
        print('el costo unitario es invalido')
    return 

def altaDeProducto():
    codigo=input('escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ') #ARREGLAR ESTO 
    for i in range (len(codigo)):
        if codigo[i].isalpha():
            print('letra')
        elif codigo[i].isdigit():
            print('numero')
        else:
            print('error')
    nombre=input('escriba el nombre del nuevo producto: ')
    while len(nombre)==0:
        nombre=input('ERROR: escriba el nombre del nuevo producto: ')
        #añadir producto a lista
    unidad=input('escriba la unidad de medicion del producto (kg, lt, mts): ')
    while unidad!="kg" and unidad!= 'lt' and unidad== 'mts':
        unidad=input('ERROR: unidad erronea, escriba una unidad valida (kg, lt, mts): ')

    stockA=int(input('escriba el stock actual del producto: '))
    while stockA<=0:
        stockA=int(input('ERROR: escriba un stock valido: '))
    stockM=int(input('escriba el stock minimo requerido para el producto: '))
    while stockM<=0:
        stockM=int(input('ERROR: escriba un stock minimo valido: '))
        if stockM>stockA:
            stockM=int(input('ERROR: el stock minimo no puede ser mayor que el stock actual, intente otra vez:  '))
    costo=int(input('escriba el costo unitario del producto: '))
    while costo<=0:
        costo=int(input('ERROR: escriba un costo por unidad valido: '))


