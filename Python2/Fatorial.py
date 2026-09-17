#Declarar
N: int = 0
F: int = 1
#Inicio
N = int(input('Digite um número inteiro: '))
while N > 0:
    F = N * F
    N = N - 1
print('O fatorial é', F)
#Fim