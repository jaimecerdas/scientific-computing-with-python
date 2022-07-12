#Making "smart" loops

'''
For THING in data...

Run data to find something

'''
largest = -1
for number in [3,41,12,9,74,15]:
    if number > largest:
        largest = number
print(largest)