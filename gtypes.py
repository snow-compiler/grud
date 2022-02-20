from enum import Enum
from typing import Dict, List, Tuple
from gast import ASTVaulePair as ASTVP , ASTKeyPair as ASTKP 

BaseRow   = Tuple[ASTKP,List[ASTVP]]
BaseTable = Dict[str,BaseRow]

class TreeEnumType(Enum):
    LEXER = 0,
    GRAMMAR = 1,
    AST = 2,