from posixpath import abspath
from lexer import Lexer, LexerGrud

def test_lexer():
    path = abspath("./test/tslang.grud")
    lex = LexerGrud(path)

    while True:
        token = lex.next()

        if not token:
            break
        print({token})
 
