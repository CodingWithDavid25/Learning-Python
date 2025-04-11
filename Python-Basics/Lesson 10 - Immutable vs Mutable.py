x = 3   #x is bound to the location of 3 in memory
y = x   #y is bound to the location of x in memory
x+=1    #4 is created and put in memory and x is bound to it

#so now mem(x) != mem(y)
#is = used to check if 2 memory locations are the same

print(x is y) #False, they are NOT bound to the same location
#the behavior above is for the immutable types

a = [1, 2, 3] #a is bound to the first location of this list,
              # or in other words to the location of 1
b = a
a += [1]  #new element is added and the locations are not changed
print(a is b) #True, they are bound to the same location
print(f'a = {a}   b = {b}') # a = [1, 2, 3, 1] b = [1, 2, 3, 1]
a[3] = 4 #just the element on position 3 is changed from 1 to 3, no new location is allocated
print(a is b) #True, they are bound to the same location
print(f'a = {a}   b = {b}') # a = [1, 2, 3, 4] b = [1, 2, 3, 4]

#the behavior above is how mutable types work

#examples below show why it's important to know if type is mutable or not
#check your understing of this topic with these 2 examples :)
#if you don't know the answer and why feel free to ask in comment
# or in gmail: coding.with.david25@gmail.com
def change_var(a):
    a += 1

x = 2
change_var(a = x)
print(x)

def change_list(l):
    l += [1]

r = [1, 2, 3]
change_list(l = r)
print(r)

#mutable   types: list, dict, set
#immutable types: int, float, complex, bool, str, tuple, frozenset,