def recebeInteiro():
    while True:
        try:
            return int(input("Informe um número inteiro: "))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def maximo(num1, num2, num3):
    return max(num1, num2, num3)

num1 = recebeInteiro()
num2 = recebeInteiro()
num3 = recebeInteiro()

maior_numero = maximo(num1, num2, num3)

print(f"O máximo de {num1}, {num2} e {num3} é {maior_numero}")



#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU