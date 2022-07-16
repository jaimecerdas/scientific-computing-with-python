#TUPLES
'''
Tuples are immutable, cannot be modified.
They cannot be:
.sort()
.append()
.reverse()
nothing that modifies as you would do with a list

You ca do:
-count
-list

but...

Tuples are more efficient
Better memory use

When to use? When you are not planning on modify.

You can assign more than one at the time
'''


(a, y) = (4, 'fred')
print(a)

#Tuples and dictionary

d = dict()
d['one'] = 2
d['two'] = 4

for (k, v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

#compare tuples

'''
It goes one by one, first answer gives true
'''

a = (1,3,4)
b = (1,2,4)

print(a>b)
print(a<b)

#COMPARING AND SORTING TUPLES

#Sorting Dictionaries

d = {'a': 10, 'c':5,'b':2}
print(d.items())
print(sorted(d.items()))

#iterate using the sorted dictionary

for k, v in sorted(d.items()):
    print (k,v)

# Sort by value instead of Key

d = {'a': 10, 'c':5,'b':2}
temp = list()

for k, v in d.items():
    temp.append((v,k))

print(temp)
temp = sorted(temp,reverse=True)
print(temp)

# Print top most common words

fhand = open("Files/book.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k,v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst,reverse=True)

for v, k in lst[:10]:
    print(k, v)

# Shorter Version to sort 

d = {'a': 10, 'c':5,'b':2}

print(sorted([(v,k) for k, v in d.items()], reverse=True))

