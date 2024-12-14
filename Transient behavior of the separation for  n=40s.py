import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(x,r):
    return r*x*(1-x)

# Parameters
r=3.2
x1=0.2  # Initial condition for trajectory 1
x2=0.20001 # Initial condition for trajectory 2
no_steps=40
delta=np.abs(x2-x1) # Initial separation

deltavalues=[delta]

# Calculations
for i in range(no_steps):
    x1=logistic_map(x1,r)
    x2=logistic_map(x2,r)
    delta=np.abs(x2-x1)
    deltavalues.append(delta) # Add the new value to the list

# Logarithmic separation
ln_deltavalues=np.log(deltavalues)

plt.figure(figsize=(8,5))
plt.plot(ln_deltavalues, linestyle='-', color='b',marker='o',label='n=40')
plt.xlabel('Step Number')
plt.ylabel('ln(Δ)')
plt.title('Transient Behavior of the separation')
plt.grid(True)
plt.legend()
plt.show()
