
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from math import *
import random

# PROGRAM #
t       =   np.arange(0,8,1)
t       =   np.delete(t,0)
t2      =   np.arange(0,104,1)
A       =   np.matrix([[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]])
A2      =   np.matrix([[1,1,1],[1,1,4],[1,3,9],[1,4,16],[1,5,25],[1,6,36],[1,7,49]])
A3      =   np.matrix([[i,1] for i in range(104)])
Y       =   np.matrix('2;5;7;7;9;11;13')
YP      =   np.matrix('2;4;6;8;10;12;14')
Y2      =   np.matrix('1;5;10;15;24;37;50')

###########################################################################################

with open('exp_data.dat') as f:
    data    =   f.readlines()

for i in range(len(data)):
    data[i] =   data[i][:-2]
    data[i] =   float(data[i])

data.sort()

##########################################################################################

y  = []
y1 = []
x = np.linspace(0,10,200)
for i in x:
    y.append(i + cos(i) + random.randint(0,2))

##########################################################################################

result  =   np.dot(np.dot(np.linalg.inv(np.dot(A.transpose(),A)),A.transpose()),Y)
resultP =   np.dot(np.dot(np.linalg.inv(np.dot(A.transpose(),A)),A.transpose()),YP)
result2 =   np.dot(np.dot(np.linalg.inv(np.dot(A2.transpose(),A2)),A2.transpose()),Y2)
result3 =   np.dot(np.dot(np.linalg.inv(np.dot(A3.transpose(),A3)),A3.transpose()),data)

result3 =   result3.tolist()
## PLOT ##
plt.subplot(3,2,1)
plt.plot(t,YP,'ro')
plt.plot(t,float(resultP[0])*t + float(resultP[1]),'k')

plt.subplot(3,2,2)
plt.plot()
plt.plot()

plt.subplot(3,2,3)
plt.plot(t,Y,'ro')
plt.plot(t,float(result[0])*t + float(result[1]),'k')

plt.subplot(3,2,4)
plt.plot(t,Y2,'ro')
plt.plot(t,float(result2[0]) + float(result2[1])*t + float(result2[2])*t**2,'k')

plt.subplot(3,2,5)
plt.plot(data,'o')
plt.plot(t2,result3[0][0]*t2 + result3[0][1],'r')

plt.show()
