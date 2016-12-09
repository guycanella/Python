
# Import of libraries
import random
import math
import numpy as np
from random import randint
import matplotlib.pyplot as plt

# Constants
begin       =   0
count       =   1
iterations  =   1000
individuals =   200
cities      =   10
minMerit    =   range(iterations)
meanMerit   =   range(iterations)
deviation   =   range(iterations)

def shift(key,array):
    return array[-key:]+array[:-key]

def dados(tupla):
    soma        =   0.0
    soma2       =   0.0
    valueMerits =   range(len(tupla))
    for i in range(len(tupla)):
        soma    =   soma    + tupla[i][0]
    media   =   soma/len(tupla)
    for i in range(len(tupla)):
        soma2   =   soma2   +   (media - tupla[i][0])**2
    desvio  =   math.sqrt(soma2/len(tupla))
    for i in range(len(tupla)):
        valueMerits[i]  =   tupla[i][0]
    return media,desvio,min(valueMerits)

def merit(individual,cities):
    soma    =   0.0
    for i in range(len(individual)):
        if (i == len(individual)-1): return [soma,individual]
        a       =   individual[i]
        b       =   individual[i+1]
        value   =   math.sqrt((cities[b][1] - cities[a][1])**2 + (cities[b][0] - cities[a][0])**2)
        soma    =   soma + value

def returnMeritsOfGen(tupla):
    value   =   range(len(tupla))
    for i in range(len(tupla)):
        value[i]    =   tupla[i][0]
    return value


# PROGRAM
# Generate the coordinates of the cities
coordCities =   [(random.random(),random.random()) for x in range(cities)]


# Generate the individuals
column, line    =   individuals, cities

matrixInd       =   [range(line) for y in range(column)]
for i in range(len(matrixInd)):
    random.shuffle(matrixInd[i])
    matrixInd[i].remove(0)
    matrixInd[i]   =   [begin] + matrixInd[i]


# Generate merits and with repective individuals
ascendingIndMerits  =   [range(2) for y in range(line)]

for i in range(len(ascendingIndMerits)):
    ascendingIndMerits[i]   =   merit(matrixInd[i],coordCities)

ascendingIndMerits.sort()


# Calculate the Mean value and the Mean deviation
meanMerit[0], deviation[0], minMerit[0] =   dados(ascendingIndMerits)


## GENERATIONS ##
##########################
#auxMatrix   =   [range(line) for y in range(column)]
auxMatrix   =   [range(len(ascendingIndMerits))]
result      =   [range(2) for y in range(line)]


for i in range(len(ascendingIndMerits)):
    auxMatrix[0][i]    =   ascendingIndMerits[i][1]

while (count < iterations):
    for i in range(int(0.2*cities),int(0.4*cities)):
        auxMatrix[0][i]    =   auxMatrix[0][randint(int(0.2*cities),cities-1)]
        if (0 not in auxMatrix[0][i]): auxMatrix[0][i]    =   [begin] + auxMatrix[0][i]
    for i in range(int(0.4*cities),int(0.6*cities)):
        auxMatrix[0][i]    =   shift(int(0.3*cities),auxMatrix[0][i])
        auxMatrix[0][i].remove(0)
        auxMatrix[0][i]    =   [begin] + auxMatrix[0][i]
    for i in range(int(0.6*cities),int(0.8*cities)):
        random.shuffle(auxMatrix[0][i])
        auxMatrix[0][i].remove(0)
        auxMatrix[0][i]    =   [begin] + auxMatrix[0][i]
    for i in range(int(0.8*cities),cities):
        auxMatrix[0][i]    =   range(line)
        auxMatrix[0][i].remove(0)
        random.shuffle(auxMatrix[0][i])
        auxMatrix[0][i]    =   [begin] + auxMatrix[0][i]
    for i in range(len(auxMatrix[0])):
        result[i]  =   merit(auxMatrix[0][i],coordCities)
    meanMerit[count], deviation[count], minMerit[count] =   dados(result)
    count += 1
    
plt.plot(meanMerit)
plt.show()
