nome = input("Digite o persongem: ")

match nome:

    case "Frodo" | "Legolas":
        print("Hobbit")
    case "Sam":
        print("Hobbit")
    case"Aragorn":
        print("Homem")
    case "Gandalf":
        print("Mago")
    case _:
        print("Quem?")