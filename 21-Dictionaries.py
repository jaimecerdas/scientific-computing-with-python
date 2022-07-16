# Lists vs diccionary
#  linear collection of values
# a bag of value, no order, it has keys

'''
Associate arrays

Key value paris

'''

purse =  {}
purse['money'] = 12
purse['candy'] = 4
print(purse)

purse['candy'] = purse['candy'] + 3

print(purse)

# Applications ... how to create an histogram

counts = dict()
names = ['carlos','juan','jose','carlos','mario','mario']
for name in names:
    if name  not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# using get()

counts = dict()
names = ['carlos','juan','jose','carlos','mario','mario']
for name in names:
    counts[name] = counts.get(name, 0) + 1 # we need to add 1
print(counts)

# DIctionaries and loops.

text = open("Files/book.txt")
count = {}
words = []

for eachLine in text:
    words = words + eachLine.split()
print (words)

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

#LOOK at dictionaries

count = { 'chuck': 1, 'juan': 3, 'john': 5}
for key in count:
    print(key, count[key])

#Getting the list of Keys and Values

#Just keys
print(list(count))

print(count.keys())

print(count.values())
#Ask for items, gives a TUPLE 
print(count.items())

# Two iteration variables

count = { 'chuck': 1, 'juan': 3, 'john': 5}

for aaa, bbb in count.items():
    print(aaa,bbb)

#LARGEST VALUE IN A DIC

text = open("Files/book.txt")
count = {}
words = []

for eachLine in text:
    words = words + eachLine.split()
print (words)

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)