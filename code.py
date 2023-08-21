import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

#variables
#D : distance to screen
#b : aperture size
#WaveL: Wavelength
y = np.arange(-0.1,0.1,0.00001)

def plot(D, b, WaveL):
    k = (2*np.pi)/(WaveL*1E-09)
    theta = y/D
    Beta = (1/2)*k*(b*1E-03)*np.sin(theta)
    Amp = (np.sin(Beta))/Beta
    I_P = Amp**2
    plt.plot(y,I_P)
    plt.xlim(-0.1,0.1)
    plt.show()
    
interactive(plot, D=(0.01,5.0,0.1), b=(0.001,1,0.01), WaveL=(400,700,1.0))
