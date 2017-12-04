from socket import *

ip = "10.0.151.251"
prot = 1034

address = (ip, prot)
file = open("old_copy.jpg", mode="rb")
c = socket(AF_INET, SOCK_STREAM)
c.connect(address)
while True:
    data = file.read()
# if not data:
#     break
# print(data)
    c.send(data)
file.close()
c.close()




