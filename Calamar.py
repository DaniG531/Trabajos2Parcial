import random
PlayerMarbles = 10
CPUMarbles = 10
Even = False

def CPUWins():
    print(f"El Rival Habia apostado {CPUBet} canicas.")
    print(f"Tú apostaste {PlayerBet} canicas.")
    print(f" - Has perdido {PlayerBet} canicas")
    print("")
    print("=========================================")

def PlayerWins():
    print(f"El Rival Habia apostado {CPUBet} canicas.")
    print(f"Tú apostaste {PlayerBet} canicas.")
    print(f" - Has Ganado {CPUBet} canicas")
    print("")
    print("=========================================")
    

#def EndGame():
    if PlayerMarbles == 20:
        Game = False
        return Game
    if CPUMarbles == 20:
        Game = False
        return Game

print(f"Tienes {PlayerMarbles} Canicas.")
Game = True
Ciclo = True
while Game:
    ### Turno Jugador ###
    print("¿Cuantas Canicas quieres apostar?")
    while Ciclo:
        PlayerBet = int(input())
        if PlayerBet > 0 and PlayerBet <= PlayerMarbles:
            break
        else:
            print("")
            print("La Apuesta No puede ser 0 y debe ser una Cantidad Posible con Tus Canicas.")
            print("")
    
    
    print("")
    if PlayerBet % 2 == 0:    #True = Par
        Even = True           #False = Inpar
    else:
        Even = False

    CPUBet = random.randint(1,CPUMarbles)
    CPUGuess = bool(random.getrandbits(1))
    if CPUGuess == True:
        print("El Rival apostó por Par.")
        if CPUGuess == Even:
            CPUWins()
            PlayerMarbles -= PlayerBet
            CPUMarbles += PlayerBet
        if CPUGuess != Even:
            PlayerWins()
            CPUMarbles -= CPUBet
            PlayerMarbles += CPUBet
    else:
        print("El Rival apostó por Inpar.")
        if CPUGuess == Even:
            CPUWins()
            PlayerMarbles -= PlayerBet
            CPUMarbles += PlayerBet
        if CPUGuess != Even:
            PlayerWins()
            CPUMarbles -= CPUBet
            PlayerMarbles += CPUBet

    print("")
    print(f"Tienes {PlayerMarbles} Canicas.")

    if PlayerMarbles == 20:
        Game = False
        print("")
        print("Ganaste.")
        print("")
        print("=========================================")
    if CPUMarbles == 20:
        Game = False
        print("")
        print("Perdiste.")
        print("")
        print("=========================================")
