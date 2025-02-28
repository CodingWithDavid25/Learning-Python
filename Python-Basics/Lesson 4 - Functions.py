def check_even(number): #syntax for functions: def [function name] ([parameters - optional])
    if number % 2 == 0: #check if number is even
        print(number)
        print("is even")

for i in range(1, 11):
    check_even(i) #same as number = i

def even_range(start = 1, end = 10):
    count = 0
    for i in range(start, end+1):
        if i % 2 == 0:
            count += 1
    return count #return means we want our function to give us some value

x = even_range(1, 10) #x gets the value of count that even_range() function returns

def print_range(start, /, *, end):
    # everything before / must be  passed positionally,
    # everything after * must be passed as keyword arguments
    for i in range(start, end+1):
        print(i)

print_range(1, end = 2) #correct way of calling the function print_range()
#end = 2 is passing value using keyword arguments
#end is a keyword