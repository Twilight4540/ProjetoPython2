#Declaração
n: int = 1
m: int = 1
i: int = 0
#Inicio
while i < 7:
    m = 1
    while n + m != 7:
        m = m + 1
    if n + m == 7:
        print(n, '+', m, 'é igual a 7')
    i = i + 1
    n = n + 1
#Fim