from socket import *
from threading import Thread

BUF_SIZE = 1024


def listen_client(client_socket, l_client_list):
    print("2222222")
    while True:
        data = client_socket.recv(BUF_SIZE).decode("utf-8")
        if not data:
            client_socket.close()
            l_client_list.remove(client_socket)
            break
        client_socket.send(("ECHO:%s" % data).encode("utf-8"))


if __name__ == '__main__':
    IP = "localhost"
    PORT = 10045
    address = (IP, PORT)

    tcp_sever_socket = socket(AF_INET, SOCK_STREAM)
    tcp_sever_socket.bind(address)
    tcp_sever_socket.listen(3)
    print("-----等待客户端连接------")
    tcp_client_socket, tcp_client_address = tcp_sever_socket.accept()
    print("接收到:%s" % str(tcp_client_address))
    client_list = []
    while True:
        tcp_client_socket, tcp_client_address = tcp_sever_socket.accept()
        print("---------接收到%s的连接--------" % str(tcp_client_address))
        if tcp_client_socket not in client_list:
            client_list.append(tcp_client_socket)
            print("接收到:%s" % str(tcp_client_address))
            t = Thread(target=listen_client, args=(tcp_client_socket, client_list))
            t.start()
        # data = tcp_client_socket.recv(buf_size)
        # if not data:
        #     break
        # tcp_client_socket.send(data)

    # tcp_sever_socket.close()
