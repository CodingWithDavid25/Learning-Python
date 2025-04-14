class Animal:
    _statement = 'I love animals!' #class attribute
    #they are created in class scope outside of methods
    #_ before name, convention for protected variable
    def __init__(self, type):
        self.type = type #public variable by convention
        self.__name = 'max' #instance variable
        #private variable by convention, __ before variable name mangles to variable name
        #from __name to _[clas_name]__[variable_name]

dog = Animal('dog')
print(dog.type) #dog
print(dog._Animal__name) #used to access 'private' variable
print(Animal._statement) #gets 'protected' variable
