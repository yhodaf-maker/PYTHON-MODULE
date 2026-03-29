host_port = ("127.0.0.1", 3000)
print(host_port)
print(type(host_port))
print(host_port[0])  # host
print(host_port[1])  # port
red_rgb = (255, 0, 0)
single_value = (5)
print(type(single_value))  # <class 'int'>
single_value_tuple = (5,)
print(type(single_value_tuple))  # <class 'tuple'>
print(host_port[:1])
print(host_port[-2:])
host_port[0] = "localhost"