import sys

def Executor(A, B):
    print('Sum: ', A + B)
    print('Difference: ', A - B)
    print('Product: ',A * B)
    if(B == 0):
        print('Quotient: ', "ERROR (division by zero)")
        print('Remainder: ',' ERROR (modulo by zero)')
    else:
        print('Quotient: ', A / B)
        print('Remainder: ',A % B)
        


def main():
    if len(sys.argv) == 3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            Executor(a, b)
        except:
            print("Argument must be numbers")
            sys.exit
        
    elif len(sys.argv) == 1:
        print("Usage: python operations.py <number1> <number2>")
    else:
        print("ERROR")

if __name__ == "__main__":
    main()