# -*- coding: cp1254 -*-
import socket

# Server dosyasında ki bağlı port numarasıyla aynı port olması gerekiyor.
host = socket.gethostname()    
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# baglantı saglandıktan sonra veriler gonderilebilir
s.sendall(b'Hello, world\0')
data = s.recv(1024)
s.close()

print('Received', repr(data))
