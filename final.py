#INICIANDO PEDIDO DE DATOS
def ruta():   
   print("\nDIGITE EL VALOR PARA CADA RUTA PISIBLE EN DECIMALES O ENTEROS, QUE REPRESENTAN LOS KMS (SOLO DATOS MAYORES A CERO), \nEL RECORRIDO INICIA DEL PUNTO 'A' Y TERMINA EN 'H' ")
   print ("\n\nINICIANDO RECORRIDO PUNTO A\n")
   A1 = float(input("RUTA A1: "))
   A2 = float(input("RUTA A2: "))   
   A3 = float(input("RUTA A3: ")) 
   B1 = float(input("RUTA B1: "))
   B2 = float(input("RUTA B2: "))   
   C1 = float(input("RUTA C1: "))
   C2 = float(input("RUTA C2: "))
   D1 = float(input("RUTA D1: ")) 
   E1 = float(input("RUTA E1: "))
   E2 = float(input("RUTA E2: "))
   E3 = float(input("RUTA E3: "))
   F1 = float(input("RUTA F1: "))
   G1 = float(input("RUTA G1: "))
   print("\nDESTINO PUNTO H\n\n")
   
   print("-- DATOS PARA CALCULOS --") 

#CALCULO DE FUNCIONALIDADES
   
   COSTO_GASOLINA = float(input("\nCOSTO DE GASOLINA POR LITRO: "))
   VELOCIDAD = float(input("\nVELOCIDAD CONSTANTE BASADA EN KM/H: "))
   GASOLINA_DISPONIBLE = float(input("\n¿CUANTOS LITROS DE GASOLINA DISPONE? "))
   print("\nNOTA: SE ESTIMA QUE EL CONSUMO PROMEDIO DE UN AUTOMOVIL ES DE: 10KM POR LITRO.")

   
#LISTA DE LAS RUTAS POSIBLES
   R1 = [A1, B1, F1]
   R2 = [A1, B2, D1, E1, F1]
   R3 = [A1, B2, D1, E2]
   R4 = [A1, B2, D1, E3, G1]
   R5 = [A2, D1, E1, F1]
   R6 = [A2, D1, E2]
   R7 = [A2, D1, E3, G1]
   R8 = [A3, C1, D1, E1, F1]
   R9 = [A3, C1, D1, E2]
   R10 = [A3, C1, D1, E3, G1]
   R11 = [A3, C2, G1]

#ASIGNACION STRING A LISTA:

   RF1 = ["A1", "B1", "F1"]
   RF2 = ["A1", "B2", "D1", "E1", "F1"]
   RF3 = ["A1", "B2", "D1", "E2"]
   RF4 = ["A1", "B2", "D1", "E3", "G1"]
   RF5 = ["A2", "D1", "E1", "F1"]
   RF6 = ["A2", "D1", "E2"]
   RF7 = ["A2", "D1", "E3", "G1"]
   RF8 = ["A3", "C1", "D1", "E1", "F1"]
   RF9 = ["A3", "C1", "D1", "E2"]
   RF10 = ["A3", "C1", "D1", "E3", "G1"]
   RF11 = ["A3", "C2", "G1"]

#PROMEDIO DE LAS LISTAS PARA CALCULAR LA RUTA CORTA
   
   LISTA = []
    
   P1 = sum(R1)
   LISTA.append(P1)

   P2 = sum(R2)
   LISTA.append(P2)

   P3 = sum(R3)
   LISTA.append(P3)


   P4 = sum(R4)
   LISTA.append(P4)

   P5 = sum(R5)
   LISTA.append(P5)

   P6 = sum(R6)
   LISTA.append(P6)

   P7 = sum(R7)
   LISTA.append(P7)

   P8 = sum(R8)
   LISTA.append(P8)

   P9 = sum(R9)
   LISTA.append(P9)

   P10 = sum(R10)
   LISTA.append(P10)

   P11 = sum(R11)
   LISTA.append(P11)

   MINIMA=min(LISTA)
   MAXIMA=max(LISTA)



#CALCULO DE FUNCIONALIDADES


#CALCULO DE CONSUMO DE COMBUSTIBLE, DONDE 10 SON KM.
   
   CONSUMO_MINIMO = MINIMA / 10 #LITROS
   CONSUMO_MAXIMO =MAXIMA/10
   GASOLINA_RESTANTE=GASOLINA_DISPONIBLE - CONSUMO_MINIMO
   RECORRE_KM = GASOLINA_RESTANTE*10 #ALCANZA PARA ESTOS KILOMETROS
   NO_SUFICIENTE = GASOLINA_DISPONIBLE/10
   AHORRO=CONSUMO_MAXIMO - CONSUMO_MINIMO     
   


#COMPARACION DE GASOLINA SUFICIENTE:
   print("\n\n--DATOS DE CONSUMO--\n")

   if(GASOLINA_DISPONIBLE>=CONSUMO_MINIMO and GASOLINA_DISPONIBLE>0):
      print("CONSUMO:",MINIMA,"KM, CONSUMIRA", CONSUMO_MINIMO,
            "L, POR LO TANTO, LE RESTARÁN", GASOLINA_RESTANTE,"LITRO(S), PARA RECORRER",RECORRE_KM,"KM(S)")
      print("\nAHORRO: BASADO EN LA RUTA MAXIMA DE ",MAXIMA,"KM(S),", "USTED ESTA AHORRANDO", AHORRO,"LITROS, POR LO TANTO SE AHORRA", AHORRO*COSTO_GASOLINA, "PESOS")

   else:
      
      return print("**USTED NO CUENTA CON SUFICIENTE COMBUSTIBLE, SOLO PODRA RECORRER", NO_SUFICIENTE,"KM(S)\n", "NO PUEDE REALIZAR SU RECORRIDO DE", MINIMA,"KM(S)")


#COMPARACION DE VELOCIDAD MAYOR A 0
   print("\n\n--DATOS DE TIEMPO--\n")

   if VELOCIDAD > 0:
      DISTANCIA = MINIMA
      TIEMPO = DISTANCIA/VELOCIDAD
      print("TIEMPO APROXIMADO EN HORAS.MINUTOS:", TIEMPO)
   else:
      return print("\n\n**LA VELOCIDAD DEBE SER MAYOR A CERO**\n DATOS NO VALIDOS: ", VELOCIDAD)



 
 #COMPARACIÓN PARA MOSTRAR LA RUTA FINAL:
   print("\n\n--DATOS DE RUTA--\n")

   if(MINIMA>0 and MINIMA==P1):
      print("LA MEJOR RUTA ES: ", list(enumerate(RF1)))
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R1),"KM")
      REGRESO = list(enumerate(RF1[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)
   
   elif(MINIMA>0 and MINIMA == P2):
      print("LA MEJOR RUTA ES: ", RF2)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R2),"KM")
      REGRESO = list(enumerate(RF2[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)
   
   elif(MINIMA>0 and MINIMA == P3):
      print("LA MEJOR RUTA ES: ", RF3)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R3),"KM")
      REGRESO = list(enumerate(RF3[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P4):
      print("LA MEJOR RUTA ES: ", RF4)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R4),"KM")
      REGRESO = list(enumerate(RF4[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P5):
      print("LA MEJOR RUTA ES: ", RF5)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R5),"KM")
      REGRESO = list(enumerate(RF5[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P6):
      print("LA MEJOR RUTA ES: ", RF6)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R6),"KM")
      REGRESO = list(enumerate(RF6[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P7):
      print("LA MEJOR RUTA ES: ", RF7)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R7),"KM")
      REGRESO = list(enumerate(RF7[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P8):
      print("LA MEJOR RUTA ES: ", RF8)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R8),"KM")
      REGRESO = list(enumerate(RF8[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P9):
      print("LA MEJOR RUTA ES: ", RF9)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R9),"KM")
      REGRESO = list(enumerate(RF9[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P10):
      print("LA MEJOR RUTA ES: ", RF10)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R10),"KM")
      REGRESO = list(enumerate(RF10[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)

   
   elif(MINIMA>0 and MINIMA == P11):
      print("LA MEJOR RUTA ES: ", RF11)
      print("TOTAL DE KILIMETROS POR RECORRER: ", sum(R11),"KM")
      REGRESO = list(enumerate(RF11[::-1]))
      print("\nSI DESEA REGRESAR EN SU PUNTO DE PARTIDA TOME ESTA RUTA: ",REGRESO)


   else:
      return print("**ERROR DE VALORES, NO SE PUEDE CALCULAR LA RUTA**\n Datos no validos: ",MINIMA )

      


#SALIR O INTERNAR

   SALIR=str(input("DESEA CONTINUAR 'SI' O 'NO' \n"))
   
   if SALIR in ['si', 'SI' , 'Si' , 's', '']:
      ruta()
   else:
      exit()



#FORMULA PARA CALCULAR TIEMPO t=d/v
#FORMULA PARA CALACULAR DISTANCIA d=v*t
