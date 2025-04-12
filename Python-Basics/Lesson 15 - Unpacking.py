l = [1, 2, 3]
a, b, c = l #each variable will get the elem matching their position
print(f'a = {a}, b = {b}, c = {c}') #a = 1, b = 2, c = 3

#a, b = l
#print(f'a = {a}, b = {b}') #ValueError: too many values to unpack (expected 2)
#with unpacking you have to know exactly how many elements iterable has
#but ofc there is a fix


#if you need just first 2 elems you could write this:
arr = [1, 2, 3, 4, 5]
a, *c, b = arr #*c gets all the elems after a, b are evaluated
print(a, b, c) #* expression ALWAYS stores values as a list

#but if you won't use those elems and you just need first, and last
#Python convention is to use _ for that
a, *_, b = arr #this code does the same thing as one above, it's just cleaner
print(a, b, _) #1 5 [2, 3, 4]

#all the rules that i mention with list apply to tuples, sets and dicts, but they have twist

t = (1, 2, 3, 4, 5)
a, *c, b = t
print(a, b) #1 5
print(type(c)) #still a list even though t is a tuple

s = {1, 2, 3, 4, 5}
a, *c, b = s
print(a, b, c) #1 5 [2, 3, 4]

d = {'one' : 1, 'two' : 2, 'three' : 3}
a, b, c = d #by default unpacking gets you the keys
print(a, b, c) #one two three
a, b, c = d.values() #this unpacks the values
print(a, b, c) #1 2 3

a, b, c = d.items() #this unpacks keys and values as tuple pairs
print(a, b, c)
#but if you want to get them as variables not as tuple pairs write this:
(key_a,value_a), (key_b,value_b), (key_c,value_c) = d.items()
print(f'keys = {key_a} {key_b} {key_c}')         #keys = one two three
print(f'values = {value_a} {value_b} {value_c}') #values = 1 2 3