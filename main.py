# import os

# os.system("cls")

# #ciclo repeticion for -> para
# for x in range(3):
#     print(f"se portaron bien el sabado{x}")
    
# contadornota = 0
# try:
#      cantidad = int (input("ingrese cantidad de notas a promediar"))
#      for x in range(cantidad):
#       nota = float(input(f"ingrese nota{x+1}"))
#      contadornota = contadornota + nota
#      promedio = round(contadornota/cantidad)   
#      #promedioredondeado = round(promedio) 
#      print(f"el resultado de {cantidad} nota es: {promedio}")
# except:
#     print("tipo de dato no es compatible")
    
#     # while  -> mientras 
bandera = True
 
while bandera:
     numero = int(input("ingrese un numero"))
     if numero%2==0 :
         print("puede elegir otro numero!")
     else:
         print ("el numero es impar,se acabo el ciclo")
         bandera = False
print ("muchas gracias por ocupar esta gran aplicacion")

a = 10
while a >= 10:
    a = int(input("ingrese numero"))
print ("bailecito")   
      