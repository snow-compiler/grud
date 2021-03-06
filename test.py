from posixpath import abspath
from ggram import Grammar
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
 
def test_parser_tree(outlog = False):
    f = None
    if(outlog):
        f = open(abspath("./log/gtree"),"w+")

    path = abspath("./test/tslang.grud")
    lex = LexerGrud(path)
    parser = ParserGrud(lex)
    gtree = parser.parse()

    for key in gtree:
        g3 : GrudTree = gtree[key]
        print("[::%s::]" % key)
        GrudTree.print(g3.tbl,key,f)
        rows = GrudTree.tobase(g3)
        # GrudTree.sortbykey(rows)
        for key in rows:
            r = rows.get(key) 
            if r : 
                print(r[0].key,len(r[1]))

def test_grammar_initializer():
    
    path = abspath("./test/tslang.grud")
    lex = LexerGrud(path)
    parser = ParserGrud(lex)
    tree = parser.parse()
    lrows = GrudTree.tobase(tree["Grammar"])
    grows = GrudTree.tobase(tree["Grammar"])

    gram = Grammar(lrows,grows)
    gram.init()