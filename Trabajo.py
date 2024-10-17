import random

print("PIEDRA PAPEL TIJERA")
elecciones=["piedra", "papel", "tijera"]
def piedra_papel_tijera():
    selec = (input("¿Que vas a jugar?")).casefold()
    cpuchoice = random.choice(elecciones)
    print("Has jugado", selec)
    print("La CPU ha jugado", cpuchoice)
    match selec.casefold():
        case "piedra":
            if cpuchoice == "piedra":
                print("EMPATE")
            elif cpuchoice == "papel":
                print("HAS PERDIDO")
            elif cpuchoice == "tijera":
                print("HAS GANADO")
        case "papel":
            if cpuchoice == "piedra":
                print("HAS GANADO")
            elif cpuchoice == "papel":
                print("EMPATE")
            elif cpuchoice == "tijera":
                print("HAS PERDIDO")
        case "tijera":
            if cpuchoice == "piedra":
                print("HAS PERDIDO")
            elif cpuchoice == "papel":
                print("HAS GANADO")
            elif cpuchoice == "tijera":
                print("EMPATE")
        case _:
            print("No te he entendido")
            piedra_papel_tijera()
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
    