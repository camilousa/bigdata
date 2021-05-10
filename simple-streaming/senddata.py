import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 9897))
s.listen()

conn, addr = s.accept()

print(f'conectado con {addr}')



while True:
	data = input('introduzca una palabra: ')
	conn.sendall(bytes(data+'\n', encoding='utf-8'))


