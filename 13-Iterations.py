#Counting in a loop

count = 0
for thing in [1 ,4 , 5 ,7 , 8] :
    count += 1
print(count)

#Total of a loop

total = 0
for thing in [1 ,4 , 5 ,7 , 8] :
    total  = thing + total
print(total)

#Total of a loop

total = 0
count = 0
for thing in [1 ,4 , 5 ,7 , 8] :
    total  = thing + total
    count += 1
average = total/count
print(average)
print (total/count)

#filtering in a Loop

print("Before")
for value in [3, 45, 21, 7, 14]:
    if value > 20:
        print("Large number ", value)
print ("After")

#Search Using a Boolean Variable

found = False
print ('Before', found)
for value in [32, 45, 21, 3, 14]:
    if value == 3 :
        found = True
        print('found',value)
        break
print('After',found)

#How to find the smallest value

smallest = 100
for number in [3,41,12,9,74,15]:
    if number < smallest:
        smallest = number
print(smallest)

#but this is not a good solution... we should use the first number to start

# None Type ... empty, non existance

smallest = None
for number in [3,41,12,9,74,15]:
    if smallest is None:
        smallest = value
    elif number < smallest:
        smallest = number
print(smallest)

