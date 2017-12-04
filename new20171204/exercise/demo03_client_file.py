from socket import *
# 1.初始化信息
ip = "127.0.0.1"
port = 22345
address = (ip, port)

# 2.创建socket
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(address)

# 3.读取本地的图片-->服务端
# step1：获取文件对象
# step2：操作文件对象，读取数据
# step3：将读到的数据，写出

file = open(r"C:\Ruby\pro\aa.jpeg", mode="rb")
img_data = file.read()  # 读取所有
client_socket.send(img_data)


# 4.关闭
client_socket.close()
