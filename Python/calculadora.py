x=input("digite o valor 1 = ")
y=input("digite o valor 2 = ")
"""print (int(x)+ int(y))"""# inteiro
print(round(float(x)/float(y),2))#round(numero,decimais) essa função transforma o numero em 2 casas decimais
##########################
valor= int(x)+ int(y)
print(f"{valor:,}")#formatar a saída (:,) é um tipo de formato no python que exibe o numero 1,000
