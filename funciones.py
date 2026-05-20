def altaDeProducto(codigo, nombre, unidad, stockA, stockM, costo):
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
    unidadN=input('escriba la unidad de medida del producto (kg, lt, mts): ')
    while unidadN!= 'kg' and unidadN!= 'lt' and  unidadN!= 'mts':
        unidadN=input('ERROR: escriba una unidad de medida valida (kg, lt, mts): ')
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

def mostrarListado(codigo, nombre, unidad, stockA, stockM, costo):
    print(f'{'Codigo':<10} | {'Nombre':<10} | {'Unidad':<10} | {'Stock Actual':<10} | {'Stock minimo':<10} | {'Costo':<10}')
    print("-" * 80)
    for i in range (len(codigo)):
        print(f'{codigo[i]:<10} | {nombre[i]:<10} | {unidad[i]:<10} | {stockA[i]:<12} | {stockM[i]:<12} | {costo[i]:<10}')
