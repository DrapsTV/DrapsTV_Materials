
//code 1//

//SERVER//

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()


//CLIENT//

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = raw_input("-> ")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print 'Received from server: ' + str(data)
        message = raw_input("-> ")
    s.close()

if __name__ == '__main__':
    Main()


//code 2//

//SERVER//

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))


    print "Server Started."
    while True:
        data, addr = s.recvfrom(1024)
        print "message From: " + str(addr)
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        s.sendto(data, addr)
    c.close()

if __name__ == '__main__':
    Main()
    


//CLIENT//    

import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1',5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = raw_input("-> ")
    while message != 'q':
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        print 'Received from server: ' + str(data)
        message = raw_input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
