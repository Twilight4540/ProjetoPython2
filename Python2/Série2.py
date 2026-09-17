#Declaração
S: float = 0
i: int = 1
o: int = 1
p: int = 1
#Inicio
while i <= 225:
    if i % 2 != 0:
        S = S + (o/i)
    else:
        S = S - (o/i)
    o = o + 1
    p = p + 2
    i = i + p
print('O resultado da soma é', S)
#Fim