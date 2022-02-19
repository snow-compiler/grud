from typing import Any
import uuid

class AST:
    def __init__(self,id) -> None:
        self.parent = None
        self.id = id
        self.children = []
        self.value = {}
    
    def first(self):
        return self.children[0]
    
    def setparent(self,parent):
        self.parent = parent
    
    def addchild(self,child):
        self.children.append(child)

    def setval(self,key:str,val:Any):
        self.value[key] = val
    
    def getval(self,key:str):
        return self.value.get(key)

class ASTKeyPair( AST ):
    def __init__(self,key:str) -> None:
        super().__init__(uuid.uuid4())
        self.key = key
    
class ASTVaulePair ( AST ):
    def __init__(self,value) -> None:
        super().__init__(uuid.uuid4())
        self.value = value