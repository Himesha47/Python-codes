import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(r,x):   # r is the control parameter
    return r*x*(1-x)

# Input for the control parameter r
r = float(input("Input the value of r:"))

# Initializing the values
x0=0.5
n=100
x=np.zeros(n) # array to store sequence
x[0]=x0

#Generate the logistic map sequence
for i in range(1,n):
    x[i]=logistic_map(r,x[i-1])

#Ploting the Logistic map
plt.plot(range(n),x,'-o',color='b')
plt.title(f'Logistic Map for r={r}')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.ylim(0,1)
plt.show()