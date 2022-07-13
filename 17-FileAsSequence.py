xfile = open ("Files/newfile.txt")
for eachLine in xfile:
    print(eachLine)

#counting lines
file = open ("Files/newfile.txt")
count = 0
for theLines in file:
    count = count + 1
print(count)

#Reading the whole file

reading = open ("Files/newfile.txt")

inp = reading.read()
print("The # of characters are",len(inp))

#Searching on a file

text = open("Files/newfile.txt")
for eachLine in text:
    if eachLine.startswith("this"):
        print(eachLine.rstrip())

# .rstrip() removes the \n that print adds

text = open("Files/newfile.txt")
for eachLine in text:
    eachLine = eachLine.rstrip()
    if eachLine.startswith("this"):
        print(eachLine)
        print("END")

#Using in to selec line

text = open("Files/newfile.txt")
for eachLine in text:
    eachLine = eachLine.rstrip()
    if not "this" in eachLine:
        continue
    print(eachLine)

#Prompt for file name as input

#fname = input("Enter the file name: ")
#fhand = open(fname)

#fix bad names & use of quit()

filename = input("Enter the file name:   ")
try:
    fhand = open(filename)
except:
    print("File cannot be opened: ", filename)
    quit()

for eachLine in fhand:
    print(eachLine)

    