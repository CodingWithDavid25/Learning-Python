s = {2, 4, 3, 2} #even though i put duplicates they will be removed
#set is unordered, which means python doesn't guarantee you that
#the set will be sorted or stored they way you placed your elems
print(s) #{2, 3, 4} - here it's sorted

empty = set() #you need to create empty set this way bcs if you write {} that will then be empty dict
print(type(empty))

n = {20, 40, 30}
print(n) #{40, 20, 30} - here it's not sorted

print(3 in s) #True, checks if 3 is in s
print(1 in s) #False

for i in s: #same as with others, i becomes one of the elems until the end
    print(s)

s.add(1) #adds 1 to s
print(s)
s.pop() #removes the first element,
print(s)
# but since we don't know the order we don't know what elem will be removed
s.remove(3) #removes 3, returns error if not found
print(s)
s.discard(2) #removes 2, does nothing if not found
print(s)

x = {1, 2, 3}
y = {3, 4, 5}

#most of the operations have their symbol + function, so I won't explain the operations
#function names should be enough for you to understand

print(x | y) #{1, 2, 3, 4, 5}
print(x.union(y)) #{1, 2, 3, 4, 5}

print(x & y) #{3}
print(x.intersection(y)) #{3}

print(x.difference(y))  #{1, 2}
print(y.difference(x))  #{4, 5}

print(x ^ y) #{1, 2, 4, 5}
print(x.symmetric_difference(y))  #{1, 2, 4, 5}

print(x <= y) #False, checks if all the elements that x has, y has as well
print(x.issubset(y)) #False

print(x >= y) #False, checks if all the elements that y has, x has as well
print(x.issuperset(y)) #False

print(x.isdisjoint(y)) #False, checks if x intersection y is empty set

fs1 = frozenset([2, 3, 4]) #frozenset is immutable set, sets are mutable
fs2 = frozenset([3, 4, 5])
s1 = {1, 2, 3}
#the type of the set when you combine frozenset and set depends on which is first
print(fs1 & s1) #here, first is frozenset so ending set will be frozenset as well
print(s1 & fs1) #here, first is set so ending set will be regular set as well