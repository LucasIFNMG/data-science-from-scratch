# -*- coding: utf-8 -*-
""" CHAPTER 2: A Crash Course in Python"""

""" FUNCTIONS """

def double(x):
    """this function does that thing"""
    return x*2

def apply_to_one(f):
    """calls the function f with 1 as its argument"""
    return f(1)

my_double = double

# Assigning a variable passing a function
x = apply_to_one(my_double)

# Lambda function
y = apply_to_one(lambda x: x+4)

def another_double(x): return 2 * x

double2 = another_double(x)


# Default
def my_print(message = "default message"):
    print (message)
    
my_print()

def substract(a = 0, b = 0):
    return a - b

subs = substract(10, 5)


""" EXCEPTIONS """

try:
    print (0 / 0)
except ZeroDivisionError:
    print ("cannot divide by zero")


""" LISTS : simply an ordered collection"""

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

list_length = len(integer_list)
list_sum = sum(integer_list)

x = range(10) # [0, 1, ..., 9]
zero = x[0]
nine = x[-1]
eight = x[-2]
x[0] = -1

first_three = x[:3]     #[-1, 1, 2]
three_to_end = x[3:]    #[3, 4, ..., 9]
one_to_four = x[1:5]    #[1, 2, 3, 4]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

# IN operator to check for list membership:
1 in [1, 2, 3]      #True
0 in [1, 2, 3]      #False 

# This check involves examining the elements of the list ONE AT A TIME.
# You shouldn't use it unless you know your list is pretty small

x = [1, 2, 3]

# Concat
x.extend([4, 5, 6])     # x is now [1, ..., 6]

# If you don't want to modify x you can use list addition:
y = x + [4, 5, 6]
# Or append:
x.append(1)

x, y = [1, 2]

""" TUPLES : lists' immutable cousins! Anything you can do to a list that
doesn't involve modifying it, you can do to a tuple. You can specify a tuple
by using () instead []"""

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")
    
# Tuples are a convenient way to return multiple values from functions
def sum_and_product(x, y):
    return (x+y), (x * y)

sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

# Tuples (and lists) can also be used for multiple assignment:
x, y = 1, 2
x, y = y, x     # Pythonic way to swap variables


""" DICTIONARIES : associates values with keys and allows you to quickly
retrieve the value corresponding to a given key"""

empty_dict = {}     # Pythonic
grades = { "Joel" : 80, "Tim" : 95 }

joels_grade = grades["Joel"]

# KeyError if you ask for a key that's not in the dictionary:
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# Checking for the existence of a key using IN:
joel_has_grade = "Joel" in grades   # True
kate_has_grade = "Kate" in grades   # False

# Get method that returns a default value (instead of raising an exception)
# when you look up a key that's not in the dictionary:

joels_grade = grades.get("Joel", 0)     # equals 80
kates_grade = grades.get("Kate", 0)     # equals 0
no_ones_grade = grades.get("No One")    # default default is None

# Assigning key-value pairs 
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

# Example
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"  ]
}
    
tweet_keys = tweet.keys()       # list of keys
tweet_values = tweet.values()   # list of values
tweet_items = tweet.items()     # list of (key, value) tuples
        
"user" in tweet_keys        # True, but uses a slow list in
"user" in tweet             # more Pythonic, uses faster dict in
"joelgrus" in tweet_values  # True 

""" DEFAULTDICT """
# Counting words in a document
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Using get
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
    
""" DEFAULTDICT is like a regular dictionary, except that when you try to look
up a key it doesn't contain, it first adds a value for it using a zero-argument
function you provided when you created it.

In order to use it, you have to import them from collections: """

from collections import defaultdict

word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # { "Joel" : { "City" : "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0, 1]}


""" COUNTER : turns a sequence of values into a defaultdict(int)-like object
mapping keys to counts. Useful to create histograms: """

from collections import Counter
c = Counter([0, 1, 2, 0])           # c is (basically) { 0 : 2, 1 : 1, 2: 1 }

# This gives us a very simple way to the word_counts problem:
word_counts = Counter(document)

# A Counter instance has a most_common method that is frequently useful:

# print the 10 most common words and their counts

from collections import Counter
    
document = "o rato comeu a roupa do rei de roma. rato safado!"

word_counts = Counter(document)
for word, count in word_counts.most_common(10):
    print (word, count)

"""SETS : represents a collection of DISTINCT elements: """
s = set()
s.add(1)
s.add(2)    # s is now { 1, 2 }
s.add(2)    # s is still { 1, 2 }
x = len(s)  # equals 2
y = 2 in s  # True
z = 3 in s  # False

""" 2 Reasons to use: Very fast operation on sets AND to Find disting items"""
# 1
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list     # False, but have to check every element

stopwords_set = set(stopwrods_list)
"zip" in stopwords_set      # very fast to check

# 2
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)          # 6
item_set = set(item_list)           # {1, 2, 3}
num_distinct_items = len(item_set)  # 3
distinct_item_list = list(item_set) # [1, 2, 3]


""" CONTROL FLOW (if, else, while, for...)"""
# if/else
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
    
# while    
x = 0
while x < 10:
    print (x, "is less than 10")
    x += 1

# More often we'll use for and in:
for x in range(10):
    print(x, "is less than 10")

# Continue/break:
for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)


""" TRUTHINESS (Veracidade) : Booleans """
one_is_less_than_two = 1 < 2        # equals True
true_equals_false = True == False   # equals False

# Python uses the value None to indicate a nonexistent value (similar to null)
x = None
print (x == None)     # prints True, but is not Pythonic
print (x is None)     # True, and its Pythonic

# Python has an all function, which takes a list and returns True precisely
# when every element is truthy

# any function: returns True when at least one element is truthy
all([True, 1, { 3 }])   # True
all([True, 1, {}])      # False, {} is falsy
any([True, 1, {}])      # True
all([])                 # True, no falsy elements in the list
any([])                 # False, no truthy elements in the list


""" SORTING """
# Sorted
x = [4, 1, 2, 3]
y = sorted(x)
x.sort()

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key = abs, reverse = True)   # is [-4, 3, -2, 1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda (word, count): count,
            reverse=True)

""" LIST COMPREHENSIONS : transformation a list into another list, by choosing
only certain elements, or by transforming elements, or both."""

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4 , 16]

# You can similarly turn lists into dictionaries or sets:
square_dict = { x : x * x for x in range(5) }   # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set = { x * x for x in [1, -1] }         # { 1 }

# if you don't need the value from the list, it's conventional to use an 
# underscore as the variable:
zeroes = [0 for _ in even_numbers]      # has the same length as even_numbers

# Multiple fors:
pairs = [(x, y)
        for x in range(10)
        for y in range(10)]     # 100 pairs (0, 0) (0, 1), ..., (9, 9)

increasing_pairs = [(x, y)      # only pairs with x < y
                    for x in range(10)
                    for y in range(x + 1, 10)]

""" GENERATORS and ITERATORS A Gen is something that you can iterate over
but whose values are produced only as NEEDED - lazily - (useful in cases 
where we only need the first values of thousands) """

""" Generators are iterators, but you can ONLY ITERATE OVER THEM ONCE!
It’s because they do not store all the values in memory, they generate
the values on the fly: """
                                    
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

# Yield is a keyword that is used like return, except the function will return 
# a generator.
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
mygenerator = createGenerator()
print(mygenerator)  # mygenerator is an object
for i in mygenerator:
    print(i)

""" To master yield, you must understand that when you call the function,
the code you have written in the function body does not run. 
The function only returns the generator object!

Then, your code will be run each time the for uses the generator.

The first time the for calls the generator object created from your function,
it will run the code in your function from the beginning until it hits yield, 
then it’ll return the first value of the loop. Then, each other call will run
the loop you have written in the function one more time, and return the next
value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield
anymore. It can be because the loop had come to an end, or because you do not 
satisfy a “if/else” anymore.
                     
"""
                                                         
# Yield operator
def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1
        
# The following loop will consume the yielded values one at a time until none 
# are left:

for i in lazy_range(10):
    print(i)
                        
# Using comprehensions:
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

for i in lazy_evens_below_20:            
    print(i)            
            

"""RANDOMNESS"""
import random
# random.random() produces numbers uniformly between 0 and 1
four_uniform_randoms = [random.random() for _ in range(4)]           

random.seed(10)
print (random.random())
            
# random.randrange(x, y): takes either 1 or 2 arguments
# and returns an element chosen randomly from the corresponding range
random.randrange(10)
random.randrange(1, 100)

# random.shuffle randomly reorders the elements of a list:
up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)
            
# random.choice(): randomly picks one element from a list
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     

# random.sample: randomly choose a sample of elements with no duplicates
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)    

# with replacement (allowing duplicates):
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]

"""REGULAR EXPRESSIONS"""
import re

print (all([
    not re.match("a", "cat"),               # * 'cat' doesnt' start with 'a'
    re.search("a", "cat"),                 # * 'cat' has an 'a' in it
    not re.search("c", "dog"),              # * 'dog' doesn't have a 'c' in it
    3 == len(re.split("[ab]", "carbs" )),   # * split on a or b to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2")  # * replace digits with dashes
    ]))

""" OOP """
class Set:
    # every member takes a first parameter "self"
    # that refers to the particular Set object being used
    
    def __init__(self, values = None):
        """ This is the constructor. It gets called when you create
        a new Set.
        s1 = Set()              # empty set
        s2 = Set([1, 2, 2, 3])  # initialize with values"""
        
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)
    
    def __repr__(self):
        """this is the string representation of a Set object
        if you type it at the Python prompt or pass it to str()"""
        return "Set: " + str(self.dict.keys())
    
    # we'll represent membership by being a key in self.dict with value True
    def add(self, value):
        self.dict[value] = True
        
    # value is in the Set if it's a key in the dictionary
    def contains(self, value):
        return value in self.dict
    
    def remove(self, value):
        del self.dict[value]

# Using:
s = Set([1, 2, 3])
s.add(4)
print(s.contains(4))
s.remove(3)
print(s.contains(3))


"""FUNCTIONAL TOOLS"""
# Bad way:
def exp(base, power):
    return base ** power

def two_to_the(power):
    return exp(2, power)

# Good way (functools.partial):
# By using partial functions, we can replace the existing function with already
# passed arguments. Moreover, we can also create a new function version by 
# adding documentation in well-mannered. 
        
# Example:
from functools import partial
 
def multiply(x, y):
       return x * y
 
doubleNum = partial(multiply, 2)
tripleNum = partial(multiply, 3)
 
print(doubleNum(10))

# map, reduce and filter: provide functional alternatives to list comprehensions

def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]      # [2, 4, 6, 8]
twice_xs = map(double, xs)              # same as above
list_doubler = partial(map, double)     # *function* that doubles a list
twice_xs = list_doubler(xs)             # again [2, 4, 6, 8]

thrice_xs = [3 * x for x in xs]

# Map with multiple-argument functions

def multiply(x, y): return x * y

products = map(multiply, [1, 2], [4, 5])    # [1 * 4, 2 * 5] = [4, 10]

# Filter: return an iterator yielding those items of iterable for which
# function(item) is true. If function is None, return the items that are true

# Similarly, filter does the work of a list-comprehension if:
def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]     # [2, 4]
x_evens = filter(is_even, xs)               # same as above
list_evener = partial(filter, is_even)      # *function* that filters a list
x_evens = list_evener(xs)

# reduce() combines the first two elements of a list, then that result with
# the third... and so on, producing a single result:
x_product = reduce(multiply, xs)            # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply)    # *function* that reduces a list
x_product = list_product(xs)                # again = 24
 

"""ENUMERATE: to iterate over a list and use both its elements and their 
indexes:"""

# not Pythonic
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)

# also not Pythonic
    i = 0
    for document in documents:
        do_something(i, document)
        i += 1

# The Pythonic solution is enumerate, which produces tuples (index, element):
for i, document in enumerate(documents):
    do_something(i, document)
    
# Similarly, if we just want the indexes:
for i in range(len(documents)): do_something(i)     # not Pythonic
for i, _ in enumerate(documents): do_something(i)   # Pythonic

"""ZIP AND ARGUMENT UNPACKING"""
# Zip transforms multiple lists into a single list of tuples of corresponding
# elements:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)           # is [('a', 1), ('b', 2), ('c', 3)]

# if the lists are differente lengths, zip stops as soon as the first list ends

# "unzip":
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

"""ARGS AND KWARGS"""
# we want to create a higher-order function that takes as input some function
# f and returns a new function that for any input returns twice the value of f

# We need a way to specify a function that takes arbitrary arguments.
# We can do this with argument unpacking:
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)
    
    magic(1, 2, key = "word", key2 = "word2")
    
    # prints
    # unnamed args: (1, 2)
    # keyword args: {'key2': 'word2', 'key': 'word}
    
# args is a tuple of function's unnamed arguments
# kwargs is a dict of its named arguments

# Ex:
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = { "z" : 3 }
print(other_way_magic(*x_y_list, **z_dict))     # 6

# Producing higher-order functions whose inputs can accept arbitrary arguments:
def f2(x, y):
    return x + y

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print (g(1,2))      # 6
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
            
            
            






