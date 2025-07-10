###########################################
# Traditional Class
###########################################


# class Dog:
#     #Constructor
#     def __init__(self,name):
#         self.name = name

#     # Method
#     def bark(self):
#         print(f"{self.name} says Woof!")

#     # Starting representation of the object
#     def __repr__(self):
#         return f"Dog(name='{self.name}')"
    

# #Creating  an Object of the class
# my_dog = Dog("Buddy")

# #Accessing method
# my_dog.bark()

# #Accessing Property(__repr__)
# print(my_dog)


# Dog is a class.
# my_dog is an object (or instance) of that class.
# name is a property/attribute.
# bark() is a method.

###########################################
# @staticmethod in python
###########################################

# A static method doesn't depend on class instance (self) or class (cls)
# Its just a regular function inside a class - grouped logically but doesn't operate on the class/object directly.


# class Math:

#     @staticmethod
#     def add(a,b):
#         return a + b

# # Can call without creating object
# print(Math.add(4, 5)) # Output: 9

###########################################
# @dataclasses
###########################################

from dataclasses import dataclass
from typing import ClassVar

@dataclass
class American:
    
    national_language : ClassVar[str] = "English"
    national_food : ClassVar[str] = "HumBurger"
    normal_body_temprature: ClassVar[float] = 98.6
 
    name: str
    age: int
    weight: float
    liked_food: str

    # Instance Method
    def speaks(self):
        return f"{self.name} is speaking... {American.national_language}"

    def eats(self):
        return f"{self.name} is eating...."
    
    # Static Method
    @staticmethod
    def country_language():
        return American.national_language
    

    # Class Method
    @classmethod
    def cultural_info(cls):
        return f"Language: {cls.national_language}, Food: {cls.national_food}, Body Temp: {cls.normal_body_temprature}"

# invoking the static method
print(American.country_language())
    
# invoking class Method
print(American.cultural_info())

# Creating an instance of the class
john = American(name = "Hassan" , age = 23, weight = 58, liked_food= "Biryani")

# invoking instance method
print(john.speaks())
print(john.eats())
print(john)
print(john.name)
print(john.age)
print(john.weight)
print(American.national_language)