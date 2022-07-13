'''
(s[0:4])

is read s sub 0 tru 4
up to but not including 4

if you go over the available index it will not give an error

(s[:2]) since the beginning
(s[8:]) 8 to the end
(s[:]) everything

STRINGS CONCATENATION

print (x,y) adds an space
but

a = "Hello"
b = a + "hello" no space


IN as logical operator

fruit = "banana"
'n' in fruit

'''

fruit = "banana"
print('n' in fruit)

#String comparison
'''
it is possible but depends on the character set
of the computer.
Uper case and lower case are important 
for sorting.

String Library

string objects have some capabilities

'''

greet = 'HELLO'
zap = greet.lower()
print(greet)
print(zap)
print(greet.lower())

stuff = "hello"
dir(stuff)

#Search a String

fruit = 'hello John'
new = fruit.find("llo")
print(new)

#Search and replace

fruit = 'hello John'
new = fruit.replace("John","Juan")
print(new)

#Stripping Whitespace

text = "  space is huge     "
print(text.lstrip())
print(text.rstrip())
print(text.strip())

#Prefixes

line = "Starts with S"
print(line.startswith("S"))

#Parcing and extracting

data = "this is an email hello@domain.com More info"
atposition = data.find("@")
print(atposition)
spaceposition = data.find(" ",atposition)
print(spaceposition)
host = data[atposition + 1 : spaceposition]
print (host)
