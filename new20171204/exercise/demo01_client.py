"""
基于TCP的客户端程序
step1：初始化信息
    ip：要链接的服务端的ip
    port：要链接的服务端的端口
        自己的端口，由系统分配
    buf_size,

step2：创建socket对象
    socket(基于网络，TCP)
    connect()-->申请链接

step3：数据交互
    send(字符串.encode())
    recv(buf_size)-->data
            decode()

step4：关闭
    close()
"""
from socket import *

# 1.提供信息
ip = "127.0.0.1"  # 当前客户端程序，要链接的服务端的ip
port = 54321  # 要链接的服务端的程序的端口号
address = (ip, port)
buf_size = 1024

# 2.创建sokcet对象
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 去链接服务端
tcp_client_socket.connect(address)  # 表示链接服务端

# 3.数据交互
# 从终端输入：
msg = input("请输入：")  # "你在么"--->编码

tcp_client_socket.send(msg.encode("utf-8"))

# 4.关闭
tcp_client_socket.close()

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
