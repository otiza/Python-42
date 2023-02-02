import sys
from string import punctuation

def main(n): 
    s = sys.argv[1].translate(str.maketrans('', '', punctuation))
    print([x for x in s.split() if len(x) > n])

if __name__ == "__main__":
    if len(sys.argv )!= 3:
        sys.exit()
    try: 
        n =  int(sys.argv[2])
    except:
        sys.exit()
    
    main(n)



