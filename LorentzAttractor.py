#------Importing the libraries-------------
import numpy as np  #standard way import beacuse of numerical computations
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing this for 3D plot
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint #used to solve system of ODEs
#--------------Defining the constants------------
#parameters specific to the system of ODEs
sigma=10
beta=8/3
rho=28

#-------------------Solving the system numerically----------
# Defining the function
def System_of_ODEs(vector,t,sigma,beta,rho):
    x,y,z=vector
    dxdt=sigma*(y-x)   #Given ODEs
    dydt= x*(rho-z)-y
    dzdt=x*y-beta*z
    return [dxdt,dydt,dzdt]

position_0_1=[0.0,1.0,1.0] #Position 1 at t=0 [x,y,z]
position_0_2=[0.0,1.1,1.0] #Position 2 at t=0 [x,y,z]

time_points=np.linspace(0,40,1001) #an array of 1001 time values evenly spaced between 0 and 40 #S1001 is when t=40

position_1=odeint(System_of_ODEs, position_0_1, time_points,args=(sigma,beta,rho)) #The args parameter is a tuple containing passed to the ODE function
position_2=odeint(System_of_ODEs, position_0_2, time_points,args=(sigma,beta,rho))
#2D array where each row represents the state [x, y, z] at a specific time point
x_sol_1=position_1[:,0] #extracts the first column,values of x at each time point
y_sol_1=position_1[:,1] #extracts the second column,values of y at each time point
z_sol_1=position_1[:,2] #xtracts the third column,values of z at each time point

x_sol_2=position_2[:,0] 
y_sol_2=position_2[:,1] 
z_sol_2=position_2[:,2]

#-------------Plotting the solution------------
fig = plt.figure() #creates a new figure where the plot will be drawn
ax = fig.add_subplot(111, projection='3d')#adds a 3D subplot to the figure

lorentz_plt_1, = ax.plot([], [], [], lw=0.5, color='red')  # Empty 3D plot line with line width of 0.5 and red color
ax.set_xlim([min(x_sol_1), max(x_sol_1)])#limits of the X-axis based on the minimum and maximum values
ax.set_ylim([min(y_sol_1), max(y_sol_1)])
ax.set_zlim([min(z_sol_1), max(z_sol_1)])

lorentz_plt_2, = ax.plot([], [], [], lw=0.5, color='blue')#empty 3D plot line with line width of 0.5
ax.set_xlim([min(x_sol_2), max(x_sol_2)])#limits of the X-axis based on the minimum and maximum values
ax.set_ylim([min(y_sol_2), max(y_sol_2)])
ax.set_zlim([min(z_sol_2), max(z_sol_2)])
ax.set_xlabel('X Axis')#Labels the X-axis
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Lorenz Attractor')#Sets the title of the plot

#-------------Animating the solution--------------
def update(frame):
    lorentz_plt_1.set_data(x_sol_1[:frame], y_sol_1[:frame])#Updates the X and Y data to show the solution up to the current frame
    lorentz_plt_1.set_3d_properties(z_sol_1[:frame])#Updates the Z data to show the solution up to the current frame

    lorentz_plt_2.set_data(x_sol_2[:frame], y_sol_2[:frame])
    lorentz_plt_2.set_3d_properties(z_sol_2[:frame])

    return lorentz_plt_1,lorentz_plt_2#Returns the updated line objec

global anim #global variable
anim = FuncAnimation(fig, update, frames=len(time_points), interval=25) #frames=len(time_points): The total number of frames, equal to the length of time_points 
plt.show()                                                                         #interval=25: The delay between frames in milliseconds.
                                                                                   