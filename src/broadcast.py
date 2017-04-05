import socket

IP = '192.168.10.255'
PORT = 8887
MESSAGE = "Pidentify"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(MESSAGE, (IP, PORT))
s.close()
