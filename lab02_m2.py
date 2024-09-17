def posicao(pos0, v0, a, t):
    return pos0 + v0 * t + 0.5 * a * (t ** 2)

pos0 = float(input("Informe a posição inicial (m): "))
v0 = float(input("Informe a velocidade inicial (m/s): "))
a = float(input("Informe a aceleração constante (m/s²): "))


for t in range(11):
    pos = posicao(pos0, v0, a, t)
    print(f"Para t = {t} s, a posição é {pos:.1f} m")



#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU