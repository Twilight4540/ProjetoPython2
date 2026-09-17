#Declaração
B: int = 0
E: int = 0
P: int = 0
#Inicio
B = int(input('Digite o valor da base: '))
E = int(input('Digite o valor do expoente: '))
P = B
while E > 1:
    P = P * B
    E = E - 1
print('O resultado da potência é', P)
#Fim