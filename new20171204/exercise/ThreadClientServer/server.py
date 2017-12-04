"""
echo程序的服务端
"""
from socket import *
from threading import Thread


def tcplink(client_socket, client_address):

    # 4.循环处理数据
    while True:
        # step3：接收数据
        data = client_socket.recv(1024)
        if not data:
            print("%s,客户端已经结束。。" % str(client_address))
            break
        # step4：发送数据
        data = "ECHO:" + data.decode("utf-8")
        client_socket.send(data.encode("utf-8"))
    client_socket.close()


if __name__ == '__main__':

    # 1.初始化信息
    ip = "127.0.0.1"
    port = 32345
    address = (ip, port)

    # 2.创建服务端对象
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)
    print("--服务端已经建立。。。等待客户端的链接")
    while True:
        client_socket, client_address = server_socket.accept()
        print("--已有客户端链接。。%s" % str(client_address))
        # 3.等待链接
        t = Thread(target=tcplink, args=(client_socket, client_address))
        t.start()

