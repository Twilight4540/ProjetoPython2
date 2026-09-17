#Declaração
S: float = 0
i: int = 1
o: int = 1
#Inicio
while i <= 99:
    S = S + (o/i)
    o = o + 1
    i = i + 2
print('O resultado da soma é', S)
#Fim