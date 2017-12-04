"""

"""
from socket import *

ip = "10.0.151.251"
prot = 1034

address = (ip, prot)
#  图片路径


file = open("new_copy.jpg", mode="wb")
s = socket(AF_INET, SOCK_STREAM)
s.bind(address)
s.listen(5)
s_socket, addre = s.accept()
print("收到来自%s的链接，等待传输文件。。。。" % str(addre))
while True:
    data = s_socket.recv(1024)
    if not data:
        break
    file.write(data)

print("传输完成")
file.close()
s.close()
