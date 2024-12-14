import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Parameters
r = 4.0  # Parameter for chaotic region
n_steps = 60  # Number of time steps
epsilon = 1e-8  # Small difference in initial conditions

# Initial conditions
x1 = np.random.random()
x2 = x1 + epsilon

# Arrays to store the values
x1_values = np.zeros(n_steps)  # Stores trajectory of x1
x2_values = np.zeros(n_steps)  # Stores trajectory of x2
delta_values = np.zeros(n_steps)  # Stores the difference |x1 - x2|

# Calculations
for i in range(n_steps):
    x1_values[i] = x1
    x2_values[i] = x2
    delta_values[i] = abs(x1 - x2)
    x1 = logistic_map(x1, r)
    x2 = logistic_map(x2, r)

# Logarithm of the difference
log_delta_values = np.log(delta_values)

# Fit a line to determine the Lyapunov exponent
fit_start, fit_end = 10, 50  # Define flexible fitting range
fit_range = slice(fit_start, fit_end)
slope, intercept = np.polyfit(np.arange(n_steps)[fit_range], log_delta_values[fit_range], 1)
lambda_exp = slope
K = np.exp(intercept)

# Calculation of fitted line values
fitted_values = slope * np.arange(n_steps) + intercept

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(range(n_steps), log_delta_values, label='ln(Δ)', color='blue')
plt.plot(range(n_steps), fitted_values, label=f'Fit: slope={lambda_exp:.3f}', color='red', linestyle='--')
plt.axhline(intercept, color='green', linestyle=':', label=f'Intercept={intercept:.3f}')
plt.xlabel('Step number (n)')
plt.ylabel('ln(Δ)')
plt.title('ln(Δ) vs Step number')
plt.legend()
plt.grid(True)
plt.show()

lambda_exp, K
