#Declaração
N1: int = 0
N2: int = 0
i: int = 0
div: int = 0
n: int = 1
#Inicio
N1 = int(input('Digite o primeiro número inteiro: '))
N2 = int(input('Digite o segundo número inteiro: '))
if N1 > N2:
    i = N2 + 1
    while i < N1:
        div = 0
        n = 1
        while n <= i:
            if i % n == 0:
                div = div + 1
                n = n + 1
            else:
                n = n + 1
        if div == 2:
            print(i, 'é primo')
        i = i + 1
else:
    i = N1 + 1
    while i < N2:
        div = 0
        n = 1
        while n <= i:
            if i % n == 0:
                div = div + 1
                n = n + 1
            else:
                n = n + 1
        if div == 2:
            print(i, 'é primo')
        i = i + 1
#Fim