#create a string
nom1 = "Hello Beautiful World"

nom2 = "It's a Beautiful World"
#escape characters (4)

#backspace
print(nom1 + '/b' + nom2)
#new line
print(nom1 + '/n' + nom2)
#space
print(nom1 + "/s" + nom2)
#tab
print(nom1 + "/t" + nom2)
#formating(5)

#character
nom3 = 10
#string
nom4 = str(nom3)
print(type(nom4))
#integer

#float

#exponential notation

#case manipulating (5)

#pequeno
e = nom2.lower()
print(e)
#grande
d = nom1.upper()
print(d)
#título
c = nom2.title()
print(c)
#capitular
a = nom1.capitalize()
print(a)
#lower case becomes upper case and vice versa
b = nom2.swapcase()
print(b)

#Some functions(5)

#count how many times a specific string occurs in another string

#find the str
print(nom1.find("Hello"))

#join the str

#replace the str

#split the str

#triple quotes
"""Escape Characters: nom-printable characters like tab or new line. They all iniated by a backslash, 
    wich is the reason why we need to use DOUBLE backslashes for file paths
"""

#for more: W3 Schools