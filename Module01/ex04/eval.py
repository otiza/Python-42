

class Evaluator():
    
    def zip_evaluate(words, coffs):
        if not isinstance(words,list) and not isinstance(coffs,list):
            raise TypeError("Must be lists")
        if not len(words) == len(coffs):
            raise ValueError("Must be same length")
        zipped = zip(words,coffs)
        ret = 0
        for i in zipped:
            ret += len(i[0]) * i[1]
        print(ret)
    
    def enumerate_evaluate(words, coffs):
        if not isinstance(words,list) and not isinstance(coffs,list):
            raise TypeError("Must be lists")
        if not len(words) == len(coffs):
            raise ValueError("Must be same length")
        ret = 0
        for i , coff in enumerate(coffs):
            ret+= coff * len(words[i])
        print(ret)

