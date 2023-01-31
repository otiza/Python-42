import sys

if len(sys.argv) == 1:
    print("usage: python3 exec.py [args...]")
else:
    tmp = " ".join(sys.argv[1:])
    ret = tmp[::-1].swapcase()
    print (ret)