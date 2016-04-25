
//code 1//

//SERVER//

import socket
import time

host = '127.0.0.1'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print "Server Started."
while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
            
        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()


//CLIENT//

import socket
import threading

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = raw_input("Name: ")
message = raw_input(alias + "-> ")
while message != 'q':
    if message != '':
        s.sendto(alias + ": " + message, server)
    tLock.acquire()
    message = raw_input(alias + "-> ")
    tLock.release()
    time.sleep(0.2)

shudown = True
rT.join()
s.close()
