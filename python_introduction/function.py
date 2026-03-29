# # Python Functions 
# def hello():
#     print("Hello World")
    
# print(hello)

# hello()

# print(type(hello))


# # Get user age in seconds

# def user_age_in_seconds():
#     age = int(input("Whats is your age: "))
#     age_seconds = age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is: {age_seconds}")

# user_age_in_seconds()
def passed(grades):
    result = []

    for g in grades:
        if g > 60:
            result.append(g)

    return result
grades = [55, 70, 85, 40, 90]
passed_students = passed(grades)
print(f"Passed students: {passed_students}")