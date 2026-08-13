from email_validator import validate_email, EmailNotValidError
from validate_docbr import CPF
import json
import re

clientes = []
validator = CPF()

def cadastrar_cliente():
    print("\n" + "=" * 35)
    print("         CADASTRO DE CLIENTE")
    print("=" * 35)

    # 1. VALIDAÇÃO DO NOME (Suporta acentos e espaços)
    while True:
        nome = input("Digite o nome do cliente: ").strip().title()
        if not nome:
            print("O nome não pode estar vazio. Por favor, digite um nome válido.")
            continue
        # regex permite letras, acentos, cecidilha e espaços
        if not re.match(r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s]+$", nome):
            print("O nome deve conter apenas letras e espaços. Por favor, digite um nome válido.")
            continue
        break

    # 2. VALIDAÇÃO DO CPF (Limpeza imediata antes dos testes)
    while True:
        cpf_input = input("Digite o CPF do cliente (somente números): ").strip()
        cpf_limpo = "".join(filter(str.isdigit, cpf_input))  # Limpa o input imediatamente
        
        if not validator.validate(cpf_limpo):
            print("CPF inválido. Por favor, digite um CPF válido.")
            continue
        if any(cliente['cpf'] == cpf_limpo for cliente in clientes):
            print("Este CPF já está cadastrado. Por favor, digite um CPF diferente.")
            continue
        break
        

    # 3. VALIDAÇÃO DO E-MAIL (Unificada em um único laço)
    while True:
        email = input("Digite o e-mail do cliente: ").strip().lower()
        try:
            infomacoes_email = validate_email(email, check_deliverability=True)
            email_valido = infomacoes_email.email  # Normaliza o e-mail   
            break
        except EmailNotValidError:
            print("E-mail inválido. Por favor, digite um e-mail válido.")

    # 4. SALVANDO OS DADOS
    cliente = {
        "nome": nome,
        "cpf": cpf_limpo,
        "email": email_valido
    }

    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")

def listar_clientes():
    print("\n" + "=" * 35)
    print("         LISTA DE CLIENTES")
    print("=" * 35)
    # Verificando se há clientes cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    # Listando os clientes cadastrados
    for i, cliente in enumerate(clientes, start=1):
        # Formatando a exibição para ficar mais organizada visualmente
        cpf_formatado = validator.mask(cliente["cpf"])
        print(f"{i}. Nome: {cliente['nome']} | CPF: {cpf_formatado} | E-mail: {cliente['email']}")

def salvar_clientes_em_arquivo():
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)
    print("Clientes salvos em 'clientes.json' com sucesso!")

def carregar_clientes_de_arquivo():
    global clientes
    try:
        with open("clientes.json", "r") as arquivo:
            clientes = json.load(arquivo)
        print("Clientes carregados de 'clientes.json' com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'clientes.json' não encontrado. Nenhum cliente foi carregado.")
