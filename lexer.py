
class Lexer:
    def __init__(self,path) -> None:
        self.__init__()
        self.file = open(path,"r")
        self.currow = 0
        self.curcol = 0
    
    def nextch(self): 
        c = self.file.read(1)
        
        if c == '\n':
            self.curcol = 0 
            self.currow += 1
        else:
            self.curcol += 1

        return c

    def seekprev(self):
        ptel = self.file.tell() - 1
        if ptel > -1:
            self.file.seek(ptel,0)
            c = self.file.read(1)
            if c == '\n':
                self.currow -= 1
            

        self.file.seek(ptel,0)

    def seeknext(self):
        return self.nextch()
    
    def eof(self):
        return self.follow() == None

    def endl(self,c):
        return c == '\n'
    def none(self,c):
        return c == ''
        
    def skipwspace(self):
        c = self.nextch()
        
        while c.isspace():
            c = self.nextch()

        self.seekprev()
    
    def tokseek(self,t:str):
        if t != '':
            t = t[:-1]
            self.seekprev()
        
        return t

    def next(self):
        pass
    def follow(self):
        saved = self.file.tell()
        t = self.next()
        self.file.seek(saved,0)
        return t

class LexerGrud(Lexer):
    def next(self):
        c = self.nextch()

        if c == '' or c == '\n':
            return c

        self.skipwspace()
        tok = self.block()
        
        return tok
    
    def skipwspace(self):
        c = self.nextch()
        
        while c.isspace():
            if self.endl(c):
                break
            c = self.nextch()

        self.seekprev()

    def block(self):
        c = self.nextch()
        t = ''
        while c.isspace():
            if self.endl(c) or self.none(c):
                break
            t += c
            c = self.nextch()
        
        t = self.tokseek(t)

        return t