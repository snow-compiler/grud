from anytree import Node, RenderTree
import gast as AST 

class GrudTree:
    def __init__(self) -> None:
        self.tbl = list()

    def initorget( self, tbl : list, keys : list ):
        node = None

        if len( keys ) == 0:
            return None

        k = str ( keys[ 0 ] )
       
        for i in range( 0, len(tbl) ):
            gnd = tbl[ i ]
            if isinstance( gnd, AST.ASTKeyPair ):
                if gnd.key == k:
                    node = gnd
                    break
        
        if not node:
            node = AST.ASTKeyPair( k )
            tbl.append( node )

        tbl = node.children

        ret = self.initorget( tbl, keys[1:] )
        
        if ret:
            return ret
        
        return node

    def put( self, key : str, value : list ):
        keys = key.split( ":" )
        if len( keys ) == 0:
            print( "error : key is empty." )
            return False

        node = self.initorget( self.tbl, keys )
        
        if node:
            val = AST.ASTVaulePair( value )
            node.children.append( val )
            return True
        
        return False

    def rm( self, key : str ):
        pass
    
    def get( self, key : str ):
        keys = key.split( ":" )
        
        node : AST.ASTKeyPair
        tbl = self.tbl

        for k in keys:
            if k.isnumeric():
                index  = int( k )
                if index < len( tbl ) - 1:
                    node = tbl[ k ]
                    continue
            i = 0
            while True:

                if len( tbl ) <= i:
                    return None

                node : AST.ASTKeyPair = tbl[ i ]
                if GrudTree.iskeyast( node, k ):
                        tbl = node.children
                        break

                i += 1
        return node

    def iskeyast( node : AST.ASTKeyPair, key:str ):
        return isinstance( node, AST.ASTKeyPair ) and node.key == key

    def anytree(tbl,parent=None):
        if not parent:
            parent = Node("root")
        
        for node in tbl:
            if isinstance( node, AST.ASTKeyPair ):
                chp = Node(node.key,parent)
                GrudTree.anytree(node.children,parent=chp)
            if isinstance( node, AST.ASTVaulePair ):
                Node(node.value,parent=parent)

        return parent

    def print(tbl : list,title=None):
        if title: 
            title = Node(title) 

        root = GrudTree.anytree(tbl,title)
        for pre, fill, node in RenderTree(root):
             print("%s%s" % (pre, node.name))
