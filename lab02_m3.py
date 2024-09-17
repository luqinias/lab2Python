def recebeInteiro(n):
    while True:
        try:
            valor = int(input(n))
            if valor > 0:
                return valor
            else:
                print("Informe um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro positivo.")

def mdc(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = recebeInteiro("Informe um número inteiro positivo: ")
b = recebeInteiro("Informe um número inteiro positivo: ")


resultado = mdc(a, b)
print(f"O máximo divisor comum MDC entre {a} e {b} é {resultado}.")




#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU