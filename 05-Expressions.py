'''
+ addition
- substraction
* multiplication
/ Division
** Power
% Remainder "Modulo"

Operator precedence / Order of Evaluation

Parentheses
Exponentiation
Multiplication Division Remindar
Addition and Substraction
Left to right

TYPE OF DATA

Integer
float
String

Operator knows what type of variables are used.


type() --> tells what type of variable it is.
float() converts to float

Integer division produces a floating point result.

int()  converts to int

input() gets input


'''

x = 6
print(type(x))

y = 7
print(float(y))

z = "123"
v = int(z)
print (type(v))

text = input('Whats up? ')


#Elevator convertor program

imp = input ("What is your level?")
usf = int(imp) + 1
print('Usf floor is', usf)