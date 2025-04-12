def hamburger(a, *toppings, b): #*[name] stores as many positional arguments as tuple
    #you can have other parameters before and after,
    #but those after have to be assigned via keyword arguments
    print(f'a = {a}, b = {b}') #a = onions, b = ketchup
    print(toppings) #('pickles', 'mayo')
    print(type(toppings)) #<class 'tuple'>

hamburger('onions', 'pickles', 'mayo', b = 'ketchup')

def store(a, **kwargs): #**[name] stores as many keyword arguments as dictionary
    #keyword is key, value is value
    #you can have other parameters only before
    #they can be assigned via keyword and via positional args
    print(f'a = {a}') #a = 0
    print(kwargs) #{'mayo': 1.5, 'onions': 0.5, 'pickles': 3}

store(a = 0, mayo = 1.5, onions = 0.5, pickles = 3)

#you can have both, *args and **kwargs at the same functon
#example below will be a nice test if you have understood the topic

def example(a, *args, b, **kwargs):
    print(f'a = {a}  b = {b}')
    print(args)
    print(kwargs)

example(2, 1, 3, 4, b = 5, aa = 11, bb = 22, cc = 33)