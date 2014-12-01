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
