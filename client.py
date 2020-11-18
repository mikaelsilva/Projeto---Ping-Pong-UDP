import numpy as np
import socket
import time
import sys

ip = 'localhost'
port = 5538

while True:
    # Create socket for server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.settimeout(1)

    print("     ** Ctrl+c para sair do programa **")
    RTT = []
    pacotesPerdidos = 0

    print("| ----------------------------------------- |")
    n = int(input('|  Quantas mensagens deseja enviar?  '))
    print("|                                           |")
    # Let's send data through UDP protocol
    for count in range(1,n+1):
        
        try:
            send_data = "Enviando msg n " + str(count)
            s.sendto(send_data.encode('utf-8'), (ip, port))
            timeSend = int(round(time.time() * 1000*1000))
            print("|  1. Client Sent : ", send_data,'      |')
            data, address = s.recvfrom(port)
            rtt = int(round(time.time() * 1000*1000)) - timeSend
            RTT.append(rtt)
            print('|  RTT: ',rtt,'microsegundo                   |')
            print("|  2. Client received : ", data.decode('utf-8'), '          |')
            print('|                                           |')
        except:
            pacotesPerdidos += 1
            print("|              Pacote perdido               |")
            print("|                                           |")
    
    # close the socket
    s.close()
    #print("Retornou PACOTES - ", RTT , len(RTT))
    if(len(RTT) != 0 ):
        RTT = np.array(RTT)
        print("|                                           |")
        print("| Pacotes enviados:  ",n ,'                    |')
        print("| Pacotes recebidos: ",n - pacotesPerdidos ,'                    |')
        print("| Pacotes perdidos:  ",pacotesPerdidos ,'           |')
        print("| Media de RTT:      ",round(RTT.mean(),2) ,' microssegundos   |')
        print("| Minimo de RTT:     ",RTT.min() ,'  microssegundos |')
        print("| Maximo de RTT:     ",RTT.max() ,'  microssegundos  |')
        print("| ----------------------------------------- |\n")
    else:
        print("|         Nenhum pacote retornado -         |")
        print("| ----------------------------------------- |\n")
