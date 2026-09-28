from clientes import clientes, salvar_clientes_em_arquivo


def criar_conta():
    print("\n" + "=" * 35)
    print("         CRIAÇÃO DE CONTA")
    print("=" * 35)

    # Busca o cliente pelo CPF
    cpf_pesquisado = input(
        "Digite o CPF do cliente para criar a conta: "
    ).strip()

    cliente_encontrado = None

    for cliente in clientes:
        if cliente["cpf"] == cpf_pesquisado:
            cliente_encontrado = cliente
            print(f"Cliente encontrado: {cliente['nome']}")
            break
    else:
        print(
            "Cliente não encontrado. "
            "Por favor, cadastre o cliente antes de criar uma conta."
        )
        return

    # Escolha do tipo de conta
    tipo_conta = input(
        "Digite o tipo de conta (corrente/poupança): "
    ).strip().lower()

    if tipo_conta not in ["corrente", "poupança"]:
        print(
            "Tipo de conta inválido. "
            "Por favor, escolha 'corrente' ou 'poupança'."
        )
        return

    print(f"Tipo de conta selecionado: {tipo_conta.capitalize()}")

    # Geração do ID da conta
    prefixo = "CO" if tipo_conta == "corrente" else "PO"

    # Conta a quantidade de contas do mesmo tipo desse cliente
    contas_mesmo_tipo = [
        conta
        for conta in cliente_encontrado["contas"]
        if conta["tipo"] == tipo_conta
    ]

    proximo_numero = len(contas_mesmo_tipo) + 1

    # Formatação para 4 dígitos
    id_conta = f"{prefixo}{proximo_numero:04d}"

    # Criação da conta
    nova_conta = {
        "id": id_conta,
        "tipo": tipo_conta,
        "saldo": 0.0
    }

    # Adiciona a conta ao cliente
    cliente_encontrado["contas"].append(nova_conta)

    # Salva no arquivo JSON
    salvar_clientes_em_arquivo()

    print(
        f"\nConta criada com sucesso para o cliente "
        f"{cliente_encontrado['nome']}."
    )
    print(
        f"ID da conta: {id_conta} | "
        f"Tipo: {tipo_conta} | "
        f"Saldo: R${nova_conta['saldo']:.2f}"
    )
def listar_contas():
    print("\n" + "=" * 35)
    print("         LISTA DE CONTAS")
    print("=" * 35)

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"\nCliente: {cliente['nome']} | CPF: {cliente['cpf']}")

        if cliente["contas"]:
            for conta in cliente["contas"]:
                print(
                    f"ID da Conta: {conta['id']} | "
                    f"Tipo: {conta['tipo']} | "
                    f"Saldo: R${conta['saldo']:.2f}"
                )
        else:
            print("Nenhuma conta cadastrada para este cliente.")