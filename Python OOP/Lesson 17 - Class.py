#classes are blueprints for creating objects
#which means class Pet, below, can create objects like dog, cat, etc.
#instance is one object created from a certain class
#attribute is a variable that is the member of a class
#method is a function that is the member of a class

class Pet: #creating class Pet
    def __init__(self, name, owner, age): #special method __init__ known as initializer
        #initalizes the value of an instance when its created
        #purple self, is the instance itself, and it's always 1st param
        self.name = name #instance name is equal to the one you passed - 'jack'
        self.owner = owner #instance owner is equal to the one you passed - 'david'
        self.age = age #instance age is equal to the one you passed - 2

    def print_info(self): #you have to write param self otherwise it will return error
        print(self.name, self.owner, self.age) #jack david 2
        #they are called with self. to indicate that the attribute comes from that instance
        #bcs these are instance attributes
        #which means for different instances the same attribute has different values

dog = Pet('jack', 'david', 2) #here I didn't call __init__ method bcs that's called automatically
#as you can se the arguments that I passed to Pet are matching the params of __init__
#except argument for self is not passed and that's bcs that's done automatically
#when you create an instance the instance itself is passed to the self as first argument
dog.print_info() #same as with __init__ instance, dog, is passed automatically whether you want it or not
Pet.print_info(dog) #2. way of calling a method, but now I am calling it through class Pet that's why
#you have to pass dog manually

class Pet: #create class Pet
    pass

cat = Pet
print(type(cat)) #type
cat = Pet() #even if the class is empty you have to write () in order to create instance of class Pet
print(type(cat)) #__main__.Pet

cat.name = 'russel'
cat.age = 2
print(cat.name, cat.age)
#the code above will also work but that is not the clean way of coding your OOP project!!!