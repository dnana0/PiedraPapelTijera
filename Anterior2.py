import random
print("PIEDRA PAPEL TIJERA LAGARTO SPOCK \n-Gana quien consiga primero 3 puntos- \n")
elecciones=["piedra", "spock", "papel", "lagarto", "tijera"]
#Esta lista tiene sus valores organizados de tal forma que los dos valores anteriores al elegido, pierden contra el y los dos siguientes le ganan. Habría que repetir la lista en bucle para poder representarlo visualmente.
puntosplayer=0 #La puntuación. Ambos empezamos en 0.
puntoscpu=0
def piedra_papel_tijera(puntosplayer, puntoscpu):
    selec=(input("¿Que vas a jugar? \n")).casefold() #Ponemos el texto en minusculas para que coincida con la lista.
    if selec == "tijeras":   selec="tijera" #para evitar confusiones
    if selec not in elecciones:
        print("No te he entendido") # para cualquier valor introducido que no este en la lista, volvemos a llamar a la función
        piedra_papel_tijera(puntosplayer, puntoscpu)
    selec = elecciones.index(selec) # Usamos las posiciones de la lista como referencia. Con ellas haremos un calculo para ver quien ha ganado
    cpuchoice = elecciones.index(random.choice(elecciones))
    if puntosplayer==2: #Si estamos a un punto de ganar, la CPU hará trampas y cambiará su decisión a una que gana a la nuestra
        cpuchoice = (selec%4)+1
        print("---(La CPU va a hacer trampas)---") #Informamos de cuando hace trampas

    print("\nHas jugado", elecciones[selec])
    print("La CPU ha jugado", elecciones[cpuchoice])
    if selec == cpuchoice: #Si elegimos lo mismo es empate
        print("EMPATE\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu)
    elif selec>cpuchoice and cpuchoice > selec-3 or cpuchoice-selec>2: #Esta formula comprueba si la elección de la CPU esta una o dos posiciones antes en la tabla. Suponiendo que antes de la posición cero vienen la cuatro y la tres (bucle)
        puntosplayer+=1 #Actualizamos puntos
        print("HAS GANADO\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu) #Mostramos el resultado del versus y el marcador
    else: #Cualquier otro caso hemos perdido(La elección de la CPU está una o dos posiciones mas alante en la lista)
        puntoscpu+=1
        print("HAS PERDIDO\nPuntos Jugador: ", puntosplayer, "   Puntos CPU: ", puntoscpu)
    if puntosplayer == 3: #Si conseguimos los tres puntos, ganamos la partida. ESTO NO VA OCURRIR PORQUE LA CPU HARÁ TRAMPAS PARA QUE NO GANEMOS
        print("FELICIDADES, HAS GANADO")
        volver_a_jugar(puntosplayer, puntoscpu)
    elif puntoscpu == 3: #Eventualmente, la CPU siempre ganará porque hace trampas.
        print("HA GANADO LA CPU")
        volver_a_jugar(puntosplayer, puntoscpu) #LLamamos a la función volver a jugar
    else:   piedra_papel_tijera(puntosplayer, puntoscpu)

def volver_a_jugar(puntosplayer, puntoscpu):
    puntosplayer=0 #Ponemos todos los puntos a cero
    puntoscpu=0
    again=input("¿Volver a jugar? s/n")
    if again.casefold()== "s": piedra_papel_tijera(puntosplayer, puntoscpu) #Si quiere volver a jugar, llamamos a la función del juego
    elif again.casefold()== "n":    print("BYE BYE") # Si no quiere volver a jugar, ponemos un mensaje de despedida. Ya no quedará mas codigo que se vaya a ejecutar.
    else: #Si se introduce algún otro valor, llamamos a la función otra vez para volver a preguntar
        print("No te he entendido")
        volver_a_jugar(puntosplayer, puntoscpu)
piedra_papel_tijera(puntosplayer, puntoscpu) # LLamamos a la función del juego por primera vez. Nos traemos los valores de puntuación
