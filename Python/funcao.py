def exibirMensagem():
    print("sou uma função") 
     
def exibirSaudacao(nome):
    print("Olá,",nome)
    print ("O total da soma é", total)
    
def somar(valor1, valor2):
    total = valor1 + valor2
    return total


def main ():    
    exibirMensagem()
    exibirSaudacao("Antonio José")
    print(somar(6,7))
    
main()