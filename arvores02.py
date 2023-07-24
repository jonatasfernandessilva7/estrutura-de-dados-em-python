#construindo uma árvore

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