import matplotlib.pyplot as plt
import numpy as np
from random import uniform

'''
objects = [(-1, 0, 1),
           (1, 1, 1),
           (2, 0, 2),
           (1, -2, 2)]


'''
objects = [(-1, 0, 1),
           (1, 1, 1),
           (5, -1, 1),
           (2, -3, 2),
           (1, -2, 2),
           (2, 2, 2)]

def f(coef, x):
    return coef[0] + coef[1] * x[0] + coef[2] * x[1] + coef[3] * x[0] * x[1]

def update_coef(coef, x, p):
    return (coef[0] + p * 1, coef[1] + p * 4 * x[0], coef[2] + p * 4 * x[1], coef[3] + p * 16 * x[0] * x[1])

def init_func(coef):
    def f(x):
        return -(coef[0] + coef[1] * x) / (coef[2] + coef[3] * x)
    return f

def init_func2(coef):
    def fxy(x, y):
        return coef[0] + coef[1] * x + coef[2] * y + coef[3] * x * y
    return fxy

def algorythm():
    max_iter = 100
    p = 1
    coef = (0, 0, 0, 0)
    length = len(objects)

    for _ in range(max_iter):
        flag = True
        for i in range(length):
            coef = update_coef(coef, objects[i], p)
            next_object = objects[(i + 1) % length]
            res = f(coef, next_object)
            if (next_object[2] == 1 and res <= 0):
                p = 1
                flag = False
            elif (next_object[2] == 2 and res > 0):
                p = -1
                flag = False
            else:
                p = 0

        if flag:
            break
    
    return coef


coef = algorythm()
sep_func = init_func(coef)
if (coef[3] != 0):
    x_break = -coef[2] / coef[3]
else:
    x_break = 10.01

x1 = np.arange(-10, x_break, 0.01)
plt.plot(x1, sep_func(x1), color='blue')

x2 = np.arange(x_break + 0.01, 10.01, 0.01)
plt.plot(x2, sep_func(x2), color='blue')

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$y_1$')
plt.title("Разделяющая функция")
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-3, 3)

sep_func2 = init_func2(coef)

for i in range(250):
    x = uniform(-5, 5)
    y = uniform(-3, 3)
    if (sep_func2(x, y) > 0):
        plt.scatter(x, y, color='white', edgecolor='black')
    else:
        plt.scatter(x, y, color='black')

plt.show()



