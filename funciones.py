def altaDeProducto():
    codigo=input('escriba el codigo del nuevo producto, tiene que tener 3 letras y 4 numeros. Por ejemplo: abc1234: ')
    while len(codigo)!=7:
        codigo=input('ERROR: intente otra vez (no cumple con os requisitos): ') 
    if len(codigo)==7:
        while not codigo[:3].isalpha():
            codigo=input('ERROR: intente otra vez (no cumple con os requisitos): ')
        while not codigo[3:].isnumeric():
            codigo=input('ERROR: intente otra vez (no cumple con os requisitos): ') 
    nombre=input('escriba el nombre del nuevo producto: ')
    while len(nombre)==0:
        nombre=input('ERROR: escriba el nombre del nuevo producto: ')
        #añadir producto a lista
    unidad=input('escriba la unidad de medida del producto (kg, lt, mts): ')
    while unidad!= 'kg' and unidad!= 'lt' and  unidad!= 'mts':
        unidad=input('ERROR: escriba una unidad de medida valida (kg, lt, mts): ')
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


