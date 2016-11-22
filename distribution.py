"""
distribution.py
Author: xNimbleNavigatorx
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

s = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "' + s + '" is:')
print("a"*(s.count('a')))
print("b"*(s.count('b')))
print("c"*(s.count('c')))
print("d"*(s.count('d')))
print("e"*(s.count('e')))
print("f"*(s.count('f')))
print("g"*(s.count('g')))
print("h"*(s.count('h')))
print("i"*(s.count('i')))
print("j"*(s.count('j')))
print("k"*(s.count('k')))
print("l"*(s.count('l')))
print("m"*(s.count('m')))
print("n"*(s.count('n')))
print("o"*(s.count('o')))
print("p"*(s.count('p')))
print("q"*(s.count('q')))
print("r"*(s.count('r')))
print("s"*(s.count('s')))
print("t"*(s.count('t')))
print("u"*(s.count('u')))
print("v"*(s.count('v')))
print("w"*(s.count('w')))
print("x"*(s.count('x')))
print("y"*(s.count('y')))
print("z"*(s.count('z')))
sort.list