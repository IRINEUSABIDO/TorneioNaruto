import random

def default():
    players = ["alex","murilo","victor","ivan","pedro arthur", "apolo", "pedro henrique", "luis andre"]
    random.shuffle(players)
    numero = 1

    for x in range(0, len(players), 2):
        print(f"Partida {numero}")
        print(f"{players[x]} vs {players[x + 1]} \n")
        numero += 1

def custom():
    players = []

    while True:
        player = input("digita o nome da lenda ('end' pra terminar):  ")
        if player == "end":
            print("")
            break
        elif player == "":
            print("digita um nome bro")

        players.append(player)

    random.shuffle(players)
    numero = 1

    if len(players) <= 2 :
        print("pq bro bota mais gente ai")
        return 0

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
        player = input("digita o nome da lenda ('end' pra terminar):  ")

        if player == "end":
            print("")
            break
        elif player in players:
            print("essa lenda ai ja ta na lista\n")
            continue
        else:
            players.append(player)

    random.shuffle(players)
    numero = 1

    for x in range(0, len(players), 2):
        print(f"Partida {numero}")

        try:
            print(f"{players[x]} vs {players[x + 1]} \n")

        except IndexError:
            print(f"{players[-1]} vs quem perdeu na ultima")

        numero += 1
