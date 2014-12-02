"""
Data Structures and Algorithms
==============================

1. Unpacking a Sequence into Separate Variables
-----------------------------------------------
"""

# We can unpack tuples into sequence by separating variables with a comma
tup = ("lol", 42)
lol, forty_two = tup

assert lol       == "lol"
assert forty_two == 42

# We can do the same for a list
data = ["salut", 69, True, ("je","suis","un","tuple")]
salut, sixty_nine, true, tup = data

assert salut      == "salut"
assert sixty_nine == 69
assert true       == True
assert tup        == ("je","suis","un","tuple")

# We can also directly extract the tuple
salut, sixty_nine, true, (je,suis,un,tupl) = data

assert salut      == "salut"
assert sixty_nine == 69
assert true       == True
assert je         == "je"
assert suis       == "suis"
assert un         == "un"
assert tupl       == "tuple"

"""
Unpacking work every objects that are iterables: string, files, etc...
You can also skip some value with "_"
"""
string = "string"
s,_,r,_,n,_ = string
assert s == "s"
assert r == "r"
assert n == "n"

"""
2. Unpacking Elements from Iterables of Arbitrary Length
--------------------------------------------------------

We can use "*" to unpack more than one value
"""
record = ("Jean-Mi","jean.mi@wanadoo.fr", "0132101010", "+42777890910")
name, mail, *phones = record
assert name   == "Jean-Mi"
assert mail   == "jean.mi@wanadoo.fr"
assert phones == ["0132101010", "+42777890910"]

# Get the head
head, *tail = ["head", "t", "a", "i", "l"]
assert head == "head"
assert tail == ["t","a","i","l"]

# Get the tail
*head, tail = ["h","e","a","d","tail"]
assert head == ["h","e","a","d"]
assert tail == "tail"

# Get the middle
head, *mid, tail = ["head","m","i","d","tail"]
assert head == "head"
assert mid  == ["m","i","d"]
assert tail == "tail"

"""
**We can't assign assign two starred expressions:**  
`head, *queue = [0,1,2,2,1,0]` is not possible
"""

"""
3. Keeping Last N-items
-----------------------

### Yield and generators
"""

# #### A simple list
lst = [0,1,4]
assert lst[0] == 0
assert lst[1] == 1
assert lst[2] == 4

"""
#### List in intension

Basic way:
"""
nums = [0,1,2]
lst  = []
for n in nums:
    lst.append(n*n)
assert lst[0] == 0
assert lst[1] == 1
assert lst[2] == 4

# With intention
lst = [n*n for n in nums]
assert lst[0] == 0
assert lst[1] == 1
assert lst[2] == 4

# We can filter w/ intention
nums = [0,1,2,3,4,5,6]
even = [n for n in nums if n%2 == 0]
assert even == [0,2,4,6]


# #### Generators
gen = (n*n for n in range(3))
assert str(type(gen)) == "<class 'generator'>"
i = 0
for n in gen:
    assert n == i*i
    i+=1
# We can't use a generator a second time

"""
#### Yield keyword
"""

# We can also create a generator with the yield keyword
def makeGen():
    nums = range(3)
    for n in nums:
        yield i*i

gen = makeGen()

assert str(type(gen)) == "<class 'generator'>"
i = 0
for n in gen:
    assert n == i*i
    i+=1

"""
### Deque

*A double ended queu (or deque) supports adding and removing elements from either end.*
"""

# A deque work like a list
from collections import deque
d = deque("lolibar")
assert d[0]   == 'l'
assert d[-1]  == 'r'
assert len(d) == 7
d.remove('i')
assert d == deque("lolbar")

# It can be populated from left or right
d = deque()
d.append('r')
d.extend('ight')
d.appendleft('t')
d.extendleft('fel')
assert d == deque("leftright")

# We can also pop on deque
t = d.pop()
l = d.popleft()
assert t == "t"
assert l == "l"
assert d == deque("eftrigh")

# We can do right rotation...
d.rotate(2)
assert d == deque("gheftri")

#... and left rotation
d.rotate(-4)
assert d == deque("trighef")

# We can also fix a limit of size, with maxlen
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
assert d == deque([1,2,3])
d.append(4)
d.append(5)
assert d == deque([3,4,5])

"""
### Keep the last N-Items

We are searching the pattern "ZLURP" in the lines and we want to keep an history for the N last result
"""

lines = [
    "blablablablabla",
    "blablabZLURPlablabla",
    "blablablablabla",
    "blZLURPablablablabla",
    "blablablZLURPablabla",
    "blablablablabla",
    "blablablablabZLURPla",
    "ZLURPblablablablabla",
]

# This function do the search
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # If the pattern is in the line, it yield the line and the last previous line that were searched
            yield line, previous_lines
        previous_lines.append(line)

result = [(l,list(plines)) for l,plines in search(lines,"ZLURP")]
wanted = [
    ("blablabZLURPlablabla", ["blablablablabla"]),
    ("blZLURPablablablabla", ["blablablablabla","blablabZLURPlablabla","blablablablabla"]),
    ("blablablZLURPablabla", ["blablablablabla","blablabZLURPlablabla","blablablablabla","blZLURPablablablabla"]),
    ("blablablablabZLURPla", ["blablabZLURPlablabla","blablablablabla","blZLURPablablablabla","blablablZLURPablabla","blablablablabla"]),
    ("ZLURPblablablablabla", ["blablablablabla","blZLURPablablablabla","blablablZLURPablabla","blablablablabla","blablablablabZLURPla"])
]
assert result == wanted

"""
4. Finding the Largest or Smallest N Items
------------------------------------------

### heapq

The heapq module use the "list" type for adding, deleting elements and keeping the order by
using binary tree.
"""
import heapq
l = []
heapq.heappush(l, 69)
heapq.heappush(l, 42)
heapq.heappush(l, 99)
assert l == [42,69,99]

# The heapq module is perfect for this problem

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# Find the 3 largest elements of the list
largest = heapq.nlargest(3,nums)
assert largest == [42,37,23]

# Find the 3 smallest elements of the list
smallest = heapq.nsmallest(3,nums)
assert smallest == [-4,1,2]

# It can be also used with complicated data structures
beers = [
        {"brand":"Amstel Light", "alcohol":3.5},
        {"brand":"Heineken", "alcohol":5.4},
        {"brand":"Heineken Light", "alcohol":3.5},
        {"brand":"Guinness", "alcohol":7.5},
        {"brand":"1664", "alcohol":6.1},
        {"brand":"Kozel Světlý", "alcohol":4},
        {"brand":"Kronenbourg ", "alcohol":4.2}
]

drunk = heapq.nlargest(3, beers, key=lambda s: s["alcohol"])
sober = heapq.nsmallest(3, beers, key=lambda s: s["alcohol"])
assert drunk == [{'brand': 'Guinness', 'alcohol': 7.5}, {'brand': '1664', 'alcohol': 6.1}, {'brand': 'Heineken', 'alcohol': 5.4}]
assert sober == [{'brand': 'Amstel Light', 'alcohol': 3.5}, {'brand': 'Heineken Light', 'alcohol': 3.5}, {'brand': 'Kozel Světlý', 'alcohol': 4}]

"""
5. Implementing a Priority Queue
--------------------------------
"""

class PriorityQueue:
    def __init__(self):
        self._queue = []
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority,item))
    def pop(self):
        return heapq.heappop(self._queue)[1]

queue = PriorityQueue()
queue.push("lol", 78)
queue.push("foo", 34)
queue.push("baz", 42)
queue.push("lolibar", 34)

assert queue.pop() == "lol"
assert queue.pop() == "baz"
assert queue.pop() == "foo"
assert queue.pop() == "lolibar"
#

"""
6. Mapping Keys to Multiple Values in a Dictionary
--------------------------------------------------
"""

# We can use `list` if we want to keep the insertion order
d = {
    "foo": [2,3],
    "bar": [42]
}
d['foo'].append(1)
d['bar'].append(42)
assert d == {
    "foo": [2,3,1],
    "bar": [42,42]
}

# Or use `set` if we want eliminate duplicate
d = {
    "foo": {2,3},
    "bar": {42}
}
d["foo"].add(1)
d["bar"].add(42)
assert d == {
    "foo": {1,2,3},
    "bar": {42}
}

# We can also use defaultdict for make dict of string
from collections import defaultdict
d = defaultdict(list)
d["foo"].append(2)
d["foo"].append(3)
d["bar"].append(42)
assert d == {
    "foo": [2,3],
    "bar": [42]
}

"""
7. Keeping Dictionaries in Order
--------------------------------
"""

# Use OrderedDict
from collections import OrderedDict
d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["baz"] = 3
d["lol"] = 4

l = [("foo",1),("bar",2),("baz",3),("lol",4)]
i = 0
for key in d:
    assert key == l[i][0]
    assert d[key] == l[i][1]
    i+=1

"""
8. Calculating with Dictionaries
--------------------------------
"""

#### Zip

l1 = ["foo","bar","lol"]
l2 = [1,2,3]
l  = list(zip(l1,l2))
assert l == [("foo",1),("bar",2),("lol",3)]


# Use zip to invert key and value
beers_alcohol = {
    "Amstel Light":3.5,
    "Heineken":5.4,
    "Heineken Light":3.5,
    "Guinness":7.5,
    "1664":6.1,
    "Kozel Světlý":4,
    "Kronenbourg ":4.2
}
min_alcohol = min(zip(beers_alcohol.values(), beers_alcohol.keys()))[1]
max_alcohol = max(zip(beers_alcohol.values(), beers_alcohol.keys()))[1]
assert min_alcohol == "Amstel Light"
assert max_alcohol == "Guinness"

"""
9. Finding Commonalities in Two Dictionaries
--------------------------------------------
"""

a = { 'x':1, 'y':2, 'z':3 }
b = { 'w':2, 'x':1, 'y':3 }

# Find keys in common
res = a.keys() & b.keys()
assert res == {'x','y'}

# Find keys not in common
res = a.keys() - b.keys()
assert res == {'z'}

# Find key/value pairs in common
res = a.items() & b.items()
assert res == { ('x',1) }

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
assert c == {'x':1, 'y':2}

"""
10. Removing Duplicates from a Sequence while Maintaining Order
---------------------------------------------------------------
"""

# We can use a set
def dedupe(items):
    viewed = set()
    for item in items:
        if item not in viewed:
            yield item
            viewed.add(item)

l = [4,2,6,2,4,9]
res = list(dedupe(l))
assert res == [4,2,6,9]

"""
11. Naming a Slice
------------------
"""

# We can name slice
l = ["2","3","I","want","that","9","42"]
I_want_that = slice(2,5)
assert l[I_want_that] == ["I","want","that"]

# We can assign a slice
l[2:5] = ["I","disapear"]
assert l == ["2","3","I","disapear","9","42"]
l[I_want_that] = ["I want that"]
assert l == ["2","3","I want that","42"] # the 9 disapear

"""
12. Determining the Most Frequently Occurring Items in a Sequence
-----------------------------------------------------------------
"""

# By using counter
from collections import Counter
words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
assert top_three == [('eyes', 8), ('the', 5), ('look', 4)]

"""
13. Sorting a list of dictionary by a common key
------------------------------------------------
"""

# ### itemgetter
from operator import itemgetter

assert itemgetter(1)('ABCDEFG') == 'B'
assert itemgetter(1,3,5)('ABCDEFG') == ('B', 'D', 'F')
assert itemgetter(slice(2,None))('ABCDEFG') == 'CDEFG'

# Sort these beers
beers = [
    {"brand":"Amstel Light", "alcohol":3.5},
    {"brand":"Heineken", "alcohol":5.4},
    {"brand":"Heineken Light", "alcohol":3.5},
    {"brand":"Guinness", "alcohol":7.5},
    {"brand":"1664", "alcohol":6.1},
    {"brand":"Kozel Světlý", "alcohol":4},
    {"brand":"Kronenbourg ", "alcohol":4.2}
]
beers_by_name    = sorted(beers,key=itemgetter('brand'))
beers_by_alcohol = sorted(beers,key=itemgetter('alcohol'))
# By Name
wanted_by_name = [
    {"brand":"1664", "alcohol":6.1},
    {"brand":"Amstel Light", "alcohol":3.5},
    {"brand":"Guinness", "alcohol":7.5},
    {"brand":"Heineken", "alcohol":5.4},
    {"brand":"Heineken Light", "alcohol":3.5},
    {"brand":"Kozel Světlý", "alcohol":4},
    {"brand":"Kronenbourg ", "alcohol":4.2}
]
# By Alcohol
wanted_by_alcohol = [
    {"brand":"Amstel Light", "alcohol":3.5},
    {"brand":"Heineken Light", "alcohol":3.5},
    {"brand":"Kozel Světlý", "alcohol":4},
    {"brand":"Kronenbourg ", "alcohol":4.2},
    {"brand":"Heineken", "alcohol":5.4},
    {"brand":"1664", "alcohol":6.1},
    {"brand":"Guinness", "alcohol":7.5}
]

assert beers_by_name == wanted_by_name
assert beers_by_alcohol == wanted_by_alcohol

"""
14. Sorting Objects Without Native Comparison Support
-----------------------------------------------------
"""
class Beer:
    def __init__(self,name,alcohol):
        self.name = name
        self.alcohol = alcohol
    def __repr__(self):
        return "Beer({},{})".format(self.name,self.alcohol)

beers = [Beer("Guinness",7.5),Beer("Kronenbourg",4.2),Beer("1664",6.1)]

# Use operator attrgetter
from operator import attrgetter

# Sort beers by name
res    = sorted(beers, key=attrgetter('name'))
wanted = "[Beer(1664,6.1), Beer(Guinness,7.5), Beer(Kronenbourg,4.2)]"
assert str(res) == wanted

# Sort beers by alcohol
res    = sorted(beers, key=attrgetter('alcohol'))
wanted = "[Beer(Kronenbourg,4.2), Beer(1664,6.1), Beer(Guinness,7.5)]"
assert str(res) == wanted

"""
15. Grouping Records Together Based on a Field
----------------------------------------------
"""

# Group the address with the same date
rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
# By using groupby
from operator import itemgetter
from itertools import groupby

# First we need to sort
rows.sort(key=itemgetter('date'))

# Make group with groupby
by_date = defaultdict(list)
for date, items in groupby(rows, key=itemgetter('date')):
    by_date[date] = [item for item in items]

assert by_date == {
   '07/04/2012':[
      { 'address':'5148 N CLARK', 'date':'07/04/2012' },
      { 'address':'1039 W GRANVILLE', 'date':'07/04/2012' }
   ],
   '07/03/2012':[
      { 'address':'2122 N CLARK', 'date':'07/03/2012' }
   ],
   '07/02/2012':[
      { 'address':'5800 E 58TH', 'date':'07/02/2012' },
      { 'address':'5645 N RAVENSWOOD', 'date':'07/02/2012' },
      { 'address':'1060 W ADDISON', 'date':'07/02/2012' }
   ],
   '07/01/2012':[
      { 'address':'5412 N CLARK', 'date':'07/01/2012' },
      { 'address':'4801 N BROADWAY', 'date':'07/01/2012' }
   ]
}

"""
16. Filtering Sequence Elements
-------------------------------
"""

# Using a list comprehension
my_list = [3,6,7,9,2,4,69,42]
odd = [n for n in my_list if n % 2 == 1]
even = [n for n in my_list if n % 2 == 0]

assert odd == [3,7,9,69]
assert even == [6,2,4,42]

# If the result is huge, we can use generators
odd_gen = (n for n in my_list if n % 2 == 1)
i = 0
for n in odd_gen:
    assert odd[i] == n
    i+=1

# If the filtering criteria can't be easily expressed, we can use
# the built-in `filter()`
values = ['1','2','-3', '-', '4', 'N/A', '5']
# This function determine if the val is int or not
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ints_filtered = filter(is_int, values)
# `filter()` creates an iterator, so it's necessary to use `list()` if you want a
# list as result
ints_list = list(ints_filtered)
assert ints_list == ['1', '2', '-3', '4', '5']

# But a list comprehension work also for this example
ints_compr = [n for n in values if is_int(n)]
assert ints_compr == ints_list

"""
17. Extracting a Subset of a Dictionary
---------------------------------------
"""

# We want to make a subset for alcohol > 5°
beers = {
    "Amstel Light":3.5,
    "Heineken":5.4,
    "Heineken Light":3.5,
    "Guinness":7.5,
    "1664":6.1,
    "Kozel Světlý":4,
    "Kronenbourg ":4.2
}

# We can use dictionary comprehension
sup_5 = { key:value for key, value in beers.items() if value > 5 }
assert sup_5 == {
    "Heineken": 5.4,
    "Guinness": 7.5,
    "1664"    : 6.1,
}

"""
18. Mapping Names To Sequence Elements
--------------------------------------
"""

# We can use namedtuple
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr','joined'])
sub = Subscriber('xou@rinse.io','2014-09-19')
assert sub.addr   == 'xou@rinse.io'
assert sub.joined == '2014-09-19'

# We can't change the attribute, because `namedtuple` is immutable
try:
    sub.addr = 'xouabita@gmail.com'
except AttributeError:
    sub = sub._replace(addr='xouabita@gmail.com')
assert sub.addr == 'xouabita@gmail.com'
