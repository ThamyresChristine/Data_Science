import numpy as np
a = np.array([
 [4,2,9],[8,3,2]
])

print(a)

a[1][2] = 7         #linha e coluna

print(a)

#Shape Manipulation Functions

#returns the array with the same values structured in a different shape
#print(a.reshape(1,2))

#returns a flattened one-dimensional copy of the array
#print(a.flatten())

#does the same of flatten but works with the actual array instead of a copy
#print(a.ravel())

#returns an array with the same values but swapped dimensios
print(a.transpose())

#returns an array with the same values but two swapped axes
print(a.swapaxes(1,1))

#an iterator for the flatted version of array
#print(a.flat)

#we can iterate flat with for loop
#for x in a.flat:
#    print(x)

#Joining functions          #3 parenthesis
b = np.array([10,20,30])

c = np.array([40,50,60])
             
#joins multiple arrays along an existing axis
print(np.concatenate((b,c)))

#joins multiple arrays along a new axis
print(np.stack((b,c)))

#stacks the arrays horizontally (column-wise)
print(np.hstack((b,c)))

#stacks the arrays vertically (row-wise)
print(np.vstack((b,c)))

