# set([[1, 2], [3, 4]])
# # print(set([[1, 2], [3, 4]]))
# set{(1, 2), (3, 4)}
# # print(set{(1, 2), (3, 4)})
# set_of_tuples = {(1, 2), (3, 4)}
# print(set_of_tuples)
# print((2, 1) in set_of_tuples)
# print((3, 1) in set_of_tuples)
developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}
# print("Alice" in developers)
# print("Alice" in admins)
# print(developers.union(admins))
# print(developers | admins)
# print(developers.intersection(admins))
# print(developers.difference(admins))
# print(developers - admins)
# print(developers - admins)
# developers = {"Alice", "Bob", "Charlie"}

# result = developers.intersection(admins)

# print(result)
# print(developers)
developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}

print("Union:", developers | admins)
print("Intersection:", developers & admins)
print("Difference:", developers - admins)