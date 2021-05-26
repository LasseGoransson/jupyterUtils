from matplotlib import pyplot as plt
import numpy as np

def plot(x,y=None,title="",xlabel="",ylabel=""):
    plt.plot(x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
