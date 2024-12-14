import numpy as np
import matplotlib.pyplot as plt

# Parameters
n=10000 # No of r values to stimulate
r_min, r_max = 2.5, 4.0
r = np.linspace(r_min, r_max, n) # Array for control parameter 
iterations=10000
last=100 # no of final iterations

# Initial condition
x = 1e-5 * np.ones(n)

# Logistic map iteration
for i in range(iterations):
    x=r*x*(1-x) # Logistic map equation

    # Plotting the bifurcation diagram
    if i>= (iterations-last):  # Only plot the last 100 iterations
        plt.scatter(r,x,s=0.1,c='k',alpha=0.25) 

# Add grid to the plot
plt.grid()

# Display the bifurcation diagram
plt.xlim(2.5,4)
plt.title("Bifurcation Diagram")
plt.xlabel("r")
plt.ylabel("x")
plt.show()
