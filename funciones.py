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