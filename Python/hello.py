nome = input("Qual é o seu nome? ")# Ler o nome do usuário
nome = nome.strip()# Retirar os espaços caso digite com muitas entradas
nome = nome.capitalize()# Para colocar a primeira letra em maíuscula e demais em minusculas
nome = nome.strip().capitalize()# Escrita dos códigos juntos
nome = nome.strip().title()#Corrige a o nome colocando letra maiuscula na primeira letra do nome, sobrenome USO O TITLE
nome = input("Qual é o seu nome?").strip().title()#Escrever e já apresentar sem espaço e com letra maiuscula (nome e sobrenome)
print(f"Olá," {input("Qual o nome?").strip().title()})#Resumo em uma linha

############################duas variáveis imprime apenas o sobrenome #############################################
nome = input("Qual é o seu nome?").strip().title()
primeiro, sobrenome= nome.split(" ")
print(f"ola,{nome}")
print(sobrenome)
####################################################################################################################

idade = input("Qual é o sua idade? ")# Ler a idade 
print('HELLO, \"AMIGO\"')#Exibir uma mensagem na tela de saudação
print(f"olá, {nome}")#Habilitar o mestre simbol com f na frente e a variável em chaves;

#Para concatenar podemos usar sinal (+) ou (,), sendo que usando a virgular ele já diciona um espaço.
"""imprime um comentário
imprime um comentário várias linhas
"""
#a função print ela utilizada duas ou mais vezes ela pula linha EX: print("ola,") na linha abaixo print("ola,") o codigo irá mostrar ela em duas linhas.
#para usar a função na mesma linha basta usar ( end) Ex: print("hello", end)
#################################################
nome = input("Qual é o seu nome? ")


#nome = nome.strip() #strip executa os espaços de uma string

#nome = nome.capitalize()#transforma a primeira letra em Maiuscula
#nome = nome.strip().title #Quantos espaços estiver eles vai mudar sempre a primeira letra

#imprime uma mensagem na tela

#print("Hello,"  end="")
#print(nome)
#print('Ola, "amigo"')
#print(f"Ola,  {nome}")
#print("Ola," + nome)
primeiro, sobrenome = nome.split(" ")

print(f"Ola, {nome}")
print(sobrenome)