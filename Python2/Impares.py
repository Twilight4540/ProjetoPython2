#Declaração
n1: int = 0
n2: int = 0
i: int = 0
s: int = 0
#Inicio
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    i = n2 + 1
    while i < n1:
        if i % 2 != 0:
            s = s + i
            i = i + 1
        else:
            i = i + 1
else:
    i = n1 + 1
    while i < n2:
        if i % 2 != 0:
            s = s + i
            i = i + 1
        else:
            i = i + 1
print('A soma dos números ímpares é', s)
#Fim