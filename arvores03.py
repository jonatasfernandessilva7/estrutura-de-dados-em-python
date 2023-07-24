# construindo uma árvore

'''
class NoDaArvore:
    def __init__ (self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__ (self):
        return '%s <- %s -> %s' %(self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

raiz = NoDaArvore(3)
raiz.esquerda = NoDaArvore(5)
raiz.direita = NoDaArvore(1)

print('árvore: ', raiz)
'''

'''
class NoDaArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
        self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

def insere(raiz, nodo):

    if raiz is None:
        raiz = nodo

    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo

        else:
            insere(raiz.direita, nodo)

    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo

        else:
            insere(raiz.esquerda, nodo)

def busca(raiz, chave):
    if raiz is None:
        return None

    if raiz.chave == chave:
        return raiz

    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    return busca(raiz.esquerda, chave)


raiz = NoDaArvore(40)

for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NoDaArvore(chave)
    insere(raiz, nodo)

for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)

    if resultado:
        print('busca pela chave {}: sucesso!!'.format(chave))
    else:
        print('busca pela chave {}: falha!!'.format(chave))
'''

#algoritmo de huffman
import heapq
from heapq import heappop, heappush
from operator import le
from turtle import left, right
from urllib.parse import parse_qs

def isLeaf(root):
    return root.left is None and root.right is None

class Node:
    def __init__(self, ch, freq, left = None, right = None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def encode(root, s, huffman_code):
    if root is None:
        return

    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '0+1', huffman_code)

def decode (root, index, s):
    if root is None:
        return index

    if isLeaf(root):
        print(root.ch, end='')
        return index

    index += 1
    root = root.left if s[index] == 0 else root.right
    return decode(root, index, s)

def buildhuffmantree(text):
    if len(text) == 0:
        return

    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

while len(pq) != 1:
    left = heappop(pq)
    right = heappop(pq)

    total = left.freq + right.freq
    heappush(pq, Node(None, total, left, right))

root = pq[0]

huffmanCode = {}
encode(root, '', huffmanCode)

print(huffmanCode)
print(text)

s = ''
for c in text:
    s += huffmanCode.get(c)

print(s)
print(end = '')

if isLeaf(root):
    while root.freq > 0:
        print(root.ch, end = '')
        root.freq = root.freq - 1

else:
    index = -1
    while index < len(s) - 1:
        index = decode(root, index, s)

if __name__ == "__main__":
    text = 'huffman coding is a data compresion algorithm'
    buildhuffmantree(text)