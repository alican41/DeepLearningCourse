def my_decorator(func):
    def wrapper():
        print("Wrapper function executed")
        func()
        print("Wrapper function executed")
        
    return wrapper


@my_decorator
def hello_world():
    print("Hello, World!")

hello_world()

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    @age.deleter
    def age(self):
        self.__age = None

ali = Person("Ali", 30)
print(ali.name)
ali.name = "Ali Can"
del ali.name
print(ali.name)
ali.age = 50
print(ali.age)
ali.age = 25
print(ali.age)

class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
print(MathOperations.add(10, 5))
print(MathOperations.subtract(10, 5))
print(MathOperations.multiply(10, 5))
print(MathOperations.divide(10, 5))

class Pizza:

    total_pizzas = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.total_pizzas += 1

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomato", "basil"])
    
    @classmethod
    def pepperoni(cls):
        return cls(["mozzarella", "tomato", "pepperoni"])
    
    @classmethod
    def get_total_pizzas(cls):
        return cls.total_pizzas

pizza1 = Pizza.margherita()
print(pizza1.ingredients)
pizza2 = Pizza.pepperoni()
print(pizza2.ingredients)

print(Pizza.get_total_pizzas())

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print(f"{self.name} says: Woof!")

    def move(self):
        print(f"{self.name} is running.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

barley = Dog("Barley")
barley.move()

from typing import overload, Union

class Calculator:

    @overload
    def add(self, a: int, b: int) -> int: ...  
    
    @overload
    def add(self, a: int, b: int, c: int) -> int: ...

    def add(self, a: int, b: int, c: int | None = None) -> int:
        if c is not None:
            return a + b + c
        return a + b
    
    @overload
    def process(self, value: str) -> str: ...

    @overload
    def process(self, value: int) -> int: ...

    def process(self, value: Union[str, int]) -> Union[str, int]:
        if isinstance(value, str):
            return value.upper()
        elif isinstance(value, int):
            return value * 2
        else:
            raise ValueError("Unsupported type")



calc = Calculator()
print(calc.add(10, 5))

result = calc.process("ali")
print(result)
