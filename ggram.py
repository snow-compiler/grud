from typing import  List, Tuple
from gast import ASTVaulePair as ASTVP,ASTKeyPair as ASTKP
from gtypes import BaseTable, TreeEnumType

class State:
    def __init__(self,key:ASTKP,buildidx:int) -> None:
        self.base_index = buildidx
        self.name = key

class Terminal:
    def __init__(self) -> None:
        pass

class StateTerminal( Terminal ):
    def __init__(self,tet:TreeEnumType,rule_index) -> None:
        self.tet = tet
        self.rule_index = rule_index

class TokenTerminal( Terminal ):
    def __init__(self,token) -> None:
        self.token = token

class Rule:
    def __init__(self,gnode : ASTVP,state : State) -> None:
        self.gnode = gnode
        self.state = state
        self.terminals = []

    def pushterm(self,terminal:Terminal):
        self.terminals.append(terminal)

    def setterms(self,terminals : List[Terminal]):
        self.terminals = terminals

class Grammar:
    def __init__(self,lrows:BaseTable,grows:BaseTable) -> None:
        self.lrows = lrows
        self.grows = grows
        self.rules : List[Rule] = []

    def init(self):
        self.initstates()

        for key,row in self.grows.values():
            print(key.key)
            for ast in row:
                print(ast.value)
            pass
    
    def initstates(self):
        idx = 0
        for key,row in self.grows.values():
            for vals in row:
                vals.setidx(idx)
                idx += 1
                print(vals.getidx(),vals.value)

    def findstate(self,token : str) -> Tuple[TreeEnumType,int]:
        pass
