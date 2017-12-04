"""
基于TCP协议的服务端的程序

客户端-->服务端
    服务端你在么
操作步骤：
step1：初始化信息：
    ip：自己的ip
    port：自己的端口
    buf_size：

step2：创建socket对象
    socket(基于网络，TCP)
    bind(ip,port)
    listen()，监听客户端的链接

step4：accept()-->(client_socket，客户端的地址)

step5：数据交互：
    client_socket.recv(buf_size)-->data,接收数据
    data-->decode(编码),解码
    send(str.encode(编码))

step6：关闭资源，
    close()
"""
from socket import *
# 1.初始化信息
ip = "127.0.0.1"  # localhost,真实ip
port = 54321  # 改程序的端口号
address = (ip, port)  # 封装地址：ip+port
buf_size = 1024  # 服务端缓冲区的大小(单位是字节)

# 2.创建socket插座对象
# AF_INET,基于网络的
# SOCK_STREAM，TCP协议
# SOCK_DGRAM，UDP
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
# bind(),绑定该socket插座对象，和某个地址
tcp_server_socket.bind(address)
# 开启服务端的监听：5表示链接队列中的最大的数量。
tcp_server_socket.listen(5)

print("-----等待客户端的链接------")

# step3：接收客户端的链接请求：res(socket,客户端的address)
client_socket, client_adress = tcp_server_socket.accept()  # 该方法是阻塞式
print("来自 %s 的链接。。" % str(client_adress))

# step4：数据传递
data = client_socket.recv(buf_size)
data = data.decode("utf-8")

print("客户端传来的数据：%s" % data)

# step4：关闭资源
client_socket.close()  # 关闭和客户端链接的socket
tcp_server_socket.close()  # 关闭服务端的socket