class ErrorHandler :
    def __init__(self) -> None:
        self.warningc = 0
        self.syntaxc = 0
        self.semanticc = 0

    def warning(self,msg):
        self.warningc += 1
        print("syntax error : ",msg)
     
    def syntaxerr(self,msg):
        self.syntaxerr += 1
        print("syntax error : ",msg)
    
    def semanticerr(self,msg):
        self.semanticc += 1
        print("syntax error : ",msg)
    
        
        