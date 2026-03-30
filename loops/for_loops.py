# friends = ["Rolf", "Bob", "Jen", "Anne"]    

# for friend in friends:
#     print (f"{friend} is my friend")

# range function
# for num in range(4):
#      print(f"{num} is my friend")
     
# for num in range(0, 10000, 3):
#      print(f"{num} is my friend")
# grades = [80, 75, 90, 100, 85]
# total = 0
# amount = len(grades)

# for grade in grades:
#     total += grade
    
# print(total / amount)

# task 1

# for num in range (1, 6):
#     print(num)

# task 2
# for num in range (5, 0, -1):
#     print(num)
    
# task 3 
# for num in range (2, 11, 2):
#     print(num)

# task 4
# for number in range (1, 11):
#    print(number)

# task 5
# for number in range(0, 20, 3)   :
#     print(number)   

# task 6
# for i in range(5):
#     print("Hello")

# task 7
# for num in range(0, 10):
#     print(num)

# task 8
# for num in range(2, 21, 2):
#     print(num)
    
# task 9
# for num in range(10, -1, -1):
#     print(num)

# task 10

# total = 0
# for num in range(1, 101):
#     total += num
    
# print(total)

# print(sum(range(1, 101)))

#task 11

# names = ["Yehuda", "David", "Noa", "Sara"]

# for name in names:
#     print(name)

#task 12

# names = ["Yehuda", "David", "Noa", "Sara"]
# print(len(names))

# task 13

# numbers = [1,3,5,77,87,99]
# total = 0
# for number in numbers:
#     total += number
# print(total)

# task 14
# numbers = [1,3,5,77,87,99]
# print(max(numbers))
# print(min(numbers))

#15
# names = ["avi", "aoed", "roy", "noam", "yehuda"]
# for name in names:
#     if name.startswith("a"):
#         print(name)

#task 16
# numbers =[1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

#task 17
# numbers =[1, 2, 4, 14, 18, 20, 21, 22, 23, 24]
# count = 0
# for number in numbers:
#     if number > 10:
#         count += 1
# print(count)

#task 18
# numbers = [1, 2, 4, 14, 18, 20, 21, 22, 23, 24]
# for number in numbers:
#     if number % 2 == 0 and number % 3 == 0:
#         print(number)

#task 19        
# for num in numbers:
#     print(num ** 2)

#task 20
numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)     
        
print(positive_numbers)