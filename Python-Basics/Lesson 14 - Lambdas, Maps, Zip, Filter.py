def add(a, b):
    return a + b

lam = lambda x, y: x + y #does the same as function add
#x, y after the lambda are the parameters
#and after the : comes what you want your lambda to return
#to call a lambda you have to assign some variable to it like code above

print(lam(1, 2)) #lambdas are called the same way as functions
print((lambda x, y: x + y)(1, 2)) #2. way of calling lambda

l = [2, 3, 1, 4, 5]

#function for squaring and printing elems of a list
def square(func, arr): #func is param that gets a function, arr param that gets a list
    new = [] #empty list
    for i in arr: #looping through list arr
        n = func(i) #calling a function func, and assigning the value that,
        # that function returns to n
        new += [n] #appending n to the new list
    print(new) #printing all the elems of new

square(lambda x: x ** 2, l) #passing lambda function as argument to param func, and l to param arr
#that the main usage of lambdas, they are arguments for higher order functions
#higher order function is a function that gets the function as param or returns a function


n = sorted(l, key = lambda x: x % 2 == 0) #key is the way/rule how you want function sorted to sort you iterable
#in my case my function returns 1 if number is even, and 0 if it's odd
#which means even numbers have value 1 while odd numbers have value 0
#so to sorted function l list looks like this l = [1, 0, 0, 1, 0]
print(n)

#map is used if you want to modify some iterable based on some function

arr = [2, 3, 1, 4, 5]
n = map(lambda x: x ** 2, arr) #map is a function that has 2 params
#1. param is a function, 2. param has as many iterables as you want
#map takes on elems one by one from the iterable and passes them as args to the function
#it also returns instance of map, more about that later
print(n)
print(*n) #if you want to get the values you have to write the * before variable name

n = list(map(lambda x: x ** 2, arr)) #same as above but now that object is converted to list
print(n)

#map can only get one elem at a time from iterables,
#but there are 2 workarounds that i will show you

arr = [(2, 3), (1, 4), (5, 0)] #list of tuple pairs
n = list(map(lambda x: x[0] + x[1], arr)) #tuple pair is passed to the function as argument
print(n)

arr1 = [2, 1, 5]
arr2 = [3, 4, 0]
n = list(map(lambda x, y: x + y, arr1, arr2)) #elems one by one are passed from all the iterables to the function
print(n)

#filter is used when you want to filter, get elems from an iterable based on some logic
arr = [2, 3, 1, 4, 5]
n = list(filter(lambda x: x % 2 == 0, arr)) #1. param is function, 2. param i ONE iterable
#filter gets elems one by one and passes them to function, same as lambda
#return instance of filter
#if i hadn't convert it to list i would have to write *n to get the elems, same as with map
print(n)

#if you want to have more than one param in function than you have to store values as some collection
arr = [(2, 3), (1, 4), (5, -1)]
n = list(filter(lambda x: x[0] + x[1] >= 5, arr)) #passes tuple pair as argument
print(n) #[(2, 3), (1, 4)]

#zip stores elems of iterables as tuples
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = list(zip(a, b)) #takes as many iterables as you want as arguments
# and get their elems and stores them as tuple
print(c)

x = [(1, 'a'), (2, 'b'), (3, 'c')]
print(*x) #(1, 'a') (2, 'b') (3, 'c')
n = list(zip(*x)) #* unpacks them into pairs, look at the print above
#so know zip look at this as if you have passed 3 tuple pairs, (1, 'a') (2, 'b') (3, 'c')
#by getting elem by elem from each tuple and storing them as pairs
#it creates this:
print(n)

n = zip(*x)
print(*n) #(1, 'a') (2, 'b') (3, 'c')
print(*n) #empty
#zip creates lazy elements, which means they are created when needed, when you iterate thorugh them
#not when they are created, after you iterate through them, they are exhausted
#so you can use them only once, that's what happend above
#this is same happens to map, filter and zip
