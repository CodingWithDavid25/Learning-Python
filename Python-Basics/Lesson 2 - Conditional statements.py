a = 4
b = 3

if a > b: #if (conditional statement): = used to check something
    print("A is greater than b!")
else: #if previous if statement is not true enter this scope
    print("A is smaller than b!")

#if a > 1:
#    if a < 3:
#        print("A is between 1 and 3")

if a > 1 and a < 3: #same as the code above but with merged ifs = easier to read
    #and = both have to be true in oreder for the whole if to be true
    #you can stack as many ands as you want
    print("A is between 1 and 3")

if a > 0 or a > 5: #or = one or the other statement has to be true for the whole if to be true
    print("OR")

x = 4

if x > 100:
    print("x is greater than 100")

elif x > 10:#else + if = elif, if this statement is true all others below are skipped
    print("x is greater than 10")

elif x > 1:
    print("x is greater than 1")

else:#if none of the elifs are entered, enter this else scope
    print("else")


#if x == 1:         #for comparing if two things are the same we use == instead of =
#    print("one")   #thats how we differentiate checking (==) for assigning (=)
#if x == 2:
#    print("two")
#if x == 3:
#    print("three")

match x:   #checks value of x - doesn't have to be numeric!
    case 1: #case 1 means if x == 1:
        print("one")
    case 2: #same
        print("two")
    case 3: #same
        print("three")
    case _: #case _: is basically the same as else
        print("i am not interested in this number")

#a = 4
#b = 3

#y = 1
#if a > b:
#    y = a
#else:
#    y = b

y = a if a > b else b #same as the code above but more efficient

#decompoze and read character by character to see what this line does
#that's pro tip for remembering and understanding because this way you will hear
# it sound like you are talking english language not python
print(y)