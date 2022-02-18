
class Lexer:
    def __init__(self,path) -> None:
        self.__init__()
        self.file = open(path,"r")
        self.currow = 0
        self.curcol = 0
    
    def nextch(self): 
        return self.file.read(1)

    def seekprev(self):
        ptel = self.file.tell() - 1 
        self.file.seek(ptel,0)

    def seeknext(self):
        return self.nextch()
    
    def eof(self):
        tok = self.follow()
        return tok == None

    def next():
        pass
    def follow():
        pass
    
class LexerGrud(Lexer):
    def next():
        pass
    def follow():
        pass
    
    