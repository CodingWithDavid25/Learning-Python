a = {"one" : 1, "two" : 2} #"one" is the key, 1 is the value
print(a) #{'one' : 1, 'two' : 2}
print(*a) #one two
#* expression with dicts gets you the keys
#key doesn't have to be str and value doesn't have to be numeric
#key can be any immutable type, and value can be literally any type

b = {(1, 2) : [2, 5, 1]} #key is tuple, immutable type, value is a list

print(b) #{(1, 2) : [2, 5, 1]}
print(a["two"]) #2
print(b[(1, 2)]) #[2, 5, 1]

for key, value in a.items(): #.items() return (key, value) and key = key, value = value
   print(f"key = {key}   value = {value}")


for key in a.keys(): #.keys() returns just the keys
    print(key)

for value in a.values(): #.values() returns just the values
    print(value)


print(a.get("one", "Value not found")) #get gets you the value if the key exists,
# if not it prints the message that you want
print(a.pop("three", "Value dosn't exist")) #removes the element if the key exists,
#if not it prints the message
a.update(b) #appends b at the end of the a
print(a) #{'one': 1, 'two': 2, (1, 2): [2, 5, 1]}

b.clear() #clears the whole dict
print(b) #{}

l = [2, 3, 4] #list
new = dict.fromkeys(l, 0) #creates a dict from a list,
# where elems of list are keys with the given value
print(new) #{2: 0, 3: 0, 4: 0}