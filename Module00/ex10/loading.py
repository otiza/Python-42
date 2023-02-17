import time
import datetime
import sys
from time import sleep

def ft_progress(lst):
    total = len(lst)

    t0 = time.time()
    t = t0
    for i in range(0,total):
        p = round(i * 100 / total)
        n = round (i * 20 / total)
        tmp = t
        t = time.time() - t0
        if t - tmp < 0:
            eta = 0
        else:
            eta = (t - tmp) * (total - i - 1)
        printable = ">"
        printable = printable.rjust(n,'=')
        printable = printable.ljust(20,' ')
        print("[{anim}]".format(anim=printable))
        
        yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)