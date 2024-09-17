def recebeInteiro():
    while True:
        try:
            return int(input("Informe um número inteiro: "))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = recebeInteiro()

resultado_fatorial = fatorial(numero)

print(f"O fatorial de {numero} é {resultado_fatorial}")


#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU