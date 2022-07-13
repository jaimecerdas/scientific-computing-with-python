#OPERATIONS

#CONCATENATING LOOPS

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#slicing

a = [1,2,3,99,103,204]
x = a[1:3]
y = a[:2]
z = a[3:]
xx = a[:]

print(a)
print(x)
print(y)
print(z)
print(xx)

#List Methods
dir(x)

#building a list from Scratch

stuff = list()
#create a list

stuff.append("book")
stuff.append(99)

#in operator

print(8 in stuff)

#sort lists
names = ["a","j","b"]

names.sort()
print(names)

#Functions
'''
len how many 
max largest
min smalles
sum sum
average sum/len

'''


numlist = list ()
while True:
    inp = input ("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
print("Average is: ",sum(numlist)/len(numlist))