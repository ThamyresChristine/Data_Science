import numpy as np
a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [100,110,120]
    ])

print(a)

#Splitting Functions

#splits one array into multiple arrays
#print(np.split(a,2))

#splits one array into multiple arrays horizontally (column-wise)
#print(np.hsplit(a,5))

#splits one array into multiple arrays vertically (row-wise)
#print(np.vsplit(a,4))

#Adding and Removing
#returns  a resized version of array and fills empty spaces by repeating copies of 'a'
#print(np.resize(a,(4,4)))

#appeds values at the end
#print(np.append(a,[130,140,150]))

#insert a value at the index 'x'
#print(np.insert(a,0,5))

#delete axes
print(np.delete(a,1,1))

#Loading and saving arrays

#numpy format

c = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45],
    [50,55,60]
])

np.save('myaarray.npy',c)

d = np.load('myaarray.npy')

print(d)

#csv format

np.save('myaarray.csv', c)
"""
e = np.loadtxt('C:\\Users\\thamy\\Área de Trabalho\\VisualStudioCode\\myaarray.csv.npy')

e = np.loadtxt('myaarray.csv.npy')

e = np.loadtxt('myaarray.csv.npy', delimiter=';')

print(e)
"""

 

