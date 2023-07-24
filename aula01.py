#AULA 01
'''
#Esse código representa um algoritmo booleano que verifica se o  valor A é verdadeiramente maior que a variável B

#entrada de dados informados pelo usuário
a=int(input('me diga um valor a '))
b=int(input('me diga um valor b' ))

#condição
x=a>b

#onde mostrará se o resultado é falso ou verdadeiro
print('x', x)
'''

'''
#esse código calcula a área

#dados informados pelo usuário
radius=float(input('radius: '))

#parte onde será printado o resultado no terminal
print('the area is', 3.14*radius**2)
'''

'''
#transforms número inteiro em real e real em inteiro

#entrada de dados pré-estabelecido
t=round(3.15)

#print na tela
print('t é', t)
'''

'''
#variáveis de atribuição

#mostra o valor mínimo entre parâmetros
minValue=min(100,200)
print(minValue)

#mostra o valor máximo entre parâmetros dividida por uma variável
product=max(100,200)/30
print(product)
'''

'''
#->tipos de dados

#~instruções import: permite o programador importar a biblioteca que está instalada
#~condicionais: if, elif, else(devem ter dois pontos ao final da linha e a linha seguinte deve ter recuo)/valores booleanos: false or true

#entrada de dados feita pelo usuário
x=float(input('me dê um valor para x: '))
y=float(input('me dê um valor para y: '))
#estrutura de condição para que seja apresentado um valor correto para o usuário
if x>y:
    print('x is greater than y')
elif x<y:
    print('x is less than y')
else:
    print('x is equal to y')
'''

'''
#laços de repetição (while)


#dados pré-estabelecido
product=1
value=1

#estrutura de repetição (enquanto)
while value <= 10: #calcula um valor fatorial
    product*=value #faz o valor do produto ser multiplicado pelo valor de value
    value+=1 #value é acrescentado 1, para que o programa continue, quando value for igual a 10 o programa para
    print(product)


#exemplo 02 

product=1
for value in range (1,11): #para o valor no intervalo de ()
    product*=value
    print(product)
'''

'''
#exemplo uso string
p1 = 'universidade' [0]
print (p1)
'''

'''
#exeplo 2 uso string (substring)
p1 = 'universidade' [2:9]
print (p1)
'''


#formatar string para saída
'''
for exponent in range (7,11):
    print (exponent, 10 ** exponent)
    '''

'''
#como justificar
p2 = "%-6s" % "four" #"%" limite de área justificada , a esquerda com sinal negativo e sem sinal justificado a direita
print (p2)   

for exponent in range (7,11):
    print ("%-3d%12d" % (exponent, 10 ** exponent))
    '''

'''
w1 = 'greater'.isupper()
w2 = 'greater'.upper()
w3 = 'greater'.startswith('great')
print (w1,w2,w3)
'''
'''
#exercicios

#questão 01
import math

r = float(input('digite a medida do raio da circunferência: ')) #r = raio

d = 2*r #diâmetro
c = 2*math.pi*r #cinrcunferência
a = 4*math.pi*(r**2) #área da superfície 
v = (4/3)*math.pi*(r**2)

print ('o valor do diâmetro é {}, o valor do da circunferênciaé {}, a superfíce é {}, a área tem valor de {} e o volume mede {}'.format(d,c,a,v))
'''