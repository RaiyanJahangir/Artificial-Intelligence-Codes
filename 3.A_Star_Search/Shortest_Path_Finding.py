import numpy as np

class Node:

    def __init__(self,puzzleBox):
        self.parent=None
        self.g=0
        self.puzzleBox=puzzleBox
        self.puzzleBox=np.array(self.puzzleBox)

    def moveUp(self):
        zeroPos=np.where(self.puzzleBox==0)
        zeroPosR,zeroPosC=zeroPos
        if(zeroPosR==0):
            return
        otherPosR=zeroPosR-1
        otherPosC=zeroPosC    
        self.puzzleBox[zeroPosR,zeroPosC]=self.puzzleBox[otherPosR,otherPosC]
        self.puzzleBox[otherPosR,otherPosC]=0

    
    def moveDown(self):
        zeroPos=np.where(self.puzzleBox==0)
        zeroPosR,zeroPosC=zeroPos
        if(zeroPosR==2):
            return
        otherPosR=zeroPosR+1
        otherPosC=zeroPosC    
        self.puzzleBox[zeroPosR,zeroPosC]=self.puzzleBox[otherPosR,otherPosC]
        self.puzzleBox[otherPosR,otherPosC]=0
    
    def moveLeft(self):
        zeroPos=np.where(self.puzzleBox==0)
        zeroPosR,zeroPosC=zeroPos
        if(zeroPosC==0):
            return
        otherPosR=zeroPosR
        otherPosC=zeroPosC-1    
        self.puzzleBox[zeroPosR,zeroPosC]=self.puzzleBox[otherPosR,otherPosC]
        self.puzzleBox[otherPosR,otherPosC]=0

    def moveRight(self):
        zeroPos=np.where(self.puzzleBox==0)
        zeroPosR,zeroPosC=zeroPos
        if(zeroPosC==2):
            return
        otherPosR=zeroPosR
        otherPosC=zeroPosC+1    
        self.puzzleBox[zeroPosR,zeroPosC]=self.puzzleBox[otherPosR,otherPosC]
        self.puzzleBox[otherPosR,otherPosC]=0


    
    #overriding the functions for comparison
    def __hash__(self):
        hash=0
        count=1
        for i in range(3):
            for j in range(3):
                hash=hash+count*self.puzzleBox[i][j]
                count=count+1
        return int(hash)

    def __eq__(self,other):
        if(other==None):
            return False
        
        equal=True        
        for i in range(3):
            for j in range(3):
                if(self.puzzleBox[i][j]==other.puzzleBox[i][j]):  
                    continue
                else:
                    equal=False
                    break
        return equal

    def display(self):
        print('*************************')
        for i in range (3):
            for j in range (3):
                print(f'({self.puzzleBox[i,j]})',end='')
            print('')
        print('*************************')

# node1=Node(puzzleBox=[[1,2,3],
#                       [4,5,6],
#                       [7,8,0]])
# node2=Node(puzzleBox=[[1,3,2],
#                       [4,0,5],
#                       [7,6,8]])
# node2.moveDown()
# node1.display()
# node2.display()

# node1=node2
# mySet=set()
# mySet.add(node1)
# mySet.add(node2)
# print(mySet)

def h1(node):
    goalPuzzleBox=[[0,1,2],       
                   [3,4,5],
                   [6,7,8]]
    goalPuzzleBox=np.array(goalPuzzleBox)
    currentPuzzleBox=node.puzzleBox
    totalDist=0
    for i in range(9):
      if (i==0):
        continue

      goalpos=np.where(goalPuzzleBox==i)
      curpos=np.where(currentPuzzleBox==i)

      goalR,goalC=goalpos[0],goalpos[1]
      curR,curC=curpos[0],curpos[1]
      
      tempdist=sum(abs(goalR-curR),abs(goalC-curC))
      totalDist=totalDist+tempdist
      
    return totalDist

# node=Node(
#     puzzleBox= [[7,2,4],       
#                 [5,0,6],
#                 [8,3,1]]
# )
# node.display()
# print(h1(node))

# node1=Node(puzzleBox= [[1,0,2],       
#                 [3,4,5],
#                 [6,7,8],])
# print(h1(node1))
# node2=Node(puzzleBox= [[0,7,2],       
#               [3,4,5],
#               [6,1,8],])
# print(h1(node2))
# node3=Node(puzzleBox= [[7,2,4],       
#                 [5,0,6],
#                 [8,3,1],])
# print(h1(node3))
# nodeList=[]

# nodeList.append(node3)
# nodeList.append(node1)
# nodeList.append(node2)

# for x in nodeList:
#   x.display()

def evaluationFunc(node):
  return node.g+h1(node)

# nodeList.sort(key = evaluationFunc)
# for x in nodeList:
#   x.display()

def goalTest(node):
    goalPuzzleBox=[[0,1,2],       
                [3,4,5],
                [6,7,8]]
    goalPuzzleBox=np.array(goalPuzzleBox)
    if(np.array_equal(goalPuzzleBox,node.puzzleBox)):
        return True
    else:
        return False

import copy

def aStarSearch():
  initialNode=Node(puzzleBox= [[1,2,3],       
                [0,4,6],
                [7,5,8],])
  #initialNode=Node()
  # if goalTest(initialNode)==True :
  #     return initialNode

  frontier=[] # a queue
  frontier.append(initialNode)
  
  explored= set()
  
  while(True):      
      # If frontier is empty then return failure
      if(len(frontier)==0):
          return  None
      #getting current node
      #frontier.sort(key=lambda n: n.g+ h1(n))
      frontier.sort(key=evaluationFunc)
      node=frontier.pop(0)
      if goalTest(node)==True :
          return node     
      
      #node.display()
      #adding the node to explored set
      explored.add(node)

      # for each action available we are now generating child
      child1=copy.deepcopy(node)
      child1.moveUp()
      child1.g=child1.g+1

      child2=copy.deepcopy(node)
      child2.moveDown()
      child2.g=child2.g+1

      child3=copy.deepcopy(node)
      child3.moveLeft()
      child3.g=child3.g+1

      child4=copy.deepcopy(node)
      child4.moveRight()
      child4.g=child4.g+1
     
                  
      childList=[child1,child2,child3,child4]
      
      for child in childList:
          if(child not in frontier and child not in explored):
              child.parent=node              
              frontier.append(child)            
          elif(child in frontier):
              index=frontier.index(child)
              inFrontierNode=frontier[index]
              if(h1(child)+child.g<h1(inFrontierNode)+inFrontierNode.g):
                  frontier[index]=child


x=aStarSearch()
print(x)

def printPath(node):
    if(node==None):
        return
    printPath(node.parent)
    node.display()

printPath(x)