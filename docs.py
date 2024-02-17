# COMMENTS
# this is a commment

"""
this is a
multi line
comment
"""

# LIBRARIES
import math
import random
from time import sleep

# PRINTING
print("hello")


# VARIABLES
string = "cool string"

int = "20"

float = "20.5"

boolean_a = True

boolean_b = False


# STORING DATA
int_list = [1, 4, 7, 8, 2, 3]

string_list = ["neutral", "alright", "bland"]

boolean_list = [True, True, False, True, False]


int_tuple = (2, 3, 5, 1, 3)

string_tuple = ("mad", "angry", "heat")

boolean_tuple = (False, False, True, True, False)


int_set = {1, 5, 7, 9, 3}

string_set = {"happy", "calm", "cool"}

boolean_set = {True, False, False}


data_dictionary = {
  "brand": "Lamborghini",
  "model": "Huracan",
  "type": "LP-610-4",
  "gas": True,
  "electric": False,
  "year": 2015,
  "colors": ["white", "black", "gray"]
}


"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
Dictionary is a collection which is ordered and changeable. No duplicate members.

You can still add/remove items from a set.
"""


# MATH
add = 2 + 3 # 5

subtract = 9 - 5 # 4

multiply = 3 * 4 # 12

divide = 30 / 5 # 6

modulus = 5 % 2 # 1 (remainder)

exponent = 2 ** 5 # 32 (2⁵)

divide_decimal = 15 // 2 # 7 (rounds it)


# OPERATORS
x = 1
y = 1
z = 3

x == y # x equals y

x != z # x not equal to z

z > x # z greater than x

z >= y # x greater than or equal to y

y < z # x less than z

x <= z # x less than or equal to z

y and x # get x and y

x or z # get x or z

z = not(x) # returns True


# CONDITIONALS
if x == y:
    print("x equals y") # if condition is met

elif x != y:
    print("x doesn't equal y") # else if condition is met

else:
    print("x doesn't equal anything!") # else condition is met

if z > x:
    pass # 'pass' keyword used to do nothing, just move on
    if x == y:
       print(x) # nested conditional


# LOOPS
i = 0
while i < 5:    # repeat till i is not 5
    print(i)    # print i: 0, 1, 2, 3, 4
    i += 1      # increment i by 1

while i < 6:
  print(i)
  if i == 3:
    break # break out of loop if i = 3
  i += 1 # do only this after loop broke

while i < 6:
  i += 1
  if i == 3:
    continue # countine loop  if i equals 3
  print(i)


# remember that int_list = [1, 4, 7, 8, 2, 3]
for a in int_list:
   print(i) # prints every number in list in new lines

for b in "name":
   print(i) # loops through a string and prints each character in new lines

for c in range(6):
   print(c) # uses the range function and prints numbers 0 to 6 exclusively

for d in range(2, 6):
   print(d) # same process but between the range of 2 and 6 exclusively

for e in range(0, 10, 2):
   print(e) # same process between an inclusive range of 0 and 10 but increments each iteration by 2


# remember that boolean_list = [True, True, False, True, False]
for i in range(len("string")):
   for j in boolean_list:
      print(i, j) # nested for loops


# FUNCTIONS
def f(x):
   y = x + 2
   return y # 'return' keyword returns y value with passed in x-value

f(5) # calling function with x = 5

# READING FILES
with open('file.txt', 'r') as reader:
   print(reader.readlines())

# COMMON METHODS
len("string") # get length of string

input("Enter an input: ") # get input from user

min(3, 1) # returns minimum value: 1

max(2, 4) # returns maximum value: 4

sum(int_list) # sums up all values: 25

round(5.76543, 2) # rounds given number by 2 place: 5.77

pow(4, 3) # exponentation: 64

pow(4, 3, 5) # exponentation with remainder: 4

str(4223) # typecasts int to str, you can do this with any other datatype as well


# LIST METHODS
methods_list = [5, 6, 7, 7, 7, 2, 9, 3]

methods_list.append(2) # append an element

copy_of_ML = methods_list.copy() # copies list

methods_list.count(7) # counts how many elements are of argument is in list

methods_list.extend(int_list) # extends list by appending another list to the current list

methods_list.index(9) # get index position of a element

methods_list.insert(1, 3) # insert in list at a specific index of 1 or any desired index

methods_list.pop(5) # removes an element at whatever index it's located at (5)

methods_list.remove(7) # removes the first occurence of the element without indexing

methods_list.reverse() # reverses list

methods_list.sort(reverse=True) # descends list by sort method argument

methods_list.sort(reverse=False) # ascends list by sort method argument

methods_list.clear() # clears list