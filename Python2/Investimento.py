#Declaração
tipo: str = ''
V: float = 0.0
VF: float = 0.0
#Inicio
tipo = input('Digite 1 para Poupança ou 2 para Renda Fixa: ')
V = float(input('Digite o valor do investimento: '))
if tipo == '1':
    VF = V * 1.03
    print('O valor do investimento em Poupança é: ', VF)
elif tipo == '2':
    VF = V * 1.05
    print('O valor do investimento em Renda Fixa é: ', VF)
else:
    print('Opção inválida')
#Fim    