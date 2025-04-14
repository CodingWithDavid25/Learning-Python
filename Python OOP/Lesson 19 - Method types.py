class Animal:
    _sound = '' #class attribute
    def __init__(self, type):
        self.type = type #instance attribute

    #instance method operates on instance-level date
    def animal_type(self): #instance method, first param is instance
        print(f'This animal type is {self.type}') #uses instance attribute

    #class method operates on class-level data
    @classmethod #decorator for class method
    def animal_vocal(cls, vocal): #class method, first param is class
        cls._sound = vocal #changes class attribute
        print(f'This animal sound is {cls._sound}')

    #static method is only different from function bcs it belongs to class namespace,
    #so it has to be called via class name, or instance name
    @staticmethod
    def animal_msg(): #static method, gets no class or instance as param
        print('I love this owner!')

dog = Animal('dog') #instance of Animal, dog

#to call instance method object has to be created
dog.animal_type() #. implicitly passes dog as first param
Animal.animal_type(dog) #you have to pass instance manually

#to call class method object doesn't have to be created
dog.animal_vocal('woof woof') #. implicitly passes Animal class since . operator knows that dog is instance of Animal
Animal.animal_vocal('woof woof') #. implicitly passes Animal class

#to call static method object doesn't have to be created
Animal.animal_msg() #. tells python that the function comes from Animal class namespace
dog.animal_msg()
