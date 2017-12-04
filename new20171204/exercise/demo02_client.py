from socket import *

# 1.初始化信息
ip = "127.0.0.1"
port = 12345
buf_size = 1024
address = (ip, port)

# 2.创建socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
# 3. 申请链接服务端
tcp_client_socket.connect(address)

# 4.数据交互
while True:
# A：客户端读键盘
    msg = input("请输入：")  # 阻塞式
    if not msg:
        print("客户端要跑。。")
        break
# B：客户端发送数据
    tcp_client_socket.send(msg.encode("utf-8"))
# F：客户端接收数据
    data = tcp_client_socket.recv(buf_size)  # 阻塞式
    data = data.decode("utf-8")
    print("服务端说：", data)

# 关闭资源
tcp_client_socket.close()