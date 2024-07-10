# Função para adicionar um contato à agenda
def adicionar_contato(agenda):
    print("Informe os dados do contato:")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    
    # Criando um dicionário com os dados do contato
    contato = {
        'nome': nome,
        'endereco': endereco,
        'telefone': telefone
    }
    
    # Adicionando o contato à agenda
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!\n")

# Função principal do programa
def main():
    agenda = []  # Lista vazia para armazenar os contatos
    
    while True:
        # Opções para o usuário
        print("1 - Adicionar novo contato")
        print("2 - Encerrar e mostrar lista de contatos")
        opcao = input("Escolha uma opção (1/2): ")
        
        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            # Mostrar a lista de contatos e encerrar o programa
            print("\n=== Lista de Contatos ===")
            for contato in agenda:
                print(f"Nome: {contato['nome']}, Endereço: {contato['endereco']}, Telefone: {contato['telefone']}")
            break
        else:
            print("Opção inválida. Escolha 1 ou 2.\n")
    
    print("Programa encerrado.")

# Chamando a função principal para executar o programa
if __name__ == "__main__":
    main()