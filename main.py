
import json
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
    print("[:: %s ::]" % key)
    for k in g3.tbl:
        if isinstance(k,ASTKeyPair):
            print(k.key)
        if isinstance(k,ASTVaulePair):
            print(k.value)
