import numpy as np
a = np.array([              # a 2x3 matrix
    [10,20,30],
    [40,50,60]
])

#returns the shape
print(a.shape)

#dimensions
print(a.ndim)

#amount of elements
print(a.size)

#data type of the values
print(a.dtype)

#Mathematical Operations

#Arithmetic (4)
print(a + 5)

print(a -1)

print( a *4)

print(a /2)

#operations between arrays
b = np.array([
    [1,2,3]
])

c = np.array([
    [1], [2]
])

print(b +c)

#Mathematical Functions(6)
#exp
print(np.exp(a))

#sin
print(np.sin(a))

#cos
print(np.cos(a))

#tan
print(np.tan(a))

#log
print(np.log(a))

#sqrt
print(np.sqrt(a))

#Aggregate functions - statistic
#sum of all values
print(a.sum())

#lowest value of array
print(a.min())

#highest value of array
print(a.max())

#arithmetic mean of all values
print(a.mean())

#median value of array
print(np.median(a))

#standard deviation of values
print(np.std(a))