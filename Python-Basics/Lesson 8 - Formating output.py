x = 3
y = 2
#sep is a parameter for separation when you print multiple values
print(x, y, sep = '-') #3-2
a = [1, 2, 3]
print(*a, sep = '-') #1-2-3

#old way where you merge strings to format your output but not very clean code
print(str(x) + " is greater then " + str(y))
#f-string used for formating the output, fastest way compared to % and .format()
print(f"{x} is greater then {y}") #{} are used to evaluate the variable
print(f'{5+5}')  #{5+5} will just evaluate the expression
print(f"{5+5=}") #{5+5=} will evaluate and print the expression before =
print(f'{x+y}')  #{x+y} will just evaluate the expression
print(f"{x+y=}") #{x+y=} will evaluate and print the variable names before =

num = -3000.12345
print(f"{num:=>+30,.2f}")

#Align->sign->alternative form(#)->leading zeros->width->grouping->precision->type
#> (alignment method) = right alignment
#before alignment comes what you want your line to be filled with if you don't match the width number
#+ (sign) = prints + if num > 0, prints - if num < 0
#30 (width) = how many characters you want in a line
#, (grouping) = prints , after thousands
#.2 (precision) = rounding
#f (type) = fixed-point presentation type for decimal and float

#for all details on f-string formating, check official python documentation below
#https://docs.python.org/3/library/string.html#format-string-syntax