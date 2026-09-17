#Declaração
A: float = 0.0
B: float = 0.0
C: float = 0.0
D: float = 0.0
X1: float = 0.0
X2: float = 0.0
#Inicio
A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))
D = (B**2) - (4*A*C)
if D < 0:
   print('Não existem raízes reais')
else:
   X1 = (-B + (D**0.5))/(2*A)
   X2 = (-B - (D**0.5))/(2*A)
   print('O valor de X1 é: ', X1)
   print('O valor de X2 é: ', X2)
#Fim