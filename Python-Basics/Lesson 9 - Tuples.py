tup = (1, 2, 3) #to create tuple you need write () and values separated with ,
print(tup)  #(1, 2, 3)
print(*tup) #unpacks tuple int elements and prints them with space separation
single = (1,)   #to create single elem tuple you need to write , after the value if not you'll get int or float
single2 = (1)
print(type(single))  #tuple
print(type(single2)) #int
print(tup[1]) #indexing starts from 0, gets the 2nd elem

for i in range(len(tup)): #traversing tuples utilizing indexing, len gets the length of a tuple
    print(tup[i])

for i in tup: #i becomes each element of a tuple
    print(i)


tup2 = tup + single #+ is merging 2 or more tuples
tup3 = 3*tup #* is merging one tuple multiple times
print(tup2) #(1, 2, 3, 1)
print(tup3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

print(tup3.count(2)) #.count([value]) counts how many [value] appears in a tuple
print(tup3.index(2)) #.index([value]) returns first index of [value] in a tuple


#tuple is immutable type, for more info on that check Lesson 10
#but bcs tuple is immutable it doesn't have append, insert and remove functions
#here are alternative ways how to create them using operations and slicing
#if you don't know how slicing works check Lesson 6 - Lists

x = (2, 5, 3)
x += (1,) #+ is used to append at the end of a tuple
print(x) #(2, 5, 3, 1)
x = x[:2] + (4,) + x[2:] #inserting at position 2, positions start from 0

#formula: x = x[:pos] + (elem,) + x[pos:]
#explantion of the formula ->
#pos = index where you want to insert your new elem, starts from 0
#x[:pos] used to get the elements until the index pos, excluding the index pos
#x[pos:] used to get the elements after the index pos, including the index pos
#(elem,) adding the element at the wanted position

print(x) #(2, 5, 4, 3, 1)

x = x[:1] + x[2:] #removing elem at position 1, positions start from 0

#formula: x = x[:pos] + x[pos+1:]
#explantion of the formula ->
#pos = index of elem you want to return
#x[:pos] = used to get the elements until the index pos, excluding the index pos
#x[pos+1:] = used to get the elements after the index pos+1, including the index pos+1
#combining those 2 we get all the elements except the one at the index pos

print(x) #(2, 4, 3, 1)

#another alternative is to use typecasting, to convert tuple to list and then back to tuple

y = list(x) #convert to list
y.remove(2) #use function remove([value]) to remove [value] from y list
x = tuple(y) #converting y to tuple and bounding x to that tuple
print(x) #(4, 3, 1)

from collections import namedtuple #just write this so you can use named tuples
#line above is a topic for another video

animal = namedtuple("Animal", ["name", "age", "owner"]) #Define a namedtuple type called 'Animal' with three fields: 'name', 'age', and 'owner'.
#fields are values that my tuple will store and every field has a name, usually that describes what value will be stored
#with namedtuple you can access that elem by simple writing [tuple_name].[field_name]
#namedtuple is a function that creates namedtuple class - I'll create a series on classes then you will understand better what they are and how to use them

dog = animal("rex", 12, "David") #dog is instance(object) of class namedtuple, named Animal
print(dog.age) #access age via field name, 12
print(dog[1]) #access age via indexing,    12
