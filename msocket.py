# -*- coding: cp1254 -*-
import socket

#
# Kullan�lacak olan IP adresi ve port numaras�
host = ''        
port = 9999

#
# Servver olusturulup IP ve Port numaras� veriliyor..
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Server �al��t�r�p dinlemeye ba�l�yor.
s.listen(1)

# Veriler al�n�yor.
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if(data):
    	print(str(data))
    conn.sendall(data)
    
conn.close()
