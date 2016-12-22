
from math import *
import numpy as np
import matplotlib.pyplot as plt

def fsin(grau):
    return sin(grau)

def fcos(grau):
    return cos(grau)

# L = L0 ###########################
#

theta1  =   2.028
theta2  =   4.913
theta3  =   7.978

x1  =   np.arange(0,1.01,0.01)

frac1   =   (sqrt(theta1*theta1 + 1)-1)/(sqrt(theta1*theta1 + 1)+1)
frac2   =   (sqrt(theta2*theta2 + 1)-1)/(sqrt(theta2*theta2 + 1)+1)
frac3   =   (sqrt(theta3*theta3 + 1)-1)/(sqrt(theta3*theta3 + 1)+1)

e1  =   sqrt(theta1*theta1 + 1) - 1
e2  =   sqrt(theta2*theta2 + 1) - 1
e3  =   sqrt(theta3*theta3 + 1) - 1

Ftheta1 =   np.linspace(0,x1.size,x1.size)
Ftheta2 =   np.linspace(0,x1.size,x1.size)
Ftheta3 =   np.linspace(0,x1.size,x1.size)


for i in range(len(x1)):
    Ftheta1[i]  =   (sqrt(frac1)*fcos(theta1*x1[i])+fsin(theta1*x1[i]))*(sqrt(frac1)*fcos(theta1*x1[i])+fsin(theta1*x1[i]))+sqrt(frac1)*sqrt(frac1)*(fcos(theta1*x1[i])-sqrt(frac1)*fsin(theta1*x1[i]))*(fcos(theta1*x1[i])-sqrt(frac1)*fsin(theta1*x1[i]))

for i in range(len(x1)):
    Ftheta2[i]  =   (sqrt(frac2)*fcos(theta2*x1[i])+fsin(theta2*x1[i]))*(sqrt(frac2)*fcos(theta2*x1[i])+fsin(theta2*x1[i]))+sqrt(frac2)*sqrt(frac2)*(fcos(theta2*x1[i])-sqrt(frac2)*fsin(theta2*x1[i]))*(fcos(theta2*x1[i])-sqrt(frac2)*fsin(theta2*x1[i]))

for i in range(len(x1)):
    Ftheta3[i]  =   (sqrt(frac3)*fcos(theta3*x1[i])+fsin(theta3*x1[i]))*(sqrt(frac3)*fcos(theta3*x1[i])+fsin(theta3*x1[i]))+sqrt(frac3)*sqrt(frac3)*(fcos(theta3*x1[i])-sqrt(frac3)*fsin(theta3*x1[i]))*(fcos(theta3*x1[i])-sqrt(frac3)*fsin(theta3*x1[i]))

plt.title(r'$\mathrm{Grafico\ de\ densidade\ de\ probabilidade\ para\ uma\ caixa\ com}$ $L = L_0$',fontsize=20)
plt.ylabel(r'$|\Psi|^2$',fontsize=18)
plt.xlabel(r'$\mathrm{Comprimento\ da\ caixa}$',fontsize=18)
plt.plot(x1,Ftheta1,'o')
plt.plot(x1,Ftheta2,'^')
plt.plot(x1,Ftheta3,'s')
plt.grid()
plt.show()
