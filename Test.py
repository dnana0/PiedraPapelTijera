import random #Para la aleatoridad de la CPU

print("PIEDRA PAPEL TIJERA LAGARTO SPOCK \n-Gana quien consiga primero 3 puntos- \n")
elecciones=["piedra", "spock", "papel", "lagarto", "tijera"] #Esta lista tiene sus valores organizados de tal forma que los dos valores anteriores al elegido, pierden contra el y los dos siguientes le ganan. Habría que repetir la lista en bucle para poder representarlo visualmente.
puntosplayer=0 #La puntuación. Ambos empezamos en 0.
puntoscpu=0
trampas=True #Creamos una variable que determinará si la CPU hace trampas o no

def piedra_papel_tijera(puntosplayer, puntoscpu, trampas):
    while puntosplayer < 3 and puntoscpu < 3:
        selec=(input("¿Que vas a jugar? \n")).casefold() #Ponemos el texto en minusculas para que coincida con la lista.
        if selec=="cheatdisable": # Si introducimos un codigo secreto, desactivamos las trampas
            if not(trampas): print("Ya están desactivadas.")
            else:
                trampas=False
                print("Has desactivado las trampas")
        elif selec == "tijeras":   selec="tijera" #para evitar confusiones
        elif selec not in elecciones and selec != "bomba": 
            if selec=="surrender": puntoscpu=3
            else:
                print("No te he entendido") # para cualquier valor introducido que no este en la lista, volvemos a llamar a la función
        elif selec=="bomba": #Un truco que nos permitirá ganar siempre
            if puntosplayer==2 and trampas: print("No hay trampas que puedan con una bomba")
            puntosplayer+=1
            print("HAS GANADO LA RONDA\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu) #Mostramos el resultado del versus y el marcador
        else:
            comparacion(puntosplayer, puntoscpu, trampas, selec)
    if puntosplayer == 3:
        print("\nFELICIDADES, HAS GANADO!!!") #Nuestra victoria
    else:
        print("\nHA GANADO LA CPU") #Victoria de la CPU
    volver_a_jugar(puntosplayer, puntoscpu, trampas) #Ahora que ha terminado la partid, llamamos a la función de volver a jugar

def comparacion(puntosplayer, puntoscpu, trampas, selec):
    """Genera un número aleatorio entre min y max (ambos incluidos).

    Args:
        min (int): El valor mínimo del rango.
        max (int): El valor máximo del rango.

    Returns:
        int: El número aleatorio generado.
        
    >>> 0 <= aleatorio(0, 10) <= 10
    True
    
    >>> 0 <= aleatorio(0, 1000) <= 1000
    True
    """
    selec = elecciones.index(selec) # Usamos las posiciones de la lista como referencia. Con ellas haremos un calculo para ver quien ha ganado
    cpuchoice = elecciones.index(random.choice(elecciones)) # La CPU selecciona un valor aleatorio de la lista
    if puntosplayer==2 and trampas: #Si estamos a un punto de ganar y la opción de trampas está activada, la CPU hará trampas y cambiará su decisión a una que gana a la nuestra.
        if not (selec>cpuchoice and cpuchoice > selec-3 or cpuchoice-selec>2 or cpuchoice==selec): #La CPU va a considerar si le hace falta hacer trampas
            print("(La CPU iba a hacer a trampas pero no le ha hecho falta)")
        else: 
            print("---(La CPU va a hacer trampas)---","\n(Iba a jugar", elecciones[cpuchoice], end=". ")
            cpuchoice = (selec%4)+1
            print("Ha cambiado a", elecciones[cpuchoice], end=")\n") #Aquí mostraremos el cambio de elección que realiza la CPU
        print("\nHas jugado", elecciones[selec])
        print("La CPU ha jugado", elecciones[cpuchoice])
        if selec == cpuchoice: #Si elegimos lo mismo es empate
            print("EMPATE\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu)
        elif selec>cpuchoice and cpuchoice > selec-3 or cpuchoice-selec>2: #Esta formula comprueba si la elección de la CPU esta una o dos posiciones antes en la tabla. Suponiendo que antes de la posición cero vienen la cuatro y la tres (bucle)
            puntosplayer+=1 #Actualizamos puntos
            print("HAS GANADO LA RONDA\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu) #Mostramos el resultado del versus y el marcador
        else: #Cualquier otro caso hemos perdido(La elección de la CPU está una o dos posiciones mas alante en la lista)
            puntoscpu+=1
            print("HAS PERDIDO LA RONDA\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu)                

def volver_a_jugar(puntosplayer, puntoscpu, trampas):
    puntosplayer=0 #Ponemos todos los puntos a cero y volvemos a activar las trampas
    puntoscpu=0
    trampas=True
    again=input("¿Volver a jugar? s/n")
    if again.casefold()== "s": piedra_papel_tijera(puntosplayer, puntoscpu, trampas) #Si quiere volver a jugar, llamamos a la función del juego
    elif again.casefold()== "n":    print("BYE BYE") # Si no quiere volver a jugar, ponemos un mensaje de despedida. Ya no quedará mas codigo que se vaya a ejecutar.
    else: #Si se introduce algún otro valor, llamamos a la función otra vez para volver a preguntar
        print("No te he entendido 1212")
        volver_a_jugar(puntosplayer, puntoscpu, trampas)

piedra_papel_tijera(puntosplayer, puntoscpu, trampas) # Llamamos a la función del juego por primera vez. Nos traemos los valores de puntuación y las trampas