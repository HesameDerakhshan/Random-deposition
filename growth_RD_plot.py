
from random import randrange
import random
import matplotlib.pyplot as plt
import numpy as np
import math

H     = []

l     = 100
h     = np.zeros(l)
W_var = []
T     = []
t     = 16000
L     =range(0,l)	
j=1
pp=0
pR=0
pL=0

while (j<t):
#    StepSize=round(1 + 0.01 * t)
#    for c in range(StepSize):
    rand = randrange(l)
    h[rand%l] = h[rand%l]+1
    j = j + 1  

    #    	W_var.append(np.var(h))
    #    	T.append(j)


    if((j)%4000==0):
        H.append(h)    

		


#print('p',pp)
#print('pL',pL)
#print('pR',pR)

plt.stackplot(L,H)
#plt.legend(loc='upper left')
plt.show()
#plt.plot(T,W_var)
#plt.plot(h)



#p = np.polyfit(T,W_var,1) #fit kardan dade ba darage delkhah
#print (h)
#f = np.poly1d(p)
#print (f)
#plt.plot(T,W_var, 'bo', label="Data") # mokhtast data ha
#plt.plot(T,f(T), 'b-',label="Polyfit") # khat fit
#plt.show()
