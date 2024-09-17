def ehPar(numero):
    return numero % 2 == 0

def recebeInteiro():
    while True:
        try:
            return int(input("Informe um número inteiro: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

numero = recebeInteiro()

if ehPar(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU