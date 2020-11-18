import random
import socket
import sys

ip = 'localhost'
port = 5538

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, 5538)

try:
    s.bind(server_address)
    print("Conexão Estabelecida ")
except:
    print("Erro ao se conectar ")
print("Aperte Ctrl+c para sair do programa !!")
taxa_perda = 0.1

while True:
    print("|-------------------------------------------|")
    print("|----------- Server is listening -----------|")
    data, address = s.recvfrom(port)
    if(random.random() < 1 - taxa_perda):
        print("|  2. Server received: ", data.decode('utf-8'), "   |")
        # send_data = input("Type some text to send => ")
        send_data = 'recebido'
        s.sendto(send_data.encode('utf-8'), address)
        print("|  1. Server sent : ", send_data,"              |")
        print("|-------------------------------------------|\n")
    else:
        print("|----------------- Perdido -----------------|")
        print("|-------------------------------------------|\n")

