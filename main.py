from banco import menu
from clientes import (
    cadastrar_cliente, 
    carregar_clientes_de_arquivo, 
    listar_clientes, 
    salvar_clientes_em_arquivo  # Importado para salvar ao sair
)
from util import clear_screen

def main():
    # Inicializa carregando os dados salvos anteriormente
    carregar_clientes_de_arquivo()
    input("\nPressione Enter para ir ao menu principal...")  # Pausa inicial opcional

    while True:
        clear_screen()
        opcao = menu()

        if opcao == "0":
            print("\nSalvando dados...")
            salvar_clientes_em_arquivo()  # Garante que os dados não sejam perdidos
            print("Saindo do sistema... Até logo!")
            break
            
        elif opcao == "1":
            cadastrar_cliente()
            input("\nPressione Enter para voltar ao menu...")  # Segura a tela
            
        elif opcao in ["2", "3", "4", "5", "6", "7", "9"]:
            print(f"\n[Aviso] A opção {opcao} funcionou, mas ainda não foi implementada!")
            input("\nPressione Enter para voltar ao menu...")  # Segura a tela
            
        elif opcao == "8":
            listar_clientes()
            input("\nPressione Enter para voltar ao menu...")  # Segura a tela
            
        else:
            print("\nOpção inválida! Por favor, escolha um número do menu.")
            input("\nPressione Enter para tentar novamente...")  # Segura a tela

if __name__ == "__main__":
    main()

