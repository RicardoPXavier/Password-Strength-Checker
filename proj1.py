import argparse
import re
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument("--password",required=True)

args = parser.parse_args()
password = args.password

tem_maiscula = bool(re.search(r'[A-Z]', password))
tem_minuscula = bool(re.search(r'[a-z]', password))
tem_numero =  bool(re.search(r'[0-9]', password))
tem_caractereEspecial = bool(re.search(r'[^A-Za-z0-9]', password))

criterio = sum([tem_maiscula,tem_minuscula,tem_numero,tem_caractereEspecial])
tamanho = len(password)

if len(password) >= 8: # verifica se a senha tem no minimo 8 caracter (quantidade minima segura)
    print(f"Tamanho: {tamanho} caracteres")
    if tem_maiscula:
        print("Possui Maiuscula")
    else:
        print("Não possui Maiuscula")
    if tem_minuscula:
        print("Possui letra Minúscula")
    else:
        print("Não possui letra Minúscula")   
    if tem_numero:
        print("Possui Número")
    else:
        print("Não possui Número")
    if tem_caractereEspecial:
        print("Possui Caractere especial")
    else:
        print("Não possui Caractere especial")
else:
    print("Senha muito pequena, minimo é 8 caracteres")
    exit(0)

if criterio == 4:
    print("Senha: Forte")
elif criterio == 3:
    print("Senha: Média")
else:
    print("Senha: Fraca")

