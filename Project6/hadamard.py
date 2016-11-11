import sys
import numpy as np
import matplotlib.pyplot as plt


N	=	raw_input('Ordem da Hadamard: ')
n	=	int(N)

H	=	np.zeros(shape=(n,n))

# Gera a matrix
i1 = 1
while i1 < n:
    for i2 in range(i1):
        for i3 in range(i1):
            H[i2+i1][i3]    = H[i2][i3]
            H[i2][i3+i1]    = H[i2][i3]
            H[i2+i1][i3+i1] = not H[i2][i3]
    i1 += i1

for i in range(n):
    for j in range(n):
        if H[i][j]:
            H[i][j] = -1
        else:
            H[i][j] = 1

for i in range(n):
	plt.subplot(n,1,i+1)
	plt.plot(H[i][:n-1])

plt.show()

print(H)
print(" ")
print(np.linalg.inv(H))
