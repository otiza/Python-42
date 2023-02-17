import random

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    '''
    if not isinstance(text, str):
        return "ERROR"
    ret = text.split(sep)
    if option == None:
        for i in ret:
            yield i
    elif option == "shuffle":
        random.shuffle(ret)
        for i in ret:
            yield i
    elif option == "unique":
        ret2 = list(dict.fromkeys(ret))
        for i in ret2:
            yield i
    elif option == "sorted":
        ret.sort(key=str.lower)
        for i in ret:
            yield i
    else :
        return "ERROR"


    
