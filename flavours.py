import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

#function to plot the three flavours of Big O
def plot_big_o():
    #input size range
    n = np.linspace(1, 10, 100)

    #define the three flavours of big O
    constant = np.ones_like(n)
    logarithmic =np.log(n)
    linear = n

    #plot the threee flavours
    plt.plot(n, constant, label='0(1)- Constant')
    plt.plot(n, logarithmic, label='0(log n)- logarithmic')
    plt.plot(n, linear, label='O(n)-Linear')

    #set plot properties
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Complexity')
    plt.title('Comparison of Big O Notation')
    plt.legend()

    #display the plot
    plt.show()
#call the  function to display the graph
plot_big_o()