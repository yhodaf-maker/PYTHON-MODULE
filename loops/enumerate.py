#task 1

# names = ["Alice", "Bob", "Charlie"]

# for index, name in enumerate(names):
#     print(index, name)
    
#task 2
# servers = ["app-01", "app-02", "app-03"]

# for index, server in enumerate(servers, start=1):
#     print(index, server)
   
#task 3
errors = ["disk full", "timeout", "connection lost"]

for index, error in enumerate(errors):
    if index % 2 == 0:
        print(index, error)