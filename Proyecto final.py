import random as rnd

def repartir_cartas(cartas):
    TusCartas=[]
    ###EMPEZAR EL JUEGO, PRIMERAS 2 CARTAS.###
    for i in range(2):
        if i == 0:
            print(f"Pimera carta jugador {m + 1}:")
        if i == 1:
            print(f"Segunda carta jugador {m + 1}:")
        x=rnd.choice(baraja)
        y=rnd.choice(x)
        x.remove(y)    
        #ME IMPRIME LOS PALOS DE LAS CORRESPONDIENTES CARTAS QUE SALEN
        if x == corazones:
            print(f"{y} de corazones")
        if x == picas:
            print(f"{y} de picas")
        if x == treboles:
                print(f"{y} de treboles")
        if x == diamantes:
            print(f"{y} de diamantes") 
        TusCartas.append(y)  
        
    #Reemplaza las letras en el vector por numeros para operar con ellos    
        for y in TusCartas:    
            if y=='J':
                TusCartas.remove("J")
                y=10
                TusCartas.append(y)
            if y=='K':
                TusCartas.remove("K")
                y=10
                TusCartas.append(y)
            if y=='Q':
                TusCartas.remove("Q")
                y=10
                TusCartas.append(y)
            if y == 'A':
                TusCartas.remove("A")
                y = 0
                TusCartas.append(y)

    return TusCartas

#LOS PALOS Y SUS CORRESPONDIENTES CARTAS
corazones =[2,3,4,5,6,7,8,9,"J","K","Q","A"]
picas=[2,3,4,5,6,7,8,9,"J","K","Q","A"]
diamantes=[2,3,4,5,6,7,8,9,"J","K","Q","A"]
treboles=[2,3,4,5,6,7,8,9,"J","K","Q","A"]
baraja=[corazones, picas, diamantes, treboles]

suma=0
Baraja_cartas = []
suma_total = []
PUNTAJE_FINAL=[]


print("####### !Inicia el juego! #######")
print("")
                                                                                #DEFINIR SI SE VA A COMENZAR CON EL JUEGO 
while True:
    partida = input("¿Comenzar nueva partida?, copiar si o no: \n-")
    partida.strip()
    if partida == "no":
        print("Adios mmgv glu glu glu")                                          #ACABA CON EL JUEGO
        break
    else: 
                                                                                #CONTINUA CON EL JUEGO
        jugadores = int(input("Cuantos jugadores van a jugar:\n-"))             #PIDE EL NUMERO DE JUGADORES
        for m in range(jugadores):                                              #CICLO FOR POR LA CANTIDAD DE JUGADORES
            print("")
            print("\n")
            Baraja_cartas = repartir_cartas(jugadores)                          #LLAMA A LA FUNCION EN LA VARIABLE JUGADORES
            print(Baraja_cartas)                                                #IMPRIME LA MANO
            suma_total = sum(Baraja_cartas)                                     #SUMA DE LAS PRIMERAS 2 CARTAS
            print(suma_total)


######################################### CASO EN EL QUE LA CARTA SEA UNA A ##############################################
            if 0 in Baraja_cartas:                                            #REEMPLAZA EL A POR UN NUMERO 0 EN LAS PRIMERAS 2 CARTAS
                print(f"A esta en tus cartas, si A = 11 entonces:", (suma_total+11), "o si A = 1 entonces:", (suma_total + 1))
                definir=int(input("\n Desea definir el valor de A ahora?  ---> 1 = Si     2 = No"))
                if definir == 1:
                    A=int(input("Decida el valor de A: 1 o 11:\n- "))
                    if A==1:
                        y=1
                        suma_total+=y                                         #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                        print(f"\n el total es {suma_total}")                 #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                        Baraja_cartas.remove(0)                               #REMUEVE EL 0 TEMPORAL DEL VECTOR
                        Baraja_cartas.append(y)                               #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                        print(Baraja_cartas)                                  #IMPRIME LA MANO
                    else:
                        y=11
                        suma_total+=y                                         #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                        print(f"\n el total es {suma_total}")                 #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                        Baraja_cartas.remove(0)                               #REMUEVE EL 0 TEMPORAL DEL VECTOR
                        Baraja_cartas.append(y)                               #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                        print(Baraja_cartas)                                #IMPRIME LA MANO             
                
                if 0 in Baraja_cartas:                                        #ESTO ES PARA COMPROBAR SI DESPUES DE DEFINIR EL VALOR DE A ARRIBA, TODAVIA EXISTE OTRA A Y ASI EVITAR REPETIR ESTO
                    if (suma_total + 11) >= 21:                               #SOLAMENTE SI LA SUMA DE LAS CARTAS ES MAYOR O IGUAL A 21
                        A=int(input("Decida el valor de A: 1 o 11:\n- "))     #PIDE DEFINIR EL VALOR DE LA A CON EL FIN DE TERMINAR O CONTINUAR LA PARTIDA
                        if A==1:
                            y=1
                            suma_total+=y                                     #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                            print(f"\n el total es {suma_total}")             #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                            Baraja_cartas.remove(0)                           #REMUEVE EL 0 TEMPORAL DEL VECTOR
                            Baraja_cartas.append(y)                           #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                            print(Baraja_cartas)                              #IMPRIME LA MANO
                            print(suma_total)                                 #IMPRIME EL VALOR TOTAL ACTUAL
                        else:
                            y=11
                            suma_total+=y                                     #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                            print(f"\n el total es {suma_total}")             #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                            Baraja_cartas.remove(0)                           #REMUEVE EL 0 TEMPORAL DEL VECTOR
                            Baraja_cartas.append(y)                           #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                            print(Baraja_cartas)                              #IMPRIME LA MANO
                            print(suma_total)                                 #IMPRIME EL VALOR TOTAL ACTUAL
                print(sum(Baraja_cartas))

##############################################################################################################################    


########################## CARTAS ENTREGADAS POR LA CASA ######################################################################

            while True: 
                                                                                    #CONTINUAR CON EL JUEGO O PLANTARSE
                n=int(input("Seleccione 1 para tomar o 2 para plantar: \n-"))
                if n==1:                                                            #SI SELECCIONA 1, SE CONTINUA CON EL CODIGO
                    x=rnd.choice(baraja)                                            #entra a las baraja y selecciona un palo
                    y=rnd.choice(x)                                                 #Entra al palo y selecciona una carta
                    x.remove(y)                                                     #Quita la carta para que no se repita
                    Baraja_cartas.append(y)
                    
                    if x==corazones:                                                #IMPRIME LOS PALOS DE LAS RESPECTIVAS CARTAS
                        print("")
                        print(f"{y} de corazones")
                    if x==picas:
                        print("")
                        print(f"{y} de picas")    
                    if x==treboles:
                        print("")
                        print(f"{y} de treboles")
                    if x==diamantes:
                        print("")
                        print(f"{y} de diamantes")                             
                    for y in Baraja_cartas:                                         #REEMPLAZA LAS LETRAS POR NUMEROS EN EL VECTOR
                        if y=='J':
                            Baraja_cartas.remove("J")
                            y=10
                            Baraja_cartas.append(y)
                        if y=='K':
                            Baraja_cartas.remove("K")
                            y=10
                            Baraja_cartas.append(y)
                        if y=='Q':
                            Baraja_cartas.remove("Q")
                            y=10
                            Baraja_cartas.append(y)
                        if y == 'A':
                            Baraja_cartas.remove("A")
                            y = 0
                            Baraja_cartas.append(y)
                    suma_total+=y


                    ################# CASO EN EL QUE LA CARTA SEA UNA A ##############################################   
                    if 0 in Baraja_cartas:                    #REEMPLAZA EL A POR UN NUMERO 0 EN LAS PRIMERAS 2 CARTAS      
                        print(f"A esta en tus cartas, si A = 11 entonces:", (suma_total+11), "o si A = 1 entonces:", (suma_total + 1)) # IMPRIME LA SUMA DE LA A EN AMBOS CASOS DE LOS VALORES DE A
                        definir=int(input("\n Desea definir el valor de A ahora?  ---> 1 = Si     2 = No: \n-")) #ESTO ES PARA DEFINIR EL VALOR DE A SI EL JUGADOR LO QUIERE ASI
                        if definir == 1:                                            
                            A=int(input("Decida el valor de A: 1 o 11:\n- "))      
                            if A==1:
                                y=1
                                suma_total+=y                                   #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                                print(f"\n el total es {suma_total}")           #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                                Baraja_cartas.remove(0)                         #REMUEVE EL 0 TEMPORAL DEL VECTOR
                                Baraja_cartas.append(y)                         #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                                print(Baraja_cartas)                            #IMPRIME LA MANO
                            else:
                                y=11
                                suma_total+=y                                   #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                                print(f"\n el total es {suma_total}")           #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                                Baraja_cartas.remove(0)                         #REMUEVE EL 0 TEMPORAL DEL VECTOR
                                Baraja_cartas.append(y)                         #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                                print(Baraja_cartas)                            #IMPRIME LA MANO

                        if 0 in Baraja_cartas:                                  #ESTO ES PARA COMPROBAR SI DESPUES DE DEFINIR EL VALOR DE A ARRIBA, TODAVIA EXISTE OTRA A Y ASI EVITAR REPETIR ESTO
                            if (suma_total + 11) >= 21:                         #SOLAMENTE OPERA SI LA SUMA ES MAYOR A 21
                                A=int(input("Decida el valor de A: 1 o 11:\n- "))#PIDE DEFINIR EL VALOR DE LA A CON EL FIN DE TERMINAR O CONTINUAR LA PARTIDA
                                if A==1:
                                    y=1
                                    suma_total+=y                               #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                                    print(f"\n el total es {suma_total}")       #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                                    Baraja_cartas.remove(0)                     #REMUEVE EL 0 TEMPORAL DEL VECTOR
                                    Baraja_cartas.append(y)                     #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                                    print([Baraja_cartas])                      #IMPRIME LA MANO
                                else:
                                    y=11
                                    suma_total+=y                               #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                                    print(f"\n el total es {suma_total}")       #iMPRIME EL VALOR TOTAL DE LAS CARTAS EN LA MANO 
                                    Baraja_cartas.remove(0)                     #REMUEVE EL 0 TEMPORAL DEL VECTOR
                                    Baraja_cartas.append(y)                     #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                                    print(Baraja_cartas)                      #IMPRIME LA MANO

                    #######################################################################################################


                    print(Baraja_cartas)                                           #IMPRIME LA MANO CORRESPONDIENTE DEL JUGADOR
                    suma=sum(Baraja_cartas)                                        #SUMA EL VALOR DE LAS CARTAS
                    print(suma)
                    

                    if suma > 21:                                                  #TERMINA EL TURNO DEL JUGADOR SI SE PASA DE 21
                        print(f"{suma} Volaste")                                   #IMPRIME EL PUNTAJE 
                        PUNTAJE_FINAL.append(suma)                                 #GUARDA EL VALOR DEL PUNTAJE Y TERMINA EL TURNO 
                        break

                else:                                                              #ESTE ES EL CASO EN EL QUE SE DECIDA PLANTARSE
                    suma=sum(Baraja_cartas)
                    if 0 in Baraja_cartas:                                         #SI AL PLANTARSE EXISTE UNA A EN LAS CARTAS            
                        print(f"A esta en tus cartas, si A = 11 entonces:", (suma_total+11), "o si A = 1 entonces:", (suma_total + 1))# IMPRIME LA SUMA DE LA A EN AMBOS CASOS DE LOS VALORES DE A
                        A=int(input("Decida el valor de A: 1 o 11:\n- "))          #PIDE DEFINIR EL VALOR DE LA A CON EL FIN DE TERMINAR O CONTINUAR LA PARTIDA
                        if A==1:
                            y=1
                            suma_total+=y                                           #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                            Baraja_cartas.remove(0)                                 #REMUEVE EL 0 TEMPORAL DEL VECTOR
                            Baraja_cartas.append(y)                                 #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                            suma=sum(Baraja_cartas)                                 #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                            print("El marcador final fue", suma)                    #IMPRIME EL MARCADOR
                            PUNTAJE_FINAL.append(suma)                              #GUARDA EL PUNTAJE FINAL
                            
                        else:
                            y=11
                            suma_total+=y                                           #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                            Baraja_cartas.remove(0)                                 #REMUEVE EL 0 TEMPORAL DEL VECTOR
                            Baraja_cartas.append(y)                                 #REEMPLAZA EL VALOR ESCOGIDO POR EL JUGADOR EN EL VECTOR
                            suma=sum(Baraja_cartas)                                 #SUMA EL VALOR QUE FUE ESCOGIDO POR EL JUGADOR AL TOTAL
                            print("El marcador final fue", suma)                    #IMPRIME EL MARCADOR
                            PUNTAJE_FINAL.append(suma)                              #GUARDA EL PUNTAJE FINAL

#########################################################################################################################   
#  
                    else:                                                           #SI NO HAY UN CERO EN LA BARAJA ENTONCES:
                        print("El marcador final fue", suma)                        #IMPRIME EL MARCADOR
                        PUNTAJE_FINAL.append(suma)                                  #GUARDA EL PUNTAJE FINAL
                        break
                    
                if suma > 21:                                                       #COMPRUEBA SI LA SUMA DE LAS CARTAS ES MAYOR A 21
                    print(f"{suma}Volaste \n ")                                     #SI ES ASI, IMPRIME VOLASTE Y TERMINA EL JUEGO
                    PUNTAJE_FINAL.append(suma)                                      #GUARDA EL PUNTAJE FINAL
                    break


##################   COMPARAR PUNTAJES Y DECIDIR EL GANADOR  ##################################                    
    print(PUNTAJE_FINAL)
    for i in range(len(PUNTAJE_FINAL)):
        if PUNTAJE_FINAL[i] >21:
            print(f"jugador {i+1} : {PUNTAJE_FINAL[i]}  !PERDIO!")
        if PUNTAJE_FINAL[i] <=21:
            print(f"jugador {i+1} : {PUNTAJE_FINAL[i]}  !POSIBLE GANADOR!")
        if PUNTAJE_FINAL[i] ==21:
            print(f"jugador {i+1} : {PUNTAJE_FINAL[i]} !PUNTAJE PERFECTO!")

    print("Con mucho esfuerzo de parte de:\n Andres Santiago Martinez \n Juan Pablo Alvarez \n Sebastian Andres Reyes \n :D \n Vuelva pronto")
    break
