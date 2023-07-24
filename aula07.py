# AULA 07-listas, recursão, enumeração
'''
n1 = int(input('entre com um inteiro: '))
n2 = int(input('entre com um inteiro: '))
r = int(input('entre com o tamanho do passo: '))

inicio = n1
fim = n2
passo = r

for i in range(inicio,fim, passo):
  print(i)
'''

'''
class PowTwo:
  """Class to implement on interator of powers of two"""
  def __init__ (self, max = 0):
    self.max = max
  def __iter__(self):
    self.n = 0
    return self
  def __next__(self):
    if self.n <=self.max:
      result = 2 ** self.n
      self.n += 1
      return result
    else:
      raise StopIteration

numbers = PowTwo(4)

i = iter (numbers)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
'''

'''
def listsum(numList):
  theSum = 0
  for i in numList:
    theSum += i
  return theSum

print(listsum([1,3,5,7,9]))
'''

'''
def hanoi(disco:int,origem:str,aux:str,destino:str)->None:
  if disco<=0:
    return
  hanoi(disco -1,origem,destino,aux)
  print(f'movendo disco{disco} de {origem} para{destino}')
  hanoi(disco -1,aux,origem,destino)

if __name__ == "__main__":
  hanoi(3,'origem','aux','destino')
'''

'''
def toStr(n,base):
  convertString = "0123456789ABCDEF"

  if n<base:
    return convertString[n]
  else:
    return toStr(n//base,base)+convertString[n%base]

print(toStr(423,16))
'''
