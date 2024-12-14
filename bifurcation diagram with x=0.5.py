import numpy as np
import matplotlib.pyplot as plt

# Parameters
n=10000
r=np.linspace(2.5,4.0,n) # Control parameters
iterations=1000
last=100

# Initial condition
x=1e-5*np.ones(n)

# Storage for the Lyapunov exponent
lyapunov=np.zeros(n)

# Simulation
for i in range(iterations):
    x=r*x*(1-x) # Logistic map equation
    eps = 1e-10  # Small offset to prevent log(0)
    lyapunov += np.log(abs(r - 2 * r * x) + eps)

    # Plotting the bifurcation diagram
    if i>=(iterations-last):
        plt.plot(r,x,'k',alpha=0.25)

plt.xlim(2.5,4)
plt.title("Bifurcation Diagram")
plt.axhline(0.5,color='b',linestyle='--',label='Stable Fixed Point at x=0.5')
plt.xlabel("r")
plt.ylabel("x")
plt.show()

lyapunov /= iterations  # Average over the number of iterations

# Plot the Lyapunov exponent
plt.plot(r, lyapunov, 'r', label='Lyapunov Exponent')
plt.axhline(0, color='k', linestyle='--', label='Zero Lyapunov')
plt.xlabel("r")
plt.ylabel("Lyapunov Exponent")
plt.title("Lyapunov Exponent vs r")
plt.legend()
plt.show()
