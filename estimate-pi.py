
# coding: utf-8

# This is a program that calculates an estimation of Pi using Monte Carlo distribution.

# In[7]:

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

# We drew a square, and then a circle within that square whose diameter is equal to the length of the side of the square. For every trial, we threw six magnetic balls at this figure. We recorded the number of magnets that landed inside the circle, and the ones that landed outside of the circle (but still inside the square). This gives us an estimation of the ratio of the area of the circle to the area of the square. If the radius of the circle is r, then the area of the circle is Pi(r2), and the area of the square is 4(r2), thus the ratio of the area of the circle to the area of the square is Pi/4. Therefore, multiplying the estimated ratio we got from throwing the magnets by four will give us an estimation of Pi.

We recorded 25 sets of throws (6 throws/set). It took us about 30 minutes to do the 25 sets. Graphing all 25 ratios, then drawing an exponential line of best fit, we can see that after 25 throws, the estimation of Pi decreases from 3.7 to 3.5, so by calculating the slope of the line of best fit:

(3.7 - 3.5) / (25 - 1) ≈ -0.0087

Then we can see that the number of throws needed for the graph to start converging to the value of Pi is:

25 - ( (3.5 - 3.14) / (-0.0087) ) ≈ 67 (throws)

which should take around 80 minutes.

By graphing the estimations of pi after every magnet throwing simulation, we can see when the graph starts converging to the real value of pi (~3.14). We see that this happens after around 200 magnets thrown, which will equal about 4 hours of throwing magnets in real life.