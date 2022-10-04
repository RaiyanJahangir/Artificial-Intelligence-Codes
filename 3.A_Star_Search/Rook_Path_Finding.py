import numpy as np
import time

# Heuristic = Rook moves distance
costblock=[[2,2,2,2,2,2,2,1],
[3,10000,10000,10000,10000,2,2,1],
[3,10000,5,5,10000,3,10000,1],
[3,10000,5,5,10000,3,10000,0],
[3,10000,5,5,10000,3,10000,1],
[3,10000,4,4,4,3,10000,1],
[3,10000,10000,10000,10000,10000,10000,1],
[2,2,2,2,2,2,2,1]]

class Node:

    def __init__(self,chessboard):
        self.parent=None
        self.g=0
        self.chessboard=chessboard
        self.chessboard=np.array(self.chessboard)

    def moveUp(self,pos):
        rookPos=np.where(self.chessboard=='O')
        rookPosR,rookPosC=rookPos
        if(rookPosR-pos<0):
            return
        otherPosR=rookPosR-pos
        otherPosC=rookPosC    
        self.chessboard[rookPosR,rookPosC]='_'
        self.chessboard[otherPosR,otherPosC]='O'

    def moveDown(self,pos):
        rookPos=np.where(self.chessboard=='O')
        rookPosR,rookPosC=rookPos
        if(rookPosR+pos>7):
            return
        otherPosR=rookPosR+pos
        otherPosC=rookPosC    
        self.chessboard[rookPosR,rookPosC]='_'
        self.chessboard[otherPosR,otherPosC]='O'

    def moveLeft(self,pos):
        rookPos=np.where(self.chessboard=='O')
        rookPosR,rookPosC=rookPos
        if(rookPosC-pos<0):
            return
        otherPosR=rookPosR
        otherPosC=rookPosC-pos 
        self.chessboard[rookPosR,rookPosC]='_'
        self.chessboard[otherPosR,otherPosC]='O'

    def moveRight(self,pos):
        rookPos=np.where(self.chessboard=='O')
        rookPosR,rookPosC=rookPos
        if(rookPosC+pos>7):
            return
        otherPosR=rookPosR
        otherPosC=rookPosC+pos 
        self.chessboard[rookPosR,rookPosC]='_'
        self.chessboard[otherPosR,otherPosC]='O'

    #overriding the functions for comparison
    def __hash__(self):
        rookPos=np.where(self.chessboard=='O')
        rookPosR,rookPosC=rookPos
        return int(rookPosR[0]*rookPosC[0])

    def __eq__(self,other):
        if(other==None):
            return False
        
        equal=True        
        for i in range(8):
            for j in range(8):
                if(self.chessboard[i][j]==other.chessboard[i][j]):  
                    continue
                else:
                    equal=False
                    break
        return equal

    def display(self):
        print('*************************')
        for i in range (8):
            for j in range (8):
                print(f'({self.chessboard[i,j]})',end='')
            print('')
        print('*************************')


def h1(node):
    rookPos=np.where(node.chessboard=='O')
    rookPosR,rookPosC=rookPos
    return costblock[rookPosR[0]][rookPosC[0]]

def evaluationFunc(node):
  return node.g+h1(node)

def goalTest(node):
    goalPuzzleBox=[['_','_','_','_','_','_','_','_'],
['_','X','X','X','X','_','_','_'],
['_','X','_','_','X','_','X','_'],
['_','X','_','_','X','_','X','O'],
['_','X','_','_','X','_','X','_'],
['_','X','_','_','_','_','X','_'],
['_','X','X','X','X','X','X','_'],
['_','_','_','_','_','_','_','_']]
    goalPuzzleBox=np.array(goalPuzzleBox)
    if(np.array_equal(goalPuzzleBox,node.chessboard)):
        return True
    else:
        return False
     
import copy

def RookPathFind():
    initialNode=Node(chessboard=[['_','_','_','_','_','_','_','_'],
['_','X','X','X','X','_','_','_'],
['_','X','_','_','X','_','X','_'],
['_','X','O','_','X','_','X','D'],
['_','X','_','_','X','_','X','_'],
['_','X','_','_','_','_','X','_'],
['_','X','X','X','X','X','X','_'],
['_','_','_','_','_','_','_','_']])

    frontier=[]
    frontier.append(initialNode)
  
    explored= set()

    while(True):      
      # If frontier is empty then return failure
      if(len(frontier)==0):
          return  None
      frontier.sort(key=evaluationFunc)
      node=frontier.pop(0)
      if goalTest(node)==True :
          return node     
      
      #adding the node to explored set
      explored.add(node)

      child1=[]
      rookPos=np.where(node.chessboard=='O')
      rookPosR,rookPosC=rookPos
      i=1
      while(rookPosR[0]-i>0):
          curPosR=rookPosR-i
          if costblock[curPosR[0]][rookPosC[0]]==10000:
              break
          
        # for each action in up direction available we are now generating child
          child=copy.deepcopy(node)
          child.moveUp(i)
          child.g=child.g+1
          child1.append(child)
          i=i+1

      child2=[]
      rookPos=np.where(node.chessboard=='O')
      rookPosR,rookPosC=rookPos
      i=1
      while(rookPosR[0]+i<8):
          curPosR=rookPosR+i
          if costblock[curPosR[0]][rookPosC[0]]==10000:
              break
          
        # for each action in down direction available we are now generating child
          child=copy.deepcopy(node)
          child.moveDown(i)
          child.g=child.g+1
          child2.append(child)
          i=i+1

      child3=[]
      rookPos=np.where(node.chessboard=='O')
      rookPosR,rookPosC=rookPos
      i=1
      while(rookPosC[0]-i>0):
          curPosC=rookPosC-i
          if costblock[rookPosR[0]][curPosC[0]]==10000:
              break
          
        # for each action in left direction available we are now generating child
          child=copy.deepcopy(node)
          child.moveLeft(i)
          child.g=child.g+1
          child3.append(child)
          i=i+1

      child4=[]
      rookPos=np.where(node.chessboard=='O')
      rookPosR,rookPosC=rookPos
      i=1
      while(rookPosC[0]+i<8):
          curPosC=rookPosC+i
          if costblock[rookPosR[0]][curPosC[0]]==10000:
              break
          
        # for each action available in right direction we are now generating child
          child=copy.deepcopy(node)
          child.moveRight(i)
          child.g=child.g+1
          child4.append(child)
          i=i+1

      child1=np.array(child1)
      child2=np.array(child2)
      child3=np.array(child3)
      child4=np.array(child4)
      childList=np.concatenate((child1,child2,child3,child4))


      for iterator in childList:
          if(iterator not in frontier and iterator not in explored):
              iterator.parent=node              
              frontier.append(iterator)            
          elif(iterator in frontier):
              index=frontier.index(iterator)
              inFrontierNode=frontier[index]
              if(h1(iterator)+iterator.g<h1(inFrontierNode)+inFrontierNode.g):
                  frontier[index]=iterator

start_time = time.time()
x=RookPathFind()

def printPath(node):
    if(node==None):
        return
    printPath(node.parent)
    node.display()

printPath(x)
print("Process finished --- %s seconds ---" % (time.time() - start_time))

      