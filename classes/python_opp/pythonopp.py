# # student0 = {
# #     "name": "Rolf",
# #     "grades": (90, 90, 85, 88)
# # }

# # print(student0["name"])

# # def average(sequence):
# #     return sum(sequence) / len(sequence)

# # print(average(student0["grades"]))

# # student.average()

# class Student:
#     def __init__(self, name, grades = (0, 0, 0, 0)):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)

# student1 = Student("Rolf", (90, 90, 85, 88))
# student2 = Student("Anna", (78, 82, 80, 79))
# student3 = Student("Ben", (88, 91, 87, 90))
# student4 = Student("Lila", (92, 89, 94, 91))

# # print(student1.name)
# # print(student1.grades)

# print(student1.average())
# print(student2.average())
# print(student3.average())
# print(student4.average())

# # print(student2.name)
# # print(student2.grades)

# # print(student1)



# class Devices:
#     def __init__(self, name, connected_by, brand):
#         self.name = name
#         self.connected_by = connected_by
#         self.is_connected = True
#         self.brand = brand
#     def connect(self):
#         pass

#     def disconnect(self):
#         self.is_connected = False
#         pass



# class Keyboard(Devices):
#     def __init__(self, type, lang):
#         self.type = type
#         self.lang = lang


# class Mouse:
#     def __init__(self, brand, dpi, wireless):
#         self.dpi = dpi
#         self.wireless = wireless


# class Screen:
#     def __init__(self, brand, size, resolution):
#         self.size = size
#         self.resolution = resolution


# class Usb:
#     def __init__(self, brand, capacity, usb_type):
#         self.capacity = capacity
#         self.usb_type = usb_type


# class Charger:
#     def __init__(self, brand, power, port_type):
#         self.power = power
#         self.port_type = port_type


# class Camera:
#     def __init__(self, brand, megapixels, cam_type):
#         self.megapixels = megapixels
#         self.cam_type = cam_type


# class Headset:
#     def __init__(self, brand, wireless, mic):
#         self.wireless = wireless
#         self.mic = mic
        
        
        
#     # חיבור בין פונקציות ומחלקות    
        
# class Devices:
#     def __init__(self, name, connected_by, brand):
#         self.name = name
#         self.connected_by = connected_by
#         self.is_connected = True
#         self.brand = brand
#     def connect(self):
#         pass

#     def disconnect(self):
#         self.is_connected = False
#         pass



# class Keyboard(Devices):
#     def __init__(self, name, connected_by, brand, type, lang):
#         super().__init__(name, connected_by, brand)
#         self.type = type
#         self.lang = lang

# class Mouse(Devices):
#     def __init__(self,name, connected_by, brand, dpi, wireless):
#         super().__init__(name, connected_by, brand)
#         self.dpi = dpi
#         self.wireless = wireless

# class Screen(Devices):
#     def __init__(self, name, connected_by, brand, size, resolution):
#         self.size = size
#         self.resolution = resolution

# class Usb(Devices):
#     def __init__(self,name, connected_by, brand, capacity, usb_type):
#         super().__init__(name, connected_by, brand)
#         self.capacity = capacity
#         self.usb_type = usb_type

# class Charger(Devices):
#     def __init__(self, name, connected_by, brand, power, port_type):
#         super().__init__(name, connected_by, brand)
#         self.power = power
#         self.port_type = port_type

# class Camera(Devices):
#     def __init__(self, name, connected_by, brand, megapixels, cam_type):
#         super().__init__(name, connected_by, brand)
#         self.megapixels = megapixels
#         self.cam_type = cam_type

# class Headset(Devices):
#     def __init__(self, name, connected_by, brand, wireless, mic):
#         super().__init__(name, connected_by, brand)
#         self.wireless = wireless
#         self.mic = mic

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
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