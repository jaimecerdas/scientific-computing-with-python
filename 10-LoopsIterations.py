n = 5

while n > 0 :
    print(n)
    n = n - 1
print ("Finish")

'''
Use a Iteration variable so we don't run the loop for ever.

'''
# BREAKING OUT OF THE LOOP

while True :
    line = input ('> ')
    if line == 'done':
        break
        #break breaks the loop and send to the line at the end of the loop
    print(line)
print("done!")

# USING CONTINUE

while True :
    line = input('> ')
    if line[0] == '#':
        continue
    if line == "done":
        break
    print(line)
print("Done!")

'''
Indefinite loops: Use while loops, run while...
Next definite loops.
'''