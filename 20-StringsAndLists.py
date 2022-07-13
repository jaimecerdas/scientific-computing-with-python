'''

'''
#Splitting

abc = "This is a sentence"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[3])

for w in stuff:
    print(w)

'''
split combins more than 1 space as 1 space

sometimes you need to split by something else.

use 

.split(";") to enter the delimiter
'''

#Double split

data = "this is an email hello@domain.com More info"

words = data.split()
print(words)
parts = words[4]
print(parts)
pieces = parts.split('@')
print(pieces)
domain = pieces[1]
print("Domain is: ", domain)

