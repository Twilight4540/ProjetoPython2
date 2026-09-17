#Declaração
N: int = 0
a: int = 0
b: int = 1
c: int = 0
i: int = 1
#Inicio
N = int(input('Digite a quantidade de termos da série de Fibonacci: '))
while i <= N:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1
#Fim