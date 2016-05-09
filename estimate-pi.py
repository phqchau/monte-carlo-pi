# Copyright 2016, Chau Pham

# This is a program that calculates an estimation of Pi using Monte Carlo distribution.

import math
import numpy as np
import statistics
from scipy.integrate import quad
import random
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# Time estimation 
y = [(5/6),(11/12),(16/18),(22/24),(28/30),(34/36),(40/42),(46/48),(50/54),(55/60),(61/66),(66/72),(72/78),(77/84),(80/90),(86/96),(91/102),(97/108),(102/114),(106/120),(110/126),(115/132),(121/138),(126/144),(130/150)]
x = list(range(1, 26))
y = [i*4 for i in y]

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)

plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
plt.xlabel("Number of times 6 magnets were thrown")
plt.ylabel("Estimation of Pi")
plt.show()


# Throwing magnets at a circle within a square
def piEstimate():
    areaValue = random.uniform(0,4)
    return areaValue

x = 0
circleCount = 0
squareCount = 0
piEstList = []

while x < 200:
    result = piEstimate()
    x+=1
    if result < math.pi:
        circleCount+=1
    if result > math.pi:
        squareCount+=1
    piEst = 4*((circleCount)/x)
    piEstList.append(piEst)

print("The number of magnets that landed inside of the circle is:",circleCount)
print("The number of magnets that landed outside of the circle is:",squareCount)

print("The final estimation of Pi is:",piEst)

plt.plot(piEstList)
plt.ylabel('Estimation of Pi')
plt.xlabel('Number of magnets thrown')
plt.show()


# Shiflet and Shiflet, module 9.2, project 4
def circleArea(x):
    radius = 1
    y = math.sqrt(1-(x**2))
    return y

def piEstimate(_n):
    counter = 0
    circleCount = 0
    
    while counter < _n:
        randomX = random.uniform(0,1)
        randomY = random.uniform(0,1)
        counter+=1
    
        if randomY < circleArea(randomX):
            circleCount+=1
    
    piEst = 4*((circleCount)/(counter))

    return piEst

x = np.linspace(0,1,100)
y = np.sqrt(1-(x**2))
plt.plot(x, y)
plt.xlabel('Graph of quarter II of function x^2 + y^2 = 1')
plt.show()

n = eval(input("Enter the number of magnets thrown: "))
print("The estimation of Pi, based on", n, "magnets thrown, is:", piEstimate(n))

def rangePiEst():
    counter = 0
    piEstList = []
    
    while counter < 1000:
        piEst = piEstimate(n)
        piEstList.append(piEst)
        counter+=1
    
    piMean = statistics.mean(piEstList)
    print("The mean of the estimations, based on throwing",n, "magnets 1000 times, is:",piMean)
    piStDev = statistics.stdev(piEstList)
    print("The standard deviation of the estimations is:",piStDev)
    abserror = (math.pi)-(piMean)
    print("The absolute error is:",abserror) 
    percenterror = ((piStDev)/(math.pi))*100
    print("The percentage error is:",percenterror,"%")
    
rangePiEst()

def integrand(x):
    return math.sqrt(1-(x**2))

calcPi, err = quad(integrand, 0, 1)
print("The actual value of Pi, calculated by integration, is:", calcPi*4)
