# list
myLists = ['a', 'a', 'b', 'c', 'b', 'c', 'd']

# tuple (read-only)
myTuple = ('a', 'a', 'b', 'c', 'b', 'c', 'd')

# dictionary
myDictionary = {'lists': myLists}

# print(myDictionary['lists'][0])

# Count duplicate element in lists
print("Length of myList %d" % len(myLists))
print(myLists.count('a'))   # count object a

# ==========
# Solution A
# ==========
countSolA = {
    x: myLists.count(x) for x in myLists
}

print(countSolA)    # {'a': 2, 'b': 2, 'c': 2, 'd': 1}

# ==========
# Solution B
# ==========
countSolB = {
    x: myLists.count(x) for x in set(myLists)
}
print(set(myLists)) # build unordered unique element
print(countSolB)    # {'a': 2, 'b': 2, 'c': 2, 'd': 1}
