import math as m
import numpy as np 

def add(x,y):
    result = x+y
    print(result)

add(4,9)
add(7,10)
add(18,9)

def iterate(x):
    if x ==5:
        for _ in range(5):
            print("Hello python")
    else:
        print("Out of order")

iterate(7)

def square(x):
    return x**2
print(square(4))


man = m.sqrt(64)
print(int(man))

guess = round(np.random.rand() * 10)
print(guess)