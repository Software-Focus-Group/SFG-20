import numpy
from datetime import datetime
import random 

#making numpy array of random numbers frmo -1 to 1
A = numpy.random.randn(10000)
B = numpy.random.randn(10000)
T = 50000


#making list of random number from -1 to 1
la = [random.randrange(-1, 1, 1) for i in range(10000)]
lb = [random.randrange(-1, 1, 1) for i in range(10000)]

#defining a function to do dot product
def slow_dot_product(a, b):
    result = 0
    for i,j in zip(a, b):
        result += i + j
    return result

#defining a function to do dot product woth list
def slower_dot_product(a, b):
    result = 0
    for i,j in zip(a,b):
        result += i + j
    return result

#time for list with list function
t0 = datetime.now()
for i in range(T):
    k =slower_dot_product(la, lb)
tl = (datetime.now() - t0).total_seconds()

#time for numpy array with user function
t0 = datetime.now()
for i in range(T):
    k =slow_dot_product(A, B)
tsa = (datetime.now() - t0).total_seconds()

#time for numpy array with numpy functions
t0 = datetime.now()
for i in range(T):
    k =A.dot(B)
ta = (datetime.now() - t0).total_seconds()

print('python list : {}\n numpy array user function : {}\n numpy array with numpy function : {}'.format(tl, tsa, ta))