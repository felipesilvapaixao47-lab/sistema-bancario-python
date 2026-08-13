# Projeto Sistema Bancário 🏦

Um sistema de simulação bancária desenvolvido em Python para terminal, aplicando conceitos de modularização, persistência de dados em arquivos JSON e validações robustas de documentos e e-mails.

## 🚀 Funcionalidades

- **Cadastro de Clientes:** Validação de nome (letras/acentos), CPF real (usando `validate-docbr`) sem duplicados e e-mail estruturado.
- **Gerenciamento de Contas:** Criação de contas numéricas sequenciais atreladas a um CPF cadastrado.
- **Persistência Automática:** Carregamento e salvamento de dados em arquivos JSON com segurança contra fechamento abrupto.
- **Operações Financeiras:** Estrutura modular preparada para depósitos, saques, transferências e extratos.

## 📦 Tecnologias Utilizadas

- Python 3.x
- [validate-docbr](https://pypi.org) (Validação de CPF)
- [email-validator](https://pypi.org) (Validação e normalização de e-mails)

## 🔧 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install validate-docbr email-validator
   ```

3. Execute o sistema pelo arquivo principal:
   ```bash
   python main.py
   ```
