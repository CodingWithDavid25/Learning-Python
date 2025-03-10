s1 = "don\"t" #" used to assign string literal 1. way
#\ used to tell python that the \ should be part of the string
print(s1)
s2 = 'don\'t' #' used to assign string literal 2. way
#\ used to tell python that the ' should be part of the string
print(s2)
#triple " are multiple line strings 3. way
#the \ used to remove the extra enter
s3 = """\
subscribe 
and
like"""
#
#triple " are also used as multiple line comments in python
print(s3)

s4 = 'like \n comment' #\n special char for new line - same works with " string literal
print(s4)

s = "subscribe"
print(s[1]) #gets the 2nd char since positions start from 0
#prints U

#printing all chars using range function + indexing
for i in range(len(s)): #len() function returns length of a string
    print(s[i])

for i in s: #i becomes each char from string s
    print(i)

print(s.upper()) #converts all lower case chars to upper case
print(s.lower()) #converts all upper case chars to lower case
print(s.title()) #converts first letter to capital
print(s.islower()) #checks if all letters are lower
print(s.isupper()) #checks if all letters are upper
x = s.replace("b", "d") #replaces certain string part with another
#1. param is the old string and the 2. is the new string with which you want to replace old
print(s)


s = chr(70) #converts int number to string base on ASCII code
num = ord('F') #checks the value of F in ASCII code
print(num)
print(s)

