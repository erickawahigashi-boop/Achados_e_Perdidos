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

# ==========================================================
# FUNÇÃO PARA CADASTRAR UM OBJETO
# ==========================================================
def cadastrar_item(itens):
    # Mostra o título da tela de cadastro.
    print("\n--- CADASTRO DE OBJETO ---")
    
    # Solicita os dados do objeto.
    nome = input("Nome do objeto: ")
    descricao = input("Descrição do objeto: ")
    local = input("Local onde foi encontrado: ")
    data = input("Data do registro (dd/mm/aaaa): ")

    # Validação dos campos obrigatórios.
    if nome.strip() == "":
        print("\nO nome do objeto não pode ficar vazio.")
        return
    if descricao.strip() == "":
        print("\nA descrição não pode ficar vazia.")
        return
    if local.strip() == "":
        print("\nO local não pode ficar vazio.")
        return
    if data.strip() == "":
        print("\nA data não pode ficar vazia.")
        return

    # Cria o dicionário com os dados do objeto.
    item = {
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data
    }

    # Adiciona o dicionário à lista de objetos.
    itens.append(item)
    print("\nObjeto cadastrado com sucesso!")
