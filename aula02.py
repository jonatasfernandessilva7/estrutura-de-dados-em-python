#AULA 02

#listas
'''
k = ['greater', ['less', 10]]
print (k)
'''
'''
#tupla
p = (100)
p = (100, )
print (p)
'''

#laços sobre sequências
'''
testlist = [67,100,22]

for item in testlist:
    print (item)
    '''
'''
testlist = [67,100,22]

for index in range (len(testlist)):
    print (testlist [index])   
    '''

#funções
'''
def square (n):
     #retorna o quadrado de n
    result = n**2
    return result
m = square (20)
print ('o quadrado de m é: ', m)
'''
'''
lower = float (input ('o numero a esquerda é: '))
upper = float (input ('o numero a direita é: '))

def displayRange (lower, upper):
  if lower < upper:
    return 0
  else: 
    return lower/upper
t = displayRange (lower, upper)
print (t)
'''

#função aninhada
'''
n = float (input('digite o valor de n: '))
def factorial (n,product=1):
  if n == 1:
    return product
  else:
    return factorial (n-1, n*product)
n1 = factorial (n,1)
print ('o fatorial de {} é: {}'.format(n,n1))
'''

#exercício
'''
#pagamento semanal = pag p/hora * (total de hora regular + hora extra)
#pagamento de hora extra = total hora extra * (1.5*salario p/ hora)

#entrada de dados feita pelo usuário
nome_funcionario = str (input('digite o nome do funcionário: '))
salario_hora = float (input ('digite o salário por hora do funcionário: '))
horas_regulares = float (input ('digite o total de horas do funcionário: '))
horas_extras = float (input ('digite o total de horas extras do funcionário: '))

#cálculo hora extra
pg_hora_extra = horas_extras * (1.5 * salario_hora)

#cálculo pagamento semanal
pg_semanal = salario_hora * (horas_regulares + horas_extras)

print ('o pagamento semanal do funcionário {} é de {:.2f} reais'.format(nome_funcionario, pg_semanal))
'''