class Symbols:
    def __init__(self) -> None:
        self.parent = None
    
    def put(self):
        pass
    
    def rm(self):
        pass
    
    def get(self):
        pass
    
    def find(self):
        pass
    
class GrudSymbols ( Symbols ):
    def __init__(self) -> None:
        super().__init__()
        self.list = []

    def put(self,key : str, value : str):
        pass
    
    def rm(self,key : str):
        pass
    
    def get(self,key : str):
        pass
    
    def find(self,key : str):
        pass