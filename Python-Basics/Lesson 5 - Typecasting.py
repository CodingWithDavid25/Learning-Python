x = int(input("Type some integer: ")) #input() function used for user input
print(x, type(x)) #input() function always returns string so thats why we need typecasting

#explicit typecasting since you specificly want the x to be converted to int
y = int(x) #int() - class that converts x in int
print(y, type(y), y ** 2)

z = float(x) #float() - class that converts x in float
print(z, type(z))


t = bool(0) #bool() - class that converts x in bool
#bool() returns True if string is not empty or number is not 0, otherwise returns False
print(t, type(t))

a = 0
#implicit typecasting since python does it on his own
if a:  #checks if bool(a) is TRUE
    print(a)
