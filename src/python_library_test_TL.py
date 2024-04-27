import math
import matplotlib.pyplot as plt


def sinOfCos(x):
    return math.sin(math.cos(x))

def plotSinOfCos(n):
    x = [i/100 for i in range(n)]
    y = [sinOfCos(i) for i in x]
    plt.plot(x, y)
    plt.show()

