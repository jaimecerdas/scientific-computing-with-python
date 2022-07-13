'''
DATA STRUCTURES

Variables
x = 2

where 2 is replaceable

COLLECTIONS

carryon = ["one", "two", "Three"]

LISTS have square brackets.
A list element can be another list.
It can combine different types

Lists and definite loops are BEST PALS


'''

carryon = ["one", "two", "Three"]
print(carryon[0])

#LISTS ARE MUTABLE, STRINGS ARE NOT

muchasList = [123, 124, 125]
print(muchasList)
muchasList[1] = 999
print(muchasList)

# LEN of listas

print(len(muchasList))

print(range(2))
print(range(len(muchasList)))

for i in range(len(muchasList)):
    print("this is the iteration num:",i,"#",muchasList[i])

