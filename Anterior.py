import random

print("PIEDRA PAPEL TIJERA LAGARTO SPOCK")
print("\n")
elecciones=["piedra", "papel", "tijera", "lagarto", "spock"]

def piedra_papel_tijera():

    selec = (input("¿Que vas a jugar? \n")).casefold()
    print("\n")
    cpuchoice = random.choice(elecciones)

    print("Has jugado", selec)
    print("La CPU ha jugado", cpuchoice)


    match selec.casefold():
        case "piedra":
            if cpuchoice == "piedra":
                print("EMPATE")
            elif cpuchoice == "papel" or cpuchoice == "spock":
                print("HAS PERDIDO")
            elif cpuchoice == "tijera" or cpuchoice == "lagarto":
                print("HAS GANADO")

        case "papel":
            if cpuchoice == "piedra" or cpuchoice == "spock":
                print("HAS GANADO")
            elif cpuchoice == "papel":
                print("EMPATE")
            elif cpuchoice == "tijera" or cpuchoice == "lagarto":
                print("HAS PERDIDO")

        case "tijera":
            if cpuchoice == "piedra" or cpuchoice == "spock":
                print("HAS PERDIDO")
            elif cpuchoice == "papel" or cpuchoice == "lagarto":
                print("HAS GANADO")
            elif cpuchoice == "tijera":
                print("EMPATE")

        case "lagarto":
            if cpuchoice == "piedra" or cpuchoice == "tijera":
                print("HAS PERDIDO")
            elif cpuchoice == "papel" or cpuchoice == "spock":
                print("HAS GANADO")
            elif cpuchoice == "lagarto":
                print("EMPATE")

        case "spock":
            if cpuchoice == "papel" or cpuchoice == "lagarto":
                print("HAS PERDIDO")
            elif cpuchoice == "piedra" or cpuchoice == "tijera":
                print("HAS GANADO")
            elif cpuchoice == "spock":
                print("EMPATE")
                
        case _:
            print("No te he entendido")
            piedra_papel_tijera()
    print("\n")
    volver_a_jugar()


def volver_a_jugar():

    again=input("¿Volver a jugar? s/n")
    if again.casefold()== "s": piedra_papel_tijera()
    elif again.casefold()== "n":
        print("BYE BYE")
    else:
        print("No te he entendido")
        volver_a_jugar()

piedra_papel_tijera() 
    