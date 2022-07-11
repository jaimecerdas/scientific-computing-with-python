# Multi-way 

x = 10

if x < 2 :
    print("Less than 2")
elif x <= 10 :
    print("Less than 10")
else :
    print("Bigger than 10")
print ("FINISH")

# No else option
'''
You could have no answer
'''
# Many elifs
'''
The order is really important, it goes top to bottom.
'''
# Muti-way Puzzels
'''
When else or one of the elif is not needed because it is not
possible to get there.
'''

# TRY / EXCEPT STRUCTURE



test = "This is a string"
try:
    toprint = int(test)
except:
    test = -100

print ("First ",test)

test = 123
try:
    toprint = int(test)
except:
    test = -100

print ("Second ",test)