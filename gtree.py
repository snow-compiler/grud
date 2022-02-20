from io import TextIOWrapper
from typing import Dict, List
from anytree import Node, RenderTree
from gast import AST,ASTVaulePair as ASTVP , ASTKeyPair as ASTKP
from gtypes import BaseRow, BaseTable 


class GrudTree:
    def __init__(self) -> None:
        self.tbl = list()
        self.curidx = 0

    def initorget( self, tbl : list, keys : list , keyall  : str = "" ):
        node = None

        if len( keys ) == 0:
            return None

        k = str ( keys[ 0 ] )
        for i in range( 0, len(tbl) ):
            gnd = tbl[ i ]
            if isinstance( gnd, ASTKP ):
                if gnd.key == k:
                    node = gnd
                    break
    
        if not node:
            node = ASTKP( k )
            tbl.append( node )

        tbl = node.children

        ret : AST = self.initorget( tbl, keys[1:] , keyall )

        if ret:
            ret.setparent( node )
            return ret
        
        return node

    def put( self, key : str, value : list ):
        keys = key.split( ":" )
        if len( keys ) == 0:
            print( "error : key is empty." )
            return False

        node = self.initorget( self.tbl, keys, key)
        
        if node:
            val = ASTVP( value )
            val.setparent( node )
            val.setbuildidx(self.curidx)
            self.curidx += 1
            node.children.append( val )
            return True
        
        return False

    def rm( self, key : str ):
        pass
    
    def get( self, key : str ):
        keys = key.split( ":" )
        
        node : ASTKP
        tbl = self.tbl

        for k in keys:
            i = 0
            while True:

                if len( tbl ) <= i:
                    return None

                node : ASTKP = tbl[ i ]
                if GrudTree.iskeyast( node, k ):
                        tbl = node.children
                        break

                i += 1
        return node

    def iskeyast( node : ASTKP, key:str ):
        return isinstance( node, ASTKP ) and node.key == key

    def anytree(tbl,parent=None):
        if not parent:
            parent = Node("root")
        
        for node in tbl:
            if isinstance( node, ASTKP ):
                chp = Node(node.key,parent)
                GrudTree.anytree(node.children,parent=chp)
            if isinstance( node, ASTVP ):
                bidx = node.getbuildidx()
                name = "(%s) %s" % (bidx,node.value)
                Node(name,parent=parent)

        return parent

    def print(tbl : list,title=None,f=None):
        if title: 
            title = Node(title) 

        root = GrudTree.anytree(tbl,title)
        for pre, fill, node in RenderTree(root):
            if f:
                f : TextIOWrapper = f
                s = "%s%s" % (pre, node.name)
                f.write("%s\n" % s.rstrip())
            else:
                print("%s%s" % (pre, node.name))

    def dfsvalues(tbl : List[AST]) -> List[ASTVP]:
        values : List[ASTVP] = []
        for node in tbl:
            if isinstance(node,ASTVP):
                values.append(node)
                continue

            if isinstance(node,ASTKP):
                stbl = GrudTree.dfsvalues(node.children)
                values.extend(stbl)

        return values
    
    def tobasebykey(self,key:str) -> BaseRow: 
        for base in self.tbl:
            if isinstance(base,ASTKP):
                if base.key == key:
                    vals = GrudTree.dfsvalues(base.children)
                    return (base,vals)
        return None

    def tobase(g3) -> BaseTable:
        rows : BaseTable = dict()
        
        for base in g3.tbl:
            if isinstance(base,ASTKP):
                vals = GrudTree.dfsvalues(base.children)
                rows[base.key] = (base,vals)

        return rows

    #babel sort
    def sortbykey(rows:List[BaseRow]) -> List[BaseRow]:
        return
        for i in range(0,len(rows)):
            for j in range(i + 1,len(rows)):
                lsb = rows[i][0].key.upper()
                msb = rows[j][0].key.upper()
                
                if lsb < msb:
                    tmp = rows[i]
                    rows[i] = rows[j]
                    rows[j] = tmp

