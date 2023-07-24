#AULA 04 ARRAYS
'''
import numpy as np
a = np.ones ((3,3))
a.dtype
d = np.array ([1+2j, 3+4j, 5+6*1j])
d.dtype
e = np.array ([True,True,True])
e.dtype
f = np.array (['bonjour', 'hello', 'olá'])
f.dtype
print(a,d,e,f)
'''

#visualização 2d
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace (0,3,20)
y = np.linspace(0,9,20)
plt.plot(x,y)
plt.plot(x,y,'o')
plt.show()
'''

#visualização bidimensional
'''
image = np.random.rand(30,30)
plt.imshow(image, cmap =plt.cm.jet)
plt.colorbar()
plt.show()
'''

#operações com array
'''
import numpy as np

a = np.array ([1,2,3,4])
b = np.array ([5,6,7,8])
c = a==b
d = a>b
print (c,d)
'''
'''
a = np.array ([1,2,3,4], dtype=bool)
b = np.array ([5,6,7,8], dtype=bool)
c = np.logical_or(a,b)
d = np.logical_and(a,b)
print (c,d)
'''
'''
a = np.array ([1,2,3,4])
b = np.array ([[5,6,7,8]])
c1 = a.mean()
d = np.median(a)
e = a.std()
print (c1,d,e)
'''