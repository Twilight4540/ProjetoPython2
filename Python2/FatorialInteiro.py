#Receba um número N. Calcule e mostre a série 1 + 1/2! + 1/3! + 1/4! + ... + 1/N!.
#Declaração
N: int = 0
S: int = 0
i: int = 1
F: int = 1
j: int = 1
#Inicio
N = int(input('Digite um número inteiro: '))
while i <= N:
    while j <= i:
        F = F * j
        j = j + 1
    S = S + (1/F)
    i = i + 1
#Fim