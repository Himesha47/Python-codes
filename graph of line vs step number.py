import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(x,r):
    return r*x*(1-x)

# Parameter
# Parameter for logistic map in the chaotic region
r=4.0 # Chaotic region
n_steps=100 # Number of time steps
epsilon = 1e-8 # Small initial difference

# Initial conditions
x1=np.random.random()
x2=x1+epsilon

# Array to store the values
x1_values=np.zeros(n_steps) # Store trajectory of x1
x2_values=np.zeros(n_steps) # Store trajectory of x2
delta_values=np.zeros(n_steps) # Store the separation 

# Calculation of the evolution
for i in range (n_steps):
    x1_values[i]=x1
    x2_values[i]=x2
    delta_values[i]=abs(x1-x2)
    x1=logistic_map(x1,r)
    x2=logistic_map(x2,r)

# Logarithm of the difference
eps = 1e-10
log_delta_values = np.log(delta_values + eps)

# Plotting the graph
plt.figure(figsize=(10,5))
plt.plot(range(n_steps), log_delta_values, label='ln(Δ)')
plt.xlabel('Step number(n)')
plt.ylabel('ln(Δ)')
plt.title('ln(Δ) vs Step number(n)')
plt.legend()
plt.grid(True)
plt.show()

# A linear fit to determine the Lyapunov exponent
fit_range = slice(10,50) # To ignore transient behavior
slope,intercept=np.polyfit(np.arange(n_steps)[fit_range],log_delta_values[fit_range],1)
lambda_exp = slope # Lyapunov exponent
K=np.exp(intercept) # Scaling factor

lambda_exp,K