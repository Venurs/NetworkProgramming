"""
基于UDP协议的接收方
"""
from socket import *

# 1.初始化信息
ip = "10.0.151.228"  # 自己的ip
port = 4406 # 自己的port
address = (ip, port)
buf_size = 1024

# 2.创建socket对象
udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)

# 3.结束发送来的数据
while True:
    print("等待别人给我发送的数据。。")
    data, send_address = udp_recv_socket.recvfrom(buf_size)  # udp接收数据，返回值是一个元组(data,发送方)
    print("来自：%s 发送来的消息：%s" % (str(send_address), data.decode("utf-8")))



