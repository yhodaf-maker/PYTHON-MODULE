# # 
# car_brand = "Toyota"
# car_model = "Corola"
# car_year = 2012
# car_tank = 1.4

# car_list = [("Brand", car_brand), ("Model", car_model), ("Year", car_year), ("Tank", car_tank)]
# print(car_list)

# cars = [
#     {"brand": "Toyota",    "model": "Corolla",  "year": 2012, "tank": 1.4},
#     {"brand": "Honda",     "model": "Civic",    "year": 2018, "tank": 1.5},
#     {"brand": "Ford",      "model": "Mustang",  "year": 2020, "tank": 5.0},
#     {"brand": "BMW",       "model": "M3",       "year": 2021, "tank": 3.0},
#     {"brand": "Tesla",     "model": "Model 3",  "year": 2022, "tank": 0.0},
#     {"brand": "Chevrolet", "model": "Camaro",   "year": 2019, "tank": 6.2},
#     {"brand": "Audi",      "model": "A4",       "year": 2017, "tank": 2.0},
#     {"brand": "Mercedes",  "model": "C-Class",  "year": 2023, "tank": 2.0},
#     {"brand": "Hyundai",   "model": "Elantra",  "year": 2016, "tank": 2.0},
#     {"brand": "Volkswagen","model": "Golf",     "year": 2015, "tank": 1.6},
# ]


# human_philip = {
#     "name": "Philip",
#     "age": 24,
#     "color": "ASHKENAZ",
#     "occupation": "Junior DevOps Engineer",
#     "is_cool": True,
#     "hobbies": ["Army", "Gaming", "Cars"]
# }

# philip_list = [
#     ("name", "Philip"),
#     ("age", 24),
#     ("color", "ASHKENAZ"),
#     ("occupation", "Junior DevOps Engineer"),
#     ("is_cool", True),
#     ("hobbies", ["Army", "Gaming", "Cars"]),
# ]

# print(philip_list[1][1])
# print(human_philip["age"])

# #task 1
# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30,
#     "Anne": 27, 
    
# }
# print(friend_ages["Anne"])

#task 2+3

# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30
# }

# friend_ages["Bob"] = 20
# friend_ages["Rolf"] = 40
# print(friend_ages)

#task 4+5
# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80,
#     "Anne": 100
# }
# if "Bob" in student_attendance:
#     print("Bob is here")
    
# for student in student_attendance:
#     print(student)

# for student in student_attendance:
#      print(student+" "+str(student_attendance[student]))
     
# for student, grade in student_attendance.items():
#     print(student, grade)

#task 8
# student_attendance = {
#     "Rolf": 100,
#     "Bob": 80,
#     "Anne": 60
# }
# # total = 0
# # for grade in student_attendance.values():
# #     total += grade

# # average = total / len(student_attendance)
# # print(average)

# average = sum(student_attendance.values()) / len(student_attendance)
# print(average)

#task 9
# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30}
# ]
# print(friends[1]["name"])

#task 10
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]

result = []
for friend in friends:
   if friend["age"] > 25:
    result.append(friend)

print(result)
