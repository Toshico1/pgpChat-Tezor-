import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8887))
sock.listen(5)
# sock.setblocking(False)  # не ждем подключения, а обрабатываем исключением
sock.settimeout(5)  # если клиентов нет 5 секунд то прыгаем в исключение, раз в 5 сек
# sock.settimeout(0)  -> sock.setblocking(False)
# sock.settimeout(None)  -> sock.setblocking(True)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('No clients')
    except KeyboardInterrupt:
        sock.close()
        print('Prog was stopped')
        break
    else:
        client.setblocking(True)  # ждем подключения, зависая в 'recv'
        result = client.recv(1024)
        client.close()
        print('Message:', result.decode('utf-8'))

# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0) # подробнее