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
