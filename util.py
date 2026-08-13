import os
def clear_screen():
    # Limpa a tela do terminal de acordo com o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    # Pausa a execução do programa até que o usuário pressione Enter
    input("\nPressione Enter para continuar...")
def error_message(message):
    # Exibe uma mensagem de erro formatada
    print(f"\n[ERRO] {message}")
def success_message(message):
    # Exibe uma mensagem de sucesso formatada
    print(f"\n[SUCCESSO] {message}")