#Declaração
N1: int = 0
N2: int = 0
#Inicio
N1 = int(input('Digite o 1° número: '))
N2 = int(input('Digite o 2° número: '))
if N1 == N2:
    print('Os números são iguais')
else:
    if N1 > N2:
        print('O maior número é: ', N1)
    else:
        print('O maior número é: ', N2)
#Fim