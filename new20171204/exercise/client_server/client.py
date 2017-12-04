"""
客户端-->服务端
    ：你干啥呢
服务器-->客户端
    ：我不告诉你
客户端-->服务端
    ：那我告诉你我干啥呢
服务端-->客户端
    ：你咋那么无聊
...
"""

from socket import *


ip = "192.168.253.1"
# ip = "127.0.0.81"
port = 54321
address = (ip, port)

c = socket(AF_INET, SOCK_STREAM)
c.connect(address)
c.send("你好".encode("utf-8"))
while True:
    print("来自服务器回复：", c.recv(1024).decode("utf-8"))
    msg = input("客户端发送：")
    if msg == "exit":
        break
    c.send(msg.encode("utf-8"))
    print("信息已发送，等待回复。。。。")

c.close()




