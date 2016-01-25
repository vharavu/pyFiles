import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
print(x)
# array([1, 2, 3])
y = np.arange(10)  # like Python's range, but returns an array
print(y)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.linspace(0, 2, 4)  # create an array with 4 equally spaced points starting with 0 and ending with 2.
print(b)
plt.figure(1)
plt.plot(b)
plt.ylabel("b")

onemore = np.linspace(-np.pi, np.pi, 50)
print(onemore)

a_sine_thing = np.sin(onemore)

plt.figure(2)
plt.plot(onemore)
plt.ylabel("onemore")

plt.figure(3)
plt.plot(a_sine_thing)
plt.ylabel("a_sine_thing")

plt.show()
