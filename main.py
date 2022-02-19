
from posixpath import abspath
from gast import ASTKeyPair, ASTVaulePair
from gtree import GrudTree
from lexer import LexerGrud
from gparser import ParserGrud

path = abspath("./test/tslang.grud")
lex = LexerGrud(path)
parser = ParserGrud(lex)
gtree = parser.parse()

for key in gtree:
    g3 : GrudTree = gtree[key]
    GrudTree.print(g3.tbl,key)
