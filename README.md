# 🏦 Sistema Bancário em Python

> Projeto acadêmico e de estudo desenvolvido em Python para praticar lógica de programação, organização de código, validação de dados e persistência em JSON.

## 📌 Sobre o projeto

O **Sistema Bancário em Python** é uma aplicação de terminal criada como parte dos meus estudos em **Análise e Desenvolvimento de Sistemas**.

O projeto está sendo desenvolvido de forma incremental. Nesta etapa, o sistema já permite cadastrar clientes, validar informações, criar contas bancárias vinculadas aos clientes e listar as contas cadastradas.

O objetivo é evoluir a aplicação gradualmente, aplicando novos conceitos de Python à medida que o projeto avança.

## 🚀 Funcionalidades atuais

### 👤 Clientes

- Cadastro de clientes
- Validação de nome
- Validação de CPF
- Verificação de CPF duplicado
- Validação e normalização de e-mail
- Listagem de clientes
- Salvamento e carregamento dos dados em JSON

### 💳 Contas

- Criação de conta vinculada a um cliente
- Busca do cliente por CPF
- Escolha entre conta corrente e conta poupança
- Geração de identificador para a conta
- Saldo inicial de R$ 0,00
- Listagem das contas cadastradas
- Associação de várias contas a um cliente

### 💾 Persistência de dados

Os clientes e suas contas são armazenados localmente em um arquivo JSON.

O arquivo com os dados locais dos clientes não é versionado no GitHub. Ele está protegido pelo `.gitignore` para evitar o envio de informações pessoais utilizadas durante os testes.

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **JSON**
- **Regex**
- **email-validator**
- **validate-docbr**
- **Git e GitHub**

## 📂 Estrutura do projeto

```text
sistema-bancario-python/
│
├── banco.py          # Menu principal
├── main.py           # Controle do fluxo da aplicação
├── clientes.py       # Cadastro, validação e gerenciamento de clientes
├── contas.py         # Criação e listagem de contas
├── operações.py      # Módulo das operações bancárias
├── util.py           # Funções utilitárias
├── README.md         # Documentação do projeto
└── .gitignore        # Arquivos ignorados pelo Git
```

## 🔄 Fluxo atual

```text
Menu principal
      │
      ▼
Cadastro de cliente
      │
      ├── Nome
      ├── CPF
      └── E-mail
      │
      ▼
Cliente cadastrado
      │
      ▼
Criação de conta
      │
      ├── Busca pelo CPF
      ├── Escolha do tipo
      ├── Geração do ID
      └── Saldo inicial = R$ 0,00
      │
      ▼
Conta vinculada ao cliente
      │
      ▼
Listagem de contas
```

## 📚 Conceitos praticados

Este projeto está sendo usado para praticar:

- Variáveis e tipos de dados
- Condicionais
- Estruturas de repetição
- Funções
- Listas
- Dicionários
- `for`, `while`, `break` e `return`
- List comprehensions
- Modularização
- Importação entre módulos
- Manipulação de arquivos
- JSON
- Validação de dados
- Tratamento de erros
- Controle de versão com Git e GitHub

## 💻 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/felipesilvapaixao47-lab/sistema-bancario-python.git
```

### 2. Entre na pasta

```bash
cd sistema-bancario-python
```

### 3. Instale as dependências

```bash
pip install email-validator validate-docbr
```

### 4. Execute o sistema

```bash
python main.py
```

## 🔜 Próximos passos

O projeto ainda está em desenvolvimento.

### Operações bancárias

- [ ] Depósito
- [ ] Saque
- [ ] Transferência
- [ ] Consulta de saldo
- [ ] Extrato

### Melhorias futuras

- [ ] Ampliar as validações
- [ ] Melhorar o tratamento de erros
- [ ] Criar testes automatizados
- [ ] Evoluir a persistência dos dados
- [ ] Melhorar a organização das operações bancárias

## 🎯 Objetivo

Transformar os conhecimentos estudados em Python em uma aplicação prática e evolutiva, documentando o aprendizado por meio de um projeto real no GitHub.

## 👨‍💻 Autor

**Felipe da Silva**

Estudante de **Análise e Desenvolvimento de Sistemas**

Interesses:
- Python
- SQL
- C
- Azure
- Desenvolvimento de Software

## 📈 Status do projeto

🟡 **Em desenvolvimento**

Novas funcionalidades serão implementadas conforme a evolução do projeto.