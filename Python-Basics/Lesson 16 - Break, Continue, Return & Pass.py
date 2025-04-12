for i in range(1, 11):
    if i == 7:
        break #exits the loop
    print(i)
else: #else after for or while checks if the break was triggered
      #if it was triggered it won't enter this else scope
    print('no break')


for i in range(1, 11):
    if i == 7:
        continue #skips the rest of the code from this point on
    print(i)


def add(a, b):
    return a + b #return value, so your function gives you that value, it basically acts as variable

x = add(1, 2) #x = 3
print(x) #3

def check_winner():
    pass #does nothing, tells programmer that this function should be coded, but maybe he doesn't know how yet
    #it's basically used to write cleaner code or for some symmetric or coherence reasons
    #can be used with anything that has a scope

check_winner() #nothing
