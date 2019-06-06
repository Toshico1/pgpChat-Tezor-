import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.192.222.129', 8887))  # устанавливаем прямое подключение к серверу
message = input('M: ')
while True:
    sock.send(message.encode())


sock.close()
