#Declaração
N: int = 0
S: int = 0
i: int = 1
#Inicio
N = int(input('Digite um número inteiro: '))
while i <= N:
    S = S + (1/i)
    i = i + 1
print('O resultado da soma é', S)
#Fim