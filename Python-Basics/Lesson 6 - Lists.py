first = [2, 5.5, "cat"] #python list
print(first) #prints [2, 5.5, "cat"
print(*first) # *[lists_name] prints 2 5.5 'cat'

print(first[2]) #gets the 3rd item in a list since counting starts form 0

for i in range(3): #traversing a whole list using range()
    print(first[i])

#better way and most commonly used
for i in first: #traversing a whole list where i becomes each elem
    print(i)

x = first[0:2] #list slicing - name = [start:end:step]
y = first[:]  #start has default start 0,
              #end has a default value of the length of the list
              #defualt step is 1
#print(x, y)

longer = [1, 2, 3, 4, 5]
a = longer[2:] #gets elems from the 2nd until the end
b = longer[:3] #gets elems from the start until the 3rd
c = longer[1::2] #gets elems from the 1st position until the end with step 2
print(a)
print(b)
print(c)
print(longer[-1]) #prints the last elem of the list
d = longer[3:0:-1] #start doesn't have to be smaller than end
# but then step has to be negative
print(d)

print(len(longer))
longer.append(2) #puts 2 at the end of the list
print(longer)
longer.insert(2, 1) #inserts 1 at the position 2
print(longer)
longer.remove(1) #removes FIRST occurrence of 1 in a list
print(longer)
longer.pop() #removes last elem
print(longer)
longer.reverse() #reverses the list
print(longer)
longer.sort() #sorts a list
print(longer)
print(sorted(longer)) #solves a list with the given elems and returns it
                      #this is one-time sort
print(longer)