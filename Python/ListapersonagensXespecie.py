personagens=["Frodo", "Sam", "Legolas","Gandalf","Ginly","Smeagol","Bilbo"]
especies=["Hobbit","Hobbit","Elfo","Mago","Anão", "Hobbit", "Hobbit"]


print("Lista fixa")
for i in range(7):
    print("Nome: ", personagens[i] ,"x","Espécie:", especies[i])
    
print("Lista dinâmica")# a range len torna a tabela dinâmica
for i in range(len(personagens)):
    print("Nome: ", personagens[i] ,"x","Espécie:", especies[i])