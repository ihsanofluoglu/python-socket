# -*- coding: cp1254 -*-
import socket

#
# Kullanılacak olan IP adresi ve port numarası
host = ''        
port = 9999

#
# Servver olusturulup IP ve Port numarası veriliyor..
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Server çalıştırıp dinlemeye başlıyor.
s.listen(1)

# Veriler alınıyor.
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if(data):
    	print(str(data))
    conn.sendall(data)
    
conn.close()
