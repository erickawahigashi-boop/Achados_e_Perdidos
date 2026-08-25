# Código base do projeto

# Função responsável por mostrar o menu
def mostrar_menu():
    print("\n================================")
    print(" ACHADOS E PERDIDOS DA ESCOLA")
    print("================================")
    print("1 - Cadastrar objeto")
    print("2 - Listar objetos")
    print("3 - Excluir objeto")
    print("4 - Sair")


# Função principal do programa
def main():

    # Cria uma lista vazia.
    # Ela será utilizada nas próximas aulas.
    itens = []

    # Mantém o menu funcionando continuamente.
    while True:

        # Mostra o menu.
        mostrar_menu()

        # Pede para o usuário escolher uma opção.
        opcao = input("\nEscolha uma opção: ")

        # Se o usuário escolher 1.
        if opcao == "1":
            print("\nAbrindo cadastro de objeto...")

        # Se o usuário escolher 2.
        elif opcao == "2":
            print("\nMostrando objetos cadastrados...")

        # Se o usuário escolher 3.
        elif opcao == "3":
            print("\nAbrindo exclusão de objeto...")

        # Se o usuário escolher 4.
        elif opcao == "4":
            print("\nPrograma encerrado.")

            # Encerra a repetição.
            break

        # Se o usuário digitar outra coisa.
        else:
            print("\nOpção inválida. Digite 1, 2, 3 ou 4.")


# Inicia o programa
main()
