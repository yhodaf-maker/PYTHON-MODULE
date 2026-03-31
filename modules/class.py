from turtle import color


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        
    def show(self):
        print(self.name, self.age, self.job)
        
 
 
person1 = Person("yehuda", 26, "developer"  )    
person1.show()

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def show(self):
        print(self.brand, self.model, self.year, self.color)
        
car1 = Car("Volkswagen", "Golf", 2015, "white")
car1.show()


class book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        
    def show(self):
        print(self.title, self.genre)

book1 = book("the great gatsby", "F. Scott Fitzgerald", 1925, "Classic Literature")
book1.show()

class dog:
    def __init__(self, name, age, breed, weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight
    
    def show(self):
        print(self.name, self.age, self.breed, self.weight)
        
dog1 = dog("timmy", 9, "chihuahua", 10)
dog1.show()


class phone:
    def __init__(self, brand, model, price, battery):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = battery
    
    def show(self):
        print(self.battery)
        
phone1 = phone("apple", "iphone15", "1200", "4000mAh")
phone1.show()

class student:
    def __init__(self, name, age, grade, school):
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
    
    def show(self):
        print(self.name, self.grade)
        
student1 = student("Yehuda","26", "85", "iitc")
student1.show()