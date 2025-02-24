#print(1)
#print(2)
#print(3)
#print(4)
#print(5)
#print(6)
#print(7)
#print(8)
#print(9)
#print(10)

#i goes through all the values in the sequence
for i in range(11, 2, -1): #range(start, end, step)
    #range creates sequence of numbers from start until end with the specified step
    #for goes through all the values in the sequence, and i becomes one value at a time
    print(i)

#for used when we know the exact number of iterations

for i in "abcd": #for that iterates through abcd, i = a, than i = b until the end
    print(i)

x = 2345

#while used when we have to perform some operations to find the number of iterations

while x > 0: #while loop is run until x > 0 when this isn't met it breaks from the while loop
    digit = x % 10 #0 1 2 3 4 5 6 7 8 9 - possible values
    x //= 10       #same as x = x // 10 - used to trim the number's last digit
    print(digit)

for i in range(1, 5):
    for j in 'abcd':#first this loop is finished than the outer ones
        print(i, j)

for i in range(1, 4):
    y = 1
    while y < 3:    #first this loop is finished than the outer ones
        print(i, y)
        y += 1      #incrementing (increasing value by 1) the y