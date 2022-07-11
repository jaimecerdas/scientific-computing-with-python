def myown():
    print("this is line 1")
    print("line 2")

# def does not do anything at the time, until you invoque them

print("It's starting")
myown()
print("It's done, now again: ")
myown()

#Passing parameters

def newfunction(word):
    if word == "yes":
        print("si")
    if word == "no":
        print("no pero en espanol")

newfunction("no")

#Return values

def green():
    return("Hello")

print(green(),"Jaime")