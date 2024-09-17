def recebeInteiro():
    while True:
        try:
            return int(input("Informe um número inteiro: "))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def media(num1, num2, num3):
    return (num1 + num2 + num3) / 3

num1 = recebeInteiro()
num2 = recebeInteiro()
num3 = recebeInteiro()

resultado_media = media(num1, num2, num3)

print(f"A média de {num1}, {num2} e {num3} é {resultado_media:.2f}")



#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU