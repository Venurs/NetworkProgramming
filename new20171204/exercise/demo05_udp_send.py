"""
udp编程：发送的一方
"""
from socket import *
# 1.初始化信息
ip = "10.0.151.228" # 接收方法的ip
port = 4406 # 接收方的端口
address = (ip, port)

# 2.创建socket对象
# AF_INET,基于网络
#SOCK_DGRAM，使用UDP协议
udp_send_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("请输入：")
    if not msg:
        print("结束发送方程序。。")
        break

    # 发送
    udp_send_socket.sendto(msg.encode("utf-8"), address)


udp_send_socket.close()
