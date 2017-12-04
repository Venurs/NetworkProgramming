from socket import *

# ip = "192.168.253.1"
ip = "10.0.151.251"
port = 54321
address = (ip, port)
bufz_size = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind(address)
s.listen(5)
client_socket, add = s.accept()
print("客户端%s链接成功" % str(add))
while True:
    data = client_socket.recv(bufz_size)
    data = data.decode("utf-8")
    print("来自%s消息：%s", (add, data))
    re = input("服务端回复：")
    client_socket.send(re.encode("utf-8"))
    print("信息已回复，等待消息。。。。")

s.close()
