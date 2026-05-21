#Programa principal
import funciones #form branch lolo1

codigo=[111,222,333,444]
nombre=["azucar","cinta","moto","cerveza"]
unidad=['kg',"mts", "u","lts"]
stockA=[50,100,5,25]
stockM=[5,10,1,2]
costo=[100,50,500,250]

def main():
    funciones.altaDeProducto(codigo,nombre,unidad,stockA,stockM,costo)
    funciones.modificarProducto(codigo,nombre,unidad,stockA,stockM,costo)
    funciones.mostrarListado(codigo,nombre,unidad,stockA,stockM,costo)
    funciones.bajaProducto(codigo,nombre,unidad,stockA,stockM,costo)
main()