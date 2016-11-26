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

f = [s.count("a"), s.count("b"), s.count("c"), s.count("d"), s.count("e"), s.count("f"), s.count("g"), s.count("h"), s.count("i"), s.count("j"), s.count("k"), s.count("l"), s.count("m"), s.count("n"), s.count("o"), s.count("p"), s.count("q"), s.count("r"), s.count("s"), s.count("t"), s.count("u"), s.count("v"), s.count("w"), s.count("x"), s.count("y"), s.count("z")]
combo = zip( f ,['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
print(combo)

list.sort()
(list[::-1])

