# Password Strength Checker

Um verificador de força de senhas em Python que analisa a segurança de senhas, verifica se foram comprometidas em vazamentos de dados usando a API do [Have I Been Pwned](https://haveibeenpwned.com/), e inclui um gerador de senhas seguras.

---

## Funcionalidades

### Verificação de Força da Senha
- Verifica tamanho mínimo (8 caracteres)
- Presença de letras maiúsculas
- Presença de letras minúsculas
- Presença de números
- Presença de caracteres especiais
- Classificação em: Muito Fraca, Fraca, Média, Forte

### Verificação de Vazamentos
- Consulta a API Have I Been Pwned
- Usa hash SHA-1 para proteção da senha
- Informa quantas vezes a senha foi encontrada em vazamentos

### Gerador de Senhas Seguras
-  Gera senhas aleatórias criptograficamente seguras
-  Comprimento personalizável (mínimo 8 caracteres)
-  Opção de incluir/excluir símbolos especiais
-  Garante presença de todos os tipos de caracteres

###  Interface Colorida
-  Saída colorida no terminal
-  Indicadores visuais (✅/❌)
-  Cores para diferentes níveis de segurança

---

## Conceitos Python Praticados

- Manipulação de strings e expressões regulares
- Requisições HTTP com a biblioteca `requests`
- Condicionais e loops
- Tratamento de erros e exceções
- Hashing criptográfico com `hashlib`
- Geração segura de números aleatórios com `secrets`
- Interface em linha de comando com `argparse`
- Cores no terminal com `colorama`
- Funções e modularização do código
- Documentação com docstrings

---

## Requisitos

- Python 3.7+
- Bibliotecas:
  - `requests`
  - `colorama`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## Como Usar

### Verificar uma Senha Específica

```bash
python passwordStrengthChecker.py --password "MinhaSenh@123"
```

### Gerar uma Senha Segura

```bash
# Gerar senha padrão (12 caracteres com símbolos)
python passwordStrengthChecker.py --generate

# Gerar senha com 16 caracteres
python passwordStrengthChecker.py --generate --length 16

# Gerar senha sem símbolos especiais
python passwordStrengthChecker.py --generate --no-symbols

# Gerar senha de 10 caracteres sem símbolos
python passwordStrengthChecker.py --generate --length 10 --no-symbols
```

### Obter Ajuda

```bash
python passwordStrengthChecker.py --help
```

---

## Exemplo de Saída

```
==================================================
ANÁLISE DE SEGURANÇA DA SENHA
==================================================

Tamanho: 12 caracteres

Critérios de segurança:
Letras maiúsculas: Sim
Letras minúsculas: Sim
Números: Sim
Caracteres especiais: Sim

Força da senha: Forte

Verificando vazamentos de dados...
Boa notícia: Esta senha não foi encontrada em vazamentos conhecidos.
```

---

## Segurança e Privacidade

**Sua senha nunca é enviada completa para a internet!**

O programa usa a técnica k-Anonymity da API Have I Been Pwned:
1. Cria um hash SHA-1 da sua senha
2. Envia apenas os **primeiros 5 caracteres** do hash
3. Recebe uma lista de hashes que começam com esses 5 caracteres
4. Compara localmente para ver se sua senha está na lista

Isso significa que o Have I Been Pwned nunca recebe sua senha real!

---

## Estrutura do Código

- `check_password_strength(password)`: Analisa a força da senha
- `check_pwned_password(password)`: Verifica vazamentos usando API
- `generate_secure_password(length, include_symbols)`: Gera senhas seguras
- `print_password_analysis(password)`: Exibe análise completa formatada
- `main()`: Função principal com interface de linha de comando

---
