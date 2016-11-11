
from math import *
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t	=	np.arange(0.0,1.0,0.001)

x1	=	np.cos(2*np.pi*10*t)
x2	=	0.5*np.cos(2*np.pi*20*t)
n	=	np.cos(2*np.pi*60*t)
pwm	=	0.5*signal.square(-15*np.pi*t)+0.5


x	=	x1	+	x2
y	=	x	+	n

sp	=	np.fft.fft(x)
spS	=	np.fft.fftshift(sp)
sn	=	np.fft.fft(n)
snS	=	np.fft.fftshift(sn)
sy	=	np.fft.fft(y)
syS	=	np.fft.fftshift(sy)

filtro	=	syS*pwm

xOrg	=	np.fft.ifftshift(filtro)
quase	=	np.fft.ifft(xOrg)
final	=	quase - x

print(syS.real)

plt.subplot(9,1,1)
plt.plot(x)
plt.subplot(9,1,2)
plt.plot(spS)
plt.subplot(9,1,3)
plt.plot(n)
plt.subplot(9,1,4)
plt.plot(snS)
plt.subplot(9,1,5)
plt.plot(y)
plt.subplot(9,1,6)
plt.plot(syS)
plt.subplot(9,1,7)
plt.plot(filtro)
plt.subplot(9,1,8)
plt.plot(quase)
plt.subplot(9,1,9)
plt.plot(final)
plt.show()

