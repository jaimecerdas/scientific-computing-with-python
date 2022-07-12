'''
Indexing Strings, each caracter has a position.
Letters have positions.

Index operator is []


'''
x= 2
fruit = 'banana'
print (fruit[2])
print (fruit[x-1])

# len

print (len(fruit))

#loop strings

fruit = 'banana'
index = 0
while index < len(fruit):
    print(index,fruit[index])
    index += 1

for letter in fruit:
    print(letter) 

# counting a caracter.
count = 0
for letter in fruit:
    if letter == 'a' :
        count += 1
print(count) 

