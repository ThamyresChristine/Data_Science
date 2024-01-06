import numpy as np

a = np.array([10,20,30])
b = np.array([1,77,2,3])

#access the values
print(a[0])
print(b[2])

#multi-dimensional arrays

a = np.array([              # a 2x3 matrix
    [10,20,30],
    [40,50,60]
])

print(a)

print(a[1][2])          #addressing the second row and the third element

#filling arrays
b = np.array([
    [
        [10,20,30,40], [8,8,2,1], [1,1,1,2]
    ],
    [
        [9,9,2,39], [1,2,3,3], [0,0,3,2]
        
    ],
    [
        [12,33,22,1], [22,1,22,2], [0,2,3,1]
    ]
    
], dtype=float)

print(b)

#full function

c = np.full((3,5,4),7)

print(c)

#zeros and ones

a1 = np.zeros((3,3))

b1 = np.ones((2,3,4,2))

print(a1)
print(b1)

#empty and random

a2 = np.empty((4,4))

b2 = np.random.random((2,3))

print(a2)
print(b2)

#ranges - arange and linspace

a = np.arange(10,50,5)
print(a)

b = np.linspace(0,100,11)
print(b)

