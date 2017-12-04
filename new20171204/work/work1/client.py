"""
TCP编程：客户端和服务端，多句聊天
使用多线程
"""
from socket import *
from threading import Thread


#  多线程实现客户端读取输入，发送消息并阻塞
def client_input_msg(client_socket):
    while True:
        msg = input("客户端：")
        if not msg:
            print("聊天结束")
            break
        client_socket.send(msg.encode("utf-8"))


#  主线程中实现客户端接收来自服务端的消息，并阻塞

if __name__ == '__main__':
    ip = "192.168.253.1"
    port = 1234
    address = (ip, port)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(address)
    th = Thread(target=client_input_msg, args=(client_socket,))
    th.start()
    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print("服务端消息-->", data)
    client_socket.close()
    th.join()

