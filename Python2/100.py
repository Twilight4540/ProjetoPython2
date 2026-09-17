#Declarar
i: int = 1
N: int = 0
MA: int = 0
ME: int = 0
#Inicio
MA = 50
ME = 50
while i < 100:
    N = int(input('Digite um número inteiro positivo: '))
    if N > MA:
        MA = N
    if N < ME:
        ME = N
    if N < 0:
        print('Número inválido. Digite um número inteiro positivo.')
    else:
        i = i + 1
print('O maior número digitado é', MA)
print('O menor número digitado é', ME)
#Fim