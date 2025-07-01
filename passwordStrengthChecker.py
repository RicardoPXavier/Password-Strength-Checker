import argparse
import re
import hashlib
import requests
import colorama
import secrets
import string
from colorama import Fore, Style, init

# Inicializa o colorama para cores no terminal
init(autoreset=True)

def check_password_strength(password):
    results = {
        'tamanho': len(password),
        'tem_maiuscula': bool(re.search(r'[A-Z]', password)),
        'tem_minuscula': bool(re.search(r'[a-z]', password)),
        'tem_numero': bool(re.search(r'[0-9]', password)),
        'tem_caractere_especial': bool(re.search(r'[^A-Za-z0-9]', password)),
        'tamanho_adequado': len(password) >= 8
    }
    
    # Calcula a pontuação baseada nos critérios
    criterios = [
        results['tem_maiuscula'],
        results['tem_minuscula'],
        results['tem_numero'],
        results['tem_caractere_especial']
    ]
    results['criterios_atendidos'] = sum(criterios)
    
    # Determina a força da senha
    if not results['tamanho_adequado']:
        results['forca'] = 'Muito Fraca'
        results['cor'] = Fore.RED
    elif results['criterios_atendidos'] == 4:
        results['forca'] = 'Forte'
        results['cor'] = Fore.GREEN
    elif results['criterios_atendidos'] == 3:
        results['forca'] = 'Média'
        results['cor'] = Fore.YELLOW
    else:
        results['forca'] = 'Fraca'
        results['cor'] = Fore.RED
    
    return results

def check_pwned_password(password):
    try:
        # Cria hash SHA-1 da senha
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        
        # Pega os primeiros 5 caracteres do hash
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        # Faz a requisição para a API
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            # Procura o sufixo na resposta
            for line in response.text.splitlines():
                hash_suffix, count = line.split(':')
                if hash_suffix == suffix:
                    return True, int(count)
            return False, 0
        else:
            print(f"{Fore.YELLOW}Aviso: Não foi possível verificar se a senha foi comprometida (Status: {response.status_code})")
            return False, 0
            
    except requests.RequestException as e:
        print(f"{Fore.YELLOW}Aviso: Erro ao conectar com a API: {e}")
        return False, 0
    except Exception as e:
        print(f"{Fore.YELLOW}Aviso: Erro inesperado: {e}")
        return False, 0

def generate_secure_password(length=12, include_symbols=True):
    if length < 8:
        length = 8
    
    # Define os caracteres disponíveis
    chars = string.ascii_letters + string.digits
    if include_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Gera a senha garantindo que tenha pelo menos um de cada tipo
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits)
    ]
    
    if include_symbols:
        password.append(secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Completa o resto da senha
    for _ in range(length - len(password)):
        password.append(secrets.choice(chars))
    
    # Embaralha a senha
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def print_password_analysis(password):
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.CYAN}ANÁLISE DE SEGURANÇA DA SENHA")
    print(f"{Fore.CYAN}{'='*50}")
    
    # Verifica a força da senha
    strength = check_password_strength(password)
    
    print(f"\n{Fore.WHITE}Tamanho: {strength['tamanho']} caracteres")
    
    if not strength['tamanho_adequado']:
        print(f"{Fore.RED}❌ Senha muito pequena! Mínimo recomendado: 8 caracteres")
        return
    
    # Mostra os critérios
    print(f"\n{Fore.WHITE}Critérios de segurança:")
    print(f"{'✅' if strength['tem_maiuscula'] else '❌'} Letras maiúsculas: {'Sim' if strength['tem_maiuscula'] else 'Não'}")
    print(f"{'✅' if strength['tem_minuscula'] else '❌'} Letras minúsculas: {'Sim' if strength['tem_minuscula'] else 'Não'}")
    print(f"{'✅' if strength['tem_numero'] else '❌'} Números: {'Sim' if strength['tem_numero'] else 'Não'}")
    print(f"{'✅' if strength['tem_caractere_especial'] else '❌'} Caracteres especiais: {'Sim' if strength['tem_caractere_especial'] else 'Não'}")
    
    # Mostra a força da senha
    print(f"\n{Fore.WHITE}Força da senha: {strength['cor']}{strength['forca']}{Style.RESET_ALL}")
    
    # Verifica se a senha foi comprometida
    print(f"\n{Fore.WHITE}Verificando vazamentos de dados...")
    foi_comprometida, count = check_pwned_password(password)
    
    if foi_comprometida:
        print(f"{Fore.RED}⚠️  ATENÇÃO: Esta senha foi encontrada em {count:,} vazamentos de dados!")
        print(f"{Fore.RED}   Recomenda-se fortemente trocar esta senha.")
    else:
        print(f"{Fore.GREEN}✅ Boa notícia: Esta senha não foi encontrada em vazamentos conhecidos.")

def main():
    parser = argparse.ArgumentParser(description="Verificador de Força de Senhas")
    parser.add_argument("--password", help="Senha para verificar")
    parser.add_argument("--generate", action="store_true", help="Gerar senha segura")
    parser.add_argument("--length", type=int, default=12, help="Comprimento da senha gerada (mínimo 8)")
    parser.add_argument("--no-symbols", action="store_true", help="Não incluir símbolos na senha gerada")

    args = parser.parse_args()
    
    if args.generate:
        print(f"\n{Fore.CYAN}GERADOR DE SENHAS SEGURAS")
        print(f"{Fore.CYAN}{'='*30}")
        
        include_symbols = not args.no_symbols
        generated_password = generate_secure_password(args.length, include_symbols)
        
        print(f"\n{Fore.GREEN}Senha gerada: {Fore.WHITE}{generated_password}")
        
        # Analisa a senha gerada
        print_password_analysis(generated_password)
        
    elif args.password:
        print_password_analysis(args.password)
        
    else:
        parser.print_help()
        print(f"\n{Fore.YELLOW}Exemplos de uso:")
        print(f"{Fore.WHITE}  python passwordStrengthChecker.py --password 'MinhaSenh@123'")
        print(f"{Fore.WHITE}  python passwordStrengthChecker.py --generate")
        print(f"{Fore.WHITE}  python passwordStrengthChecker.py --generate --length 16")
        print(f"{Fore.WHITE}  python passwordStrengthChecker.py --generate --length 10 --no-symbols")

if __name__ == "__main__":
    main()

