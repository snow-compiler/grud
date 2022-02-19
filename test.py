from posixpath import abspath
from glexer import LexerGrud
from gtree import GrudTree
from glexer import LexerGrud
from gparser import ParserGrud


def test_lexer():
    path = abspath("./test/tslang.grud")
    lex = LexerGrud(path)

    while True:
        token = lex.next()

        if not token:
            break
        print(token)
 
def test_lexer_linear():
    path = abspath("./test/tslang.grud")
    lex = LexerGrud(path)

    while True:
        if lex.eof():
            break

        tokl = lex.nextlinear()

        print(tokl)
 
def test_parser_tree():
    path = abspath("./test/tslang.grud")
    lex = LexerGrud(path)
    parser = ParserGrud(lex)
    gtree = parser.parse()

    for key in gtree:
        g3 : GrudTree = gtree[key]
        GrudTree.print(g3.tbl,key)
