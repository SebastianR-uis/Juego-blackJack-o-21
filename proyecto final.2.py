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

print("####### !Inicia el juego! #######")
print("")
                                                                                #DEFINIR SI SE VA A COMENZAR CON EL JUEGO 
while True:
    partida = input("¿Comenzar nueva partidao?, copiar si o no: \n-")
    partida.strip()
    if partida == "no":
        print("Adios mmgv glu glu glu")                                          #ACABA CON EL JUEGO
        break
    else: 
                                                                                #CONTINUA CON EL JUEGO
        jugadores = int(input("Cuantos jugadores quiere jugar:\n-"))            #PIDE EL NUMERO DE JUGADORES
        for m in range(jugadores):                                              #CICLO FOR POR LA CANTIDAD DE JUGADORES
            print("")
            print("\n")
            Baraja_cartas = repartir_cartas(jugadores)                          #LLAMA A LA FUNCION EN LA VARIABLE JUGADORES
            print(Baraja_cartas)
            suma_total = sum(Baraja_cartas)                                     #SUMA DE LAS PRIMERAS 2 CARTAS
            print(suma_total)

            if 0 in Baraja_cartas:                                              #REEMPLAZA EL A POR UN NUMERO EN LAS PRIMERAS 2 CARTAS
                print(f"A esta en tus cartas, si A = 11 entonces:", (suma_total+11), "o si A = 1 entonces:", (suma_total + 1))
                if (suma_total + 11) >= 21:                                     #SOLAMENTE SI LA SUMA DE LAS CARTAS ES MAYOR O IGUAL A 21
                    A=int(input("valor de A 1 o 11:\n- "))
                    if A==1:
                        y=1
                        suma_total+=y
                        print(f"\n el total es {suma_total}")
                        Baraja_cartas.remove(0)
                        Baraja_cartas.append(y)
                        print([Baraja_cartas])
                        print(suma_total)
                    else:
                        y=11
                        suma_total+=y
                        Baraja_cartas.remove(0)
                        Baraja_cartas.append(y)
                        print([Baraja_cartas])
                        print(suma_total)
########################################### PRIMERAS 2 CARTAS #######################################################################      


########################## CARTAS ENTREGADAS POR LA CASA ######################################################################

            while True: 
                                                                            #CONTINUAR CON EL JUEGO O PLANTARSE
                n=int(input("Seleccione 1 para tomar o 2 para plantar: \n-"))
                if n==1:                                                            #Si selecciona 1, se continua el codigo
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
                            
                    for y in Baraja_cartas:                                             #REEMPLAZA LAS LETRAS POR NUMEROS EN EL VECTOR
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
                        suma=suma+y
                        print(suma)

                    #BUSCAR LAS A DENTRO DEL VECTOR Y DEFINIR SU VALOR
                    if 0 in Baraja_cartas:           
                        print(f"A esta en tus cartas, si A = 11 entonces:", (suma+11), "o si A = 1 entonces:", (suma + 1))
                        if (suma_total + 11) >= 21: #SOLAMENTE OPERA SI LA SUMA ES MAYOR A 21
                            A=int(input("valor de A 1 o 11:\n- "))
                            if A==1:
                                y=1
                                suma_total+=y
                                print(f"\n el total es {suma_total}")
                                Baraja_cartas.remove(0)
                                Baraja_cartas.append(y)
                                print([Baraja_cartas])
                            else:
                                y=11
                                suma_total+=y
                                Baraja_cartas.remove(0)
                                Baraja_cartas.append(y)
                                print([Baraja_cartas])

                    print(Baraja_cartas)
                    suma=sum(Baraja_cartas) 
                    print(suma)
                    

                    if suma > 21:
                        print(f"{suma} Volaste")
                        break

                else:
                    break
                if suma > 21:
                    print(f"{suma}Volaste")
                    break