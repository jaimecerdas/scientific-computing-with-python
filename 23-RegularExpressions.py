#Regular Expressions

'''
Also refer as regex, regexp

wild card expressions for matching and parcing

you need to import re
'''

import re

hand = open("Files/book.txt")
for line in hand:
    line = line.rstrip()
    if re.search('^The', line):
        print(line)

# ^ beginning of line

# . wild card

#Regular Expressions: Matching and Extracting Data

'''
re.search() returns true/false

re.findall() all matches will be extracted.

[0-9] any number from 0 to 9



'''

import re

x = 'From: Using the : character'
greedy = re.findall('^F.+:', x)
nonGreedy = re.findall('^F.+?:', x)
print (greedy)
print (nonGreedy)

#find emails

y = re.findall('\S+@\S+', x)

#IN regular expressions, the ( ) determines what is going to be extracted
y = re.findall('From (\S+@\S+)', x)

#PRACTICAL APPLICATIONS

text = "From jaime@domain.com Sat Jan 5 5 09:14"

import re
y = re.findall('@([^ ]*)', text)
print(y)

y = re.findall('From .*@([^ ]*)', text)
print(y)

# use \ when using one of the special caracters used in search


