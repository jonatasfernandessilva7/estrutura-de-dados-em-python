#AULA 03

#função tempo
'''
import time

problemSize = 10000000
print ("%12s%16s" % ("problem size", "seconds"))
for count in range (5):
    start = time.time()
#inicio do algoritmo
    work = 1
    for x in range (problemSize):
        work += 1
        work -= 1
#fim do algoritmo
elapsed = time.time() - start
print ("%12d%16.3f" % (problemSize, elapsed))
problemSize *= 2
'''

'''
import time

problemSize = 1000
print ("%12s%16s" % ("problem size", "seconds"))
for count in range (5):
    number = 0
#inicio do algoritmo
    work = 1
    for j in range (problemSize):
        for k in range(problemSize):
            number +=1
            work += 1
            work -= 1
#fim do algoritmo
print ("%12d%15d" % (problemSize, number))
problemSize *= 2
'''

#Recursão Fibonacci
'''
n = int (input('me diga um numero natural: '))

def fib(n):

  #introdução a função

  if n < 3:
    return 1
  else:
    return fib (n - 1) + fib (n - 2)
t = fib (n)
print (t)
'''

#ALGORITMOS DE PESQUISA LINEAR
'''
def pesquisa_linear(arranjo, elemento_desejado):
  for elemento in arranjo:
    if elemento == elemento_desejado:
      print ('elemento {} está presente no arranjo'.format(elemento_desejado))
      return
  print ('elemento {} não está presente no arranjo'.format(elemento_desejado))

arranjo = list ( range (1,100))

#pesquisa desejada
pesquisa_linear (arranjo , 83)
'''

#ALGORITMOS DE PESQUISA BINÁRIA
'''
def pesquisa_binaria ( A, item):
  """implementa pesquisa binaria interativamente"""
  esquerda,direita = 0,len (A) - 1
  while esquerda <= direita:
    meio = (esquerda + direita) // 2
    if A[meio] == item:
      return meio
    elif A[meio] > item :
      direita = meio - 1
    else:
      esquerda = meio + 1
    return -1

A = [0,10,20,30,40,50,60,70]
print ('pesquisa com sucesso:', pesquisa_binaria(A,60))
'''