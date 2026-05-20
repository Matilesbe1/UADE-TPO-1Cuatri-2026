import funciones
def main():
    codigo=['abc1234']
    nombre=['hola']
    unidad=['kg']
    stockA=[2]
    stockM=[1]
    costo=[500]
    funciones.altaDeProducto(codigo, nombre, unidad, stockA, stockM, costo)
    funciones.mostrarListado(codigo, nombre, unidad, stockA, stockM, costo)
main()