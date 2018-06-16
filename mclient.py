# -*- coding: cp1254 -*-
import socket

# Server dosyas�nda ki ba�l� port numaras�yla ayn� port olmas� gerekiyor.
host = socket.gethostname()    
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# baglant� sagland�ktan sonra veriler gonderilebilir
s.sendall(b'Hello, world\0')
data = s.recv(1024)
s.close()

print('Received', repr(data))
