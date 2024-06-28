
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    return True

# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é primo
if eh_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
