
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)


# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,


# lists to store x and y axis points
xdata, ydata = [], []
