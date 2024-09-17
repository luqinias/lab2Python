#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU

import math

def converteGR(graus):
    return graus * (math.pi / 180)

def converteRG(radianos):
    return radianos * (180 / math.pi)

def leiCossenos(a, b, angulo_oposto_c):
    angulo_oposto_c_rad = converteGR(angulo_oposto_c)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angulo_oposto_c_rad))
    return c

def leiSenos(a, angulo_oposto_a, angulo_oposto_x):
    angulo_oposto_a_rad = converteGR(angulo_oposto_a)
    angulo_oposto_x_rad = converteGR(angulo_oposto_x)
    x = (a * math.sin(angulo_oposto_x_rad)) / math.sin(angulo_oposto_a_rad)
    return x

def leiSenos_angulo(x, y, angulo_oposto_x):
    angulo_oposto_x_rad = converteGR(angulo_oposto_x)
    sin_angulo_oposto_y = (y * math.sin(angulo_oposto_x_rad)) / x
    angulo_oposto_y_rad = math.asin(sin_angulo_oposto_y)
    angulo_oposto_y = converteRG(angulo_oposto_y_rad)
    return angulo_oposto_y

def terceiroAnguloGraus(theta, phi):
    return 180 - (theta + phi)

def calcular_triangulo():
    opcao = input("""Deseja entrar com: 
                  (1) dois lados e o ângulo entre eles, ou 
                  (2) dois ângulos e o lado entre eles
                  """)
    
    if opcao == "1":
        
        a = float(input("Informe o tamanho do lado A: "))
        b = float(input("Informe o tamanho do lado B: "))
        angulo_theta = float(input("Informe o ângulo entre os lados A e B (em graus): "))
        
        
        c = leiCossenos(a, b, angulo_theta)
        
        
        angulo_a = leiSenos_angulo(c, a, angulo_theta)
        angulo_b = terceiroAnguloGraus(angulo_theta, angulo_a)
        
        
        print(f"\nLados do triângulo: A = {a:.2f}, B = {b:.2f}, C = {c:.2f}")
        print(f"Ângulos do triângulo: θ = {angulo_theta:.2f}°, Ângulo oposto a A = {angulo_a:.2f}°, Ângulo oposto a B = {angulo_b:.2f}°")
    
    elif opcao == "2":
        
        angulo_a = float(input("Informe o ângulo A-B (em graus): "))
        angulo_b = float(input("Informe o ângulo A-C (em graus): "))
        c = float(input("Informe o tamanho do lado entre A-B e A-C (lado C): "))
        
        
        angulo_c = terceiroAnguloGraus(angulo_a, angulo_b)
        
        
        a = leiSenos(c, angulo_c, angulo_a)
        b = leiSenos(c, angulo_c, angulo_b)
        
        
        print(f"\nLados do triângulo: A = {a:.2f}, B = {b:.2f}, C = {c:.2f}")
        print(f"Ângulos do triângulo: Ângulo A-B = {angulo_a:.2f}°, Ângulo A-C = {angulo_b:.2f}°, Ângulo B-C = {angulo_c:.2f}°")
    
    else:
        print("Opção inválida. Escolha 1 ou 2.")

calcular_triangulo()
