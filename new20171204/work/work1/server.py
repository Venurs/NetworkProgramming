"""
服务端
多线程实现服务端读取输入，信息发送给客户端
主线程实现服务端读取数据
"""

from socket import *
from threading import Thread


def server_input_send(server_socket_accept):
    while True:
        data = server_socket_accept.recv(1024).decode("utf-8")
        if not data:
            break
        print("客户端消息-->", data)


if __name__ == '__main__':
    ip = "192.168.253.1"
    port = 1234
    address = (ip, 1234)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)
    print("服务器构建完毕，等待链接。。。")
    server_socket_accept, server_address = server_socket.accept()
    print("%s已连接到该服务器" % str(server_address))
    th = Thread(target=server_input_send, args=(server_socket_accept,))
    th.start()

    while True:
        msg = input("服务端：")
        if not msg:
            print("服务端退出聊天")
            break
        server_socket_accept.send(msg.encode("utf-8"))
    th.join()
    server_socket_accept.close()

