import math

def recebeInteiro():
    try:
        x = int(input("Informe o número de x: "))
        y = int(input("Informe o número de y: "))
        r = int(input("Informe o raio do círculo: "))
        
        return x,y,r
    
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

def dentroCirculo(x, y, r):
    distancia = math.sqrt(x**2 + y**2)
    return distancia <= r

x,y,r = recebeInteiro()

if dentroCirculo(x, y, r):
    print(f"O ponto ({x:.1f}, {y:.1f}) está dentro ou sobre o círculo do raio {r:.1f}")
else:
    print(f"O ponto ({x:.1f}, {y:.1f}) está fora da círculo do raio {r:.1f}")


#José Lucas Lira Bizil, Matrícula: 12411ECP005, Engenharia de Computação - UFU