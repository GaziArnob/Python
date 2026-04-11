from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass 

class Lion(Animal):
    def make_sound(self):
        print("Roar")

class cat(Animal):
    def make_sound(self):
        print("Meow")        

cat1 = cat()
lion = Lion()
lion.make_sound()
cat1.make_sound()