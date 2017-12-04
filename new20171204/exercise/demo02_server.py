from socket import *

# 1.初始化信息
ip = "127.0.0.1"
port = 12345
buf_size = 1024
address = (ip, port)

# 2.创建socket
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind(address)
tcp_server_socket.listen(5)

# 3.接收客户端的请求
client_socket, client_address = tcp_server_socket.accept()  # 阻塞

# 4.数据交互
while True:
# C：服务端接收数据
    data = client_socket.recv(buf_size)  # 阻塞式
    if not data:
        print("客户端已经退出。。")
        break
    data = data.decode("utf-8")
    print("客户端说：", data)
# D：服务端接收键盘
    msg = input("input：")  # 阻塞
# E：服务端发送数据
    client_socket.send(msg.encode("utf-8"))


# 关闭
client_socket.close()
tcp_server_socket.close()


