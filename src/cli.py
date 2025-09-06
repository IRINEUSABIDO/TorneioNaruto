from options import *

def main():

    options = {
    "1": default,
    "2": custom,
    "3": customDefault,
    "4": cli
    }

    # interface
    while True:
        print("")
        print("1. padrao")
        print("2. customizado")
        print("3. customizado ( padrao )")
        print("4. interface ")
        print("5. sair")
        optionInput = input(": ")
        print("")

        if optionInput == "5":
            print("saindo...")
            break

        elif optionInput in options:
            options[optionInput]()

        else:
            continue



if __name__ == "__main__":
  main()
