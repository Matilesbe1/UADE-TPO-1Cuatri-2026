#Programa principal
import funciones 

codigo=['abc1111','abc2222','abc3333','abc4444']
nombre=["azucar","cinta","moto","cerveza"]
unidad=['kilos',"metros", "unidades","litros"]
stockA=[50,100,5,25]
stockM=[5,10,1,2]
costo=[100,50,500,250]

def main():
    funciones.mostrarOpciones(codigo,nombre,unidad,stockA,stockM,costo)
main()