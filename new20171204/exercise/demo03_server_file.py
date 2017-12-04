"""
服务端：接收客户端来的图片
"""
from socket import *
# 1.初始化信息
ip = "127.0.0.1"
port = 22345
address = (ip, port)
buf_size = 1024  # 服务端的缓冲区大小

# 2.创建socekt
server_socekt = socket(AF_INET, SOCK_STREAM)
server_socekt.bind(address)
server_socekt.listen(5)
print("服务端已经建立，等待客户端的链接。。。。")
# 3.接收客户端的请求
client_socket,client_address = server_socekt.accept()
print("已有客户端连入：%s" % str(client_address))


# 4.接收图片数据-->本地文件中
# step1：获取文件对象
file = open("aa.jpeg", mode="wb")
# 循环中
# step2：接收客户端传来的数据
# step3：向改文件对象中写入数据
while True:
    img_data = client_socket.recv(buf_size)
    if not img_data:
        print("数据读取完毕。。")
        break
    file.write(img_data)

client_socket.close()
server_socekt.close()