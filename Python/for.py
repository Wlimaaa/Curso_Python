personagens=["Frodo", "Sam", "Legolas","Gandalf","Ginly","Smeagol"]

print(personagens[2])

print(personagens)

print("Lista fixa...")
for i in range(4):
    print("Nome:", personagens[i], end="\n")
print("Lista Dinâmica...")
for personagem in personagens:
    print("Nome:",personagem)