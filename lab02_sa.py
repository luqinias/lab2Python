#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU

import math

def graus_para_radianos(angulo_graus):
    return angulo_graus * (math.pi / 180)

def altura_maxima(alturas):
    return max(alturas)

def calcular_alturas(hipotenusa, angulo_graus):
    angulo_rad = graus_para_radianos(angulo_graus)
    
    cateto_adjacente = hipotenusa * math.cos(angulo_rad)
    cateto_oposto = hipotenusa * math.sin(angulo_rad)
    area = 0.5 * cateto_adjacente * cateto_oposto
    altura_hipotenusa = (2 * area) / hipotenusa
    
    return altura_hipotenusa, cateto_oposto, cateto_adjacente

hipotenusa = float(input("Informe o tamanho da hipotenusa: "))
angulo = float(input("Informe o ângulo em graus entre a hipotenusa e um dos catetos: "))

altura_hipotenusa, altura_cateto_adjacente, altura_cateto_oposto = calcular_alturas(hipotenusa, angulo)

print(f"Altura com base na hipotenusa: {altura_hipotenusa:.2f}")
print(f"Altura com base no cateto adjacente: {altura_cateto_adjacente:.2f}")
print(f"Altura com base no cateto oposto: {altura_cateto_oposto:.2f}")

alturas = [altura_hipotenusa, altura_cateto_adjacente, altura_cateto_oposto]
altura_max = altura_maxima(alturas)
print(f"A altura máxima do triângulo é: {altura_max:.2f}")

