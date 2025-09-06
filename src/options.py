import random
import bracket

def default():
    players = ["alex","murilo","victor","ivan","pedro arthur", "apolo", "pedro henrique", "luis andre"]
    random.shuffle(players)
    numero = 1

    for x in range(0, len(players), 2):
        print(f"Partida {numero}")
        print(f"{players[x]} vs {players[x + 1]} \n")
        numero += 1

def custom():
    players = bracket.getPlayers()

    if players != 0:
        random.shuffle(players)
        numero = 1

        for x in range(0, len(players), 2):
            print(f"Partida {numero}")

            try:
                print(f"{players[x]} vs {players[x + 1]} \n")

            except IndexError:
                print(f"{players[-1]} vs quem perdeu na ultima")

            numero += 1

    

def customDefault():
    players = ["alex","murilo","victor","ivan","pedro arthur", "apolo", "pedro henrique", "luis andre"]

    while True:
        player = input(f"digita o nome da lenda ('Q' pra acabar): ")

        if player == "Q":
            print("")
            break
        elif player in players:
            print("essa lenda ai ja ta na lista\n")
            continue
        else:
            players.append(player)

    random.shuffle(players)
    number = 1

    for x in range(0, len(players), 2):
        print(f"Partida {number}")

        try:
            print(f"{players[x]} vs {players[x + 1]} \n")

        except IndexError:
            print(f"{players[-1]} vs quem perdeu na ultima")

        number += 1

def cli():
    bracket.interfaceRun()
    


    