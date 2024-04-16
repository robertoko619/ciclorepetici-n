#solicitar cantidad de pasajes
#crear ciclo de repeticion ´for´
#solicitar precio del pasaje
#validar con try except
#total ingresos
#romper bucle con break en caso que se ingrese un tipo de dato != int
#mostrar info del total de pasajes
totalingresos = 0
banderacantidad = 0
banderaprecio = 0
while banderacantidad:
    try:
        cantidad = int (input("ingrese cantidad de pasajes"))
        for x in range (cantidad):
           while banderaprecio:
               try:
                   precio = int (input(f"ingrese precio para pasaje n° {x+1} \n"))
                   totalingresos = totalingresos + precio
                   break
               except:
                   print ("opcion no valida")
        break           
    except: 
        print ("opcion no valida")

print(f"para los {cantidad} pasajes,el valor a pagar es: ${totalingresos}")
