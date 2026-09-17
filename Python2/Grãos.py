#Declaração
i: int = 1
G: int = 1
s: int = 0
#Inicio
while i <= 64:
    s = s + G
    G = G * 2
    i = i + 1
print('A soma dos grãos de trigo é', s)
#Fim