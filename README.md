# Password Strength Checker

Um mini-projeto em Python que verifica a força de uma senha e se ela já foi comprometida em vazamentos de dados, utilizando a API do [Have I Been Pwned](https://haveibeenpwned.com/).

---

## O Que Este Projeto Faz

- Verifica a força de uma senha:
  - Tamanho mínimo
  - Presença de letras maiúsculas, minúsculas, números e símbolos
- Consulta se a senha foi vazada usando a API pública do Have I Been Pwned
- Gera uma saída clara no terminal

---

## Conceitos Python Praticados

- Manipulação de strings
- Requisições HTTP com a biblioteca `requests`
- Condicionais e loops
- Tratamento de erros
- Hashing com `hashlib`
- Interface em linha de comando com `argparse`
- Cores no terminal com `colorama` ou `termcolor`

---

## Requisitos

- Python 3.7+
- Bibliotecas:
  - `requests`
  - `colorama`

Instale as dependências com:

```bash
pip install -r requirements.txt
