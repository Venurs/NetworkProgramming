"""
echo程序的客户端
"""
from socket import *
# 1.初始化信息
ip = "127.0.0.1"
port = 32345
address = (ip, port)
buf_size = 1024


# 2.创建客户端对象
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(address)
print("客户端已经建立，并且申请了连接。。。")
# 4.数据交互
while True:
    # step1:读键盘
    msg = input()
    if not msg:
        print("客户端即将结束。。")
        break
    # step2：发送数据
    client_socket.send(msg.encode("utf-8"))
    # step5：接收数据
    data = client_socket.recv(buf_size)
    print(data.decode("utf-8"))

client_socket.close()