#Declaração
A: float = 1.10
M: float = 1.50
a: int = 0
#Inicio
while A < M:
    A = A + 0.03
    M = M + 0.02
    a = a + 1
print('Ana será maior que Maria em ', a, 'anos')