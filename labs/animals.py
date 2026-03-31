class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        return "animal sound"
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed        
    def speak(self):
        return f"{self.name} the {self.breed} says waf waf" 
    
    
    
    
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color        
    def speak(self):
        return f"{self.name} says meow meow"
    
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species        
    def speak(self):
        return f"{self.name} says chirp chirp"
    
class lion(Animal):
    def __init__(self, name, age, pride):
        super().__init__(name, age)
        self.pride = pride        
    def speak(self):
        return f"{self.name} says roar roar"
    
dog = Dog("Buddy", 3, "Bulldog")
cat = Cat("Mimi", 2, "White")
bird = Bird("Tweety", 1, "Canary")
lion = lion("Simba", 5, "Pride")

print(dog.speak())
print(cat.speak())
print(bird.speak())
print(lion.speak())