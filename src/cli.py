from options import *

def main():

    options = {
    "1": default,
    "2": custom,
    "3": customDefault
    }

    # interface
    while True:
        print("")
        print("1. padrao")
        print("2. customizado")
        print("3. customizado ( padrao )")
        print("4. sair")
        optionInput = input(": ")
        print("")

        if optionInput == "4":
            print("saindo...")
            break

        elif optionInput in options:
            options[optionInput]()

        else:
            continue



if __name__ == "__main__":
  main()
