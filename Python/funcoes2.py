def isPar(numero):

    return numero %2 == 0
   
def main():

    valor = int(input("Digite um numero: "))

    if isPar(valor):
        print("Par")
    else:
        print("Impar") 

main()