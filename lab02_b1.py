#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU

def recebeInteiro(valor):
    try:
        return int(valor)
    except ValueError:
        return None


num1 = input("Digite o primeiro número inteiro: ")
num2 = input("Digite o segundo número inteiro: ")
num3 = input("Digite o terceiro número inteiro: ")

num1 = recebeInteiro(num1)
num2 = recebeInteiro(num2)
num3 = recebeInteiro(num3)

if num1 is not None and num2 is not None and num3 is not None:
    soma = num1 + num2 + num3
    print(f"A soma de {num1}, {num2} e {num3} é {soma}")
else:
    print("Erro: Digite apenas números inteiros.")
