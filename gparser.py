from typing import List
from gtree import GrudTree
from lexer import Lexer, LexerGrud
from error import ErrorHandler
import gast as AST
class Parser:
    def __init__(self,lexer:Lexer) -> None:
        self.lex = lexer
        self.err = ErrorHandler()

    def parse(self):
        pass

class ParserGrud( Parser ):
    def __init__(self, lexer: LexerGrud) -> None:
        super().__init__(lexer)
        self.lex = lexer
        self.curkey = None
        self.gtree = dict()
         
    def parse(self):
        self.grud()
        return self.gtree
    
    def grud(self):
        if self.lex.eof():
            return

        self.stmt()
        self.grud()

    def stmt(self):
        tlist = self.lex.nextlinear()
        
        tlist = ParserGrud.ignorecomment(tlist)

        if len(tlist) == 0:
            return

        t = tlist[0]

        if t[0] == "%":
            self.title(t)
        else:
            self.keyvalue(tlist)

    def title(self,t):

        if t[-1] != "%":
            self.err.syntaxerr("title must closed by %")
        
        self.curkey = t[1:-1]

        if self.curkey == '':
            self.err.syntaxerr("title length must be more than zero %")
            return        
        
        if not self.gtree.get(self.curkey):
            self.gtree[self.curkey] = GrudTree()

    def keyvalue(self,tlist : list):
        root: GrudTree = self.gtree[self.curkey]
        key = str(tlist[0])
        values = tlist[1:]
        root.put(key,values)

    def ignorecomment(line : List[str]):
        newline = []

        for token in line:
            if token[0] == "#":
                break
            newline.append(token)
        
        return newline