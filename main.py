from options import *
from utils import *

def main():

    options = {
    "1": default,
    "2": custom,
    }

    # cria .json se n tiver
    if readData() == False:
        createData()


    # interface
    while True:
        print("")
        print("1. padrao")
        print("2. customizado")
        print("3. sair")
        optionInput = input(": ")
        print("")

        if optionInput == "3":
            print("saindo...")
            break

        elif optionInput in options:
            options[optionInput]()

        else:
            continue



if __name__ == "__main__":
    main()
