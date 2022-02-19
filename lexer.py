
class Lexer:
    def __init__(self,path) -> None:
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
        return self.follow() == ''

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
            # t = t[:-1]
            self.seekprev()
        
        return t

    def escapeater(self,token:str):
        c = 0
        size = len(token)
        eattok = '' 
        while c < size:   
            eattok += token[c]
            
            if token[c] == '\\':
                c +=1
            
            c += 1

        print(eattok)

        return eattok

    def next(self):
        pass
    def follow(self):
        saved = self.file.tell()
        t = self.next()
        self.file.seek(saved,0)
        return t
    
class LexerGrud(Lexer):
    def nextlinear(self):
        line = list()
        while True:
            t = self.next()
            
            if self.none(t):
                break

            if self.endl(t):
                if len(line) == 0 :
                    continue
                else:
                    break
            
            line.append(t)
        
        return line

    def next(self):
        c = self.nextch()
        
        if c == '' or self.endl(c):
            return c

        self.seekprev()
        self.skipwspace()

        tok = self.block()

        # return self.escapeater(tok)
        return tok

    def skipwspace(self):
        c = self.nextch()
        
        while c.isspace():
            if self.endl(c):
                self.seekprev()
                break
            c = self.nextch()

        self.seekprev()

    def block(self):
        c = self.nextch()
        t = ''
        while not c.isspace():
            if self.none(c) or self.endl(c):
                break
            t += c
            c = self.nextch()
        
        if self.endl(c):
            self.seekprev()

        return t