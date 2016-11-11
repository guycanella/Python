
import random
import numpy as np
import matplotlib.pyplot as plt
import math


x = 0
vec = []
intervals = []
points = []

print 'Defina ou numero de intervalos (N) ou a resolucao (R)'
m = raw_input('-->')


if m=='N':
    print 'Escolha o numero de intervalos:'
    n = raw_input('-->')
    o = int(n)
    data = [0]*(o+1)
    points = [0]*o

    for x in range(100):
        vec.append(random.random())

    x1           =   np.amax(vec)
    x2           =   np.amin(vec)

    int          =   (x1 - x2)/o
    roundInt     =   round(int,3)


    for i in data:
        intervals.append(x2)
        x2 += roundInt

    print ""
    print "Intervalos:"
    print ""

    for i in intervals:
        print i

    for j in range(len(vec)):
        for i in range(len(intervals)):
            if vec[j]>=intervals[i] and vec[j]<intervals[i+1]:
                points[i] += 1

            if i+1 == o:
                break

        if vec[j]>intervals[o]:
            points[o-1] += 1

    print points

    n, bins, patches = plt.hist(vec, o, normed=1, facecolor='red', alpha=0.75)
    plt.show()

elif m=='R':
    print 'Escolha o valor da resolucao:'
    n = raw_input('-->')
    o = float(n)
    for x in range(100):
        vec.append(random.random())

    x1           =   np.amax(vec)
    x2           =   np.amin(vec)

    val          =   (x1 - x2)/o
    roundVal     =   round(val)
    Ninteiro     =   int(roundVal)
    data = [0]*(Ninteiro+1)
    points = [0]*Ninteiro

    print ''
    print roundVal
    print Ninteiro

    for i in data:
        intervals.append(x2)
        x2 += o

    print ""
    print "Intervalos:"
    print ""

    for i in intervals:
        print i

    for j in range(len(vec)):
        for i in range(len(intervals)):
            if vec[j]>=intervals[i] and vec[j]<intervals[i+1]:
                points[i] += 1

            if i+1 == o:
                break

        if vec[j]>intervals[Ninteiro]:
            points[Ninteiro-1] += 1

    print ""
    print points

    n, bins, patches = plt.hist(vec, Ninteiro, normed=1, facecolor='red', alpha=0.75)
    plt.show()
