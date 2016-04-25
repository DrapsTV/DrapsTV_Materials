
// code //
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number you wish to calculate.", type=int)

    args = parser.parse_args()
    
    result = fib(args.num)
    print "The " + str(args.num)+ "th fib number is " + str(result)

if __name__ == '__main__':
    Main()

//interation 2//
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number you wish to calculate.", type=int)
    parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")

    args = parser.parse_args()
    
    result = fib(args.num)
    print "The " + str(args.num)+ "th fib number is " + str(result)

    if args.output:
        f = open("fibonacci.txt","a")
        f.write(str(result) + '\n')

if __name__ == '__main__':
    Main()


//iteration 3//
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("num", help="The Fibonacci number you wish to calculate.", type=int)
    parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")

    args = parser.parse_args()
    
    result = fib(args.num)
    if args.verbose:
        print "The " + str(args.num)+ "th fib number is " + str(result)
    elif args.quiet:
        print result
    else:
        print "Fib("+str(args.num)+") = " + str(result)

    if args.output:
        f = open("fibonacci.txt","a")
        f.write(str(result) + '\n')

if __name__ == '__main__':
    Main()