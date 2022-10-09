import matplotlib.pyplot as pyplot
import numpy as np

X = np.linspace(-1000, 1000, 3000, endpoint=True)

C, S = X**2 , X**3

pyplot.plot(X, C)
pyplot.plot(X, S)
pyplot.show()

