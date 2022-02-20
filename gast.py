from typing import Any
import uuid

class AST:
    def __init__(self,id) -> None:
        self.parent = None
        self.id = id
        self.children = []
        self.val = {}
    
    def first(self):
        return self.children[0]
    
    def setparent(self,parent):
        self.parent = parent
    
    def addchild(self,child):
        self.children.append(child)

    def setval(self,key:str,val:Any):
        self.val[key] = val
    
    def getval(self,key:str):
        return self.val.get(key)

class ASTKeyPair( AST ):
    def __init__(self,key:str) -> None:
        super().__init__(uuid.uuid4())
        self.key = key
    
class ASTVaulePair ( AST ):
    def __init__(self,value) -> None:
        super().__init__(uuid.uuid4())
        self.value = value

    def setidx(self,index):
        self.setval("index",index)

    def getidx(self):
        return self.getval("index")

    def setbuildidx(self,buildidx):
        self.setval("build:index",buildidx)

    def getbuildidx(self):
        return self.getval("build:index")
