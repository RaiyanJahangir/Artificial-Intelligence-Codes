import numpy as np
import copy

class Node:

    #board variable which is  3x3 array
    def __init__(self,board=None):
        if board is None:
            self.board=np.array([[0,0,0],
            [0,0,0],[0,0,0]])
        else:
            self.board=board

    #make children from the current node
    def makeChildren(self,player):
        childrenNodeList=[]
        if(player==1):
            #at first the player checks where there are blanks
            blankPositions=np.where(self.board==0)
            # Then the player creates one child at a time, placing his/her number at that blank position
            blankPositionIs=blankPositions[0]
            blankPositionJs=blankPositions[1]

            for k in range(len(blankPositionIs)):
                i=blankPositionIs[k]
                j=blankPositionJs[k]
                child=copy.deepcopy(self)
                child.board[i][j]=1

                childrenNodeList.append(child)

        elif(player==2):
            #at first the player checks where there are blanks
            blankPositions=np.where(self.board==0)
            # Then the player creates one child at a time, placing his/her number at that blank position
            blankPositionIs=blankPositions[0]
            blankPositionJs=blankPositions[1]

            for k in range(len(blankPositionIs)):
                i=blankPositionIs[k]
                j=blankPositionJs[k]
                child=copy.deepcopy(self)
                child.board[i][j]=2

                childrenNodeList.append(child)

        return childrenNodeList
    
    #print the state of the board
    def printBoard(self):
      print("*********************")
      print(self.board)
      print("*********************")

    def terminalTest(self):
      #Game has ended and player 1 is the winner
      if(self.board[0][0]==1 and self.board[0][1]==1 and self.board[0][2]==1):
        return True
      elif(self.board[1][0]==1 and self.board[1][1]==1 and self.board[1][2]==1):
        return True
      elif(self.board[2][0]==1 and self.board[2][1]==1 and self.board[2][2]==1):
        return True
      elif(self.board[0][0]==1 and self.board[1][0]==1 and self.board[2][0]==1):
        return True
      elif(self.board[0][1]==1 and self.board[1][1]==1 and self.board[2][1]==1):
        return True
      elif(self.board[0][2]==1 and self.board[1][2]==1 and self.board[2][2]==1):
        return True
      elif(self.board[0][0]==1 and self.board[1][1]==1 and self.board[2][2]==1):
        return True
      elif(self.board[0][2]==1 and self.board[1][1]==1 and self.board[2][0]==1):
        return True

      #Game has ended and player 2 is the winner
      if(self.board[0][0]==2 and self.board[0][1]==2 and self.board[0][2]==2):
        return True
      elif(self.board[1][0]==2 and self.board[1][1]==2 and self.board[1][2]==2):
        return True
      elif(self.board[2][0]==2 and self.board[2][1]==2 and self.board[2][2]==2):
        return True
      elif(self.board[0][0]==2 and self.board[1][0]==2 and self.board[2][0]==2):
        return True
      elif(self.board[0][1]==2 and self.board[1][1]==2 and self.board[2][1]==2):
        return True
      elif(self.board[0][2]==2 and self.board[1][2]==2 and self.board[2][2]==2):
        return True
      elif(self.board[0][0]==2 and self.board[1][1]==2 and self.board[2][2]==2):
        return True
      elif(self.board[0][2]==2 and self.board[1][1]==2 and self.board[2][0]==2):
        return True

      #game has ended its a draw
      blankPositions=np.where(self.board==0)
      #checking the number of blank positions
      blankPositionIs=blankPositions[0]
      blankPositionJs=blankPositions[1]
      if(len(blankPositionIs)==0):
        return True #draw

      #game is still going on
      return False

    def utility(self):
          
          # Game has ended and player 1 is the winner
          if(self.board[0][0]==1 and self.board[0][1]==1 and self.board[0][2]==1):
              return 100          
          elif(self.board[1][0]==1 and self.board[1][1]==1 and self.board[1][2]==1):
              return 100
          elif(self.board[2][0]==1 and self.board[2][1]==1 and self.board[2][2]==1):
              return 100

          elif(self.board[0][0]==1 and self.board[1][0]==1 and self.board[2][0]==1):
              return 100          
          elif(self.board[0][1]==1 and self.board[1][1]==1 and self.board[2][1]==1):
              return 100
          elif(self.board[0][2]==1 and self.board[1][2]==1 and self.board[2][2]==1):
              return 100

          elif(self.board[0][0]==1 and self.board[1][1]==1 and self.board[2][2]==1):
              return 100
          elif(self.board[0][2]==1 and self.board[1][1]==1 and self.board[2][0]==1):
              return 100                  

          # Player 1 has high chance of winning
          if (self.board[0][0]==1 and self.board[0][1]==1 and self.board[0][2]==0) or (self.board[0][0]==0 and self.board[0][1]==1 and self.board[0][2]==1):
              return 10            
          elif(self.board[1][0]==1 and self.board[1][1]==1 and self.board[1][2]==0) or (self.board[1][0]==0 and self.board[1][1]==1 and self.board[1][2]==1):
              return 10
          elif(self.board[2][0]==1 and self.board[2][1]==1 and self.board[2][2]==0) or (self.board[2][0]==0 and self.board[2][1]==1 and self.board[2][2]==1):
              return 10

          elif(self.board[0][0]==1 and self.board[1][0]==1 and self.board[2][0]==0) or (self.board[0][0]==0 and self.board[1][0]==1 and self.board[2][0]==1):
              return 10          
          elif(self.board[0][1]==1 and self.board[1][1]==1 and self.board[2][1]==0) or (self.board[0][1]==0 and self.board[1][1]==1 and self.board[2][1]==1):
              return 10
          elif(self.board[0][2]==1 and self.board[1][2]==1 and self.board[2][2]==0) or (self.board[0][2]==0 and self.board[1][2]==1 and self.board[2][2]==1):
              return 10

          elif(self.board[0][0]==1 and self.board[1][1]==1 and self.board[2][2]==0) or (self.board[0][0]==0 and self.board[1][1]==1 and self.board[2][2]==1):
              return 10
          elif(self.board[0][2]==1 and self.board[1][1]==1 and self.board[2][0]==0) or (self.board[0][2]==0 and self.board[1][1]==1 and self.board[2][0]==1):
              return 10

          # Player 1 is not doing so good
          if (self.board[0][0]==1 and self.board[0][1]==0 and self.board[0][2]==0) or (self.board[0][0]==0 and self.board[0][1]==1 and self.board[0][2]==0) or (self.board[0][0]==0 and self.board[0][1]==0 and self.board[0][2]==1):
              return 1            
          elif(self.board[1][0]==1 and self.board[1][1]==0 and self.board[1][2]==0) or (self.board[1][0]==0 and self.board[1][1]==1 and self.board[1][2]==0) or (self.board[1][0]==0 and self.board[1][1]==0 and self.board[1][2]==1):
              return 1
          elif(self.board[2][0]==1 and self.board[2][1]==0 and self.board[2][2]==0) or (self.board[2][0]==0 and self.board[2][1]==1 and self.board[2][2]==0) or (self.board[2][0]==0 and self.board[2][1]==0 and self.board[2][2]==1):
              return 1

          elif(self.board[0][0]==1 and self.board[1][0]==0 and self.board[2][0]==0) or (self.board[0][0]==0 and self.board[1][0]==1 and self.board[2][0]==0) or (self.board[0][0]==0 and self.board[1][0]==0 and self.board[2][0]==1):
              return 1          
          elif(self.board[0][1]==1 and self.board[1][1]==0 and self.board[2][1]==0) or (self.board[0][1]==0 and self.board[1][1]==1 and self.board[2][1]==0) or (self.board[0][1]==0 and self.board[1][1]==0 and self.board[2][1]==1):
              return 1
          elif(self.board[0][2]==1 and self.board[1][2]==0 and self.board[2][2]==0) or (self.board[0][2]==0 and self.board[1][2]==1 and self.board[2][2]==0) or (self.board[0][2]==0 and self.board[1][2]==0 and self.board[2][2]==1):
              return 1

          elif(self.board[0][0]==1 and self.board[1][1]==0 and self.board[2][2]==0) or (self.board[0][0]==0 and self.board[1][1]==1 and self.board[2][2]==0) or (self.board[0][0]==0 and self.board[1][1]==0 and self.board[2][2]==1):
              return 1
          elif(self.board[0][2]==1 and self.board[1][1]==0 and self.board[2][0]==0) or (self.board[0][2]==0 and self.board[1][1]==1 and self.board[2][0]==0) or (self.board[0][2]==0 and self.board[1][1]==0 and self.board[2][0]==1):
              return 1
          
          return 0


    def checkWinner(self):
          
          # Game has ended and player 1 is the winner
          if(self.board[0][0]==1 and self.board[0][1]==1 and self.board[0][2]==1):
              return 1          
          elif(self.board[1][0]==1 and self.board[1][1]==1 and self.board[1][2]==1):
              return 1
          elif(self.board[2][0]==1 and self.board[2][1]==1 and self.board[2][2]==1):
              return 1

          elif(self.board[0][0]==1 and self.board[1][0]==1 and self.board[2][0]==1):
              return 1          
          elif(self.board[0][1]==1 and self.board[1][1]==1 and self.board[2][1]==1):
              return 1
          elif(self.board[0][2]==1 and self.board[1][2]==1 and self.board[2][2]==1):
              return 1

          elif(self.board[0][0]==1 and self.board[1][1]==1 and self.board[2][2]==1):
              return 1
          elif(self.board[0][2]==1 and self.board[1][1]==1 and self.board[2][0]==1):
              return 1                  


          # Game has ended and player 2 is the winner
          if(self.board[0][0]==2 and self.board[0][1]==2 and self.board[0][2]==2):
              return 2          
          elif(self.board[1][0]==2 and self.board[1][1]==2 and self.board[1][2]==2):
              return 2
          elif(self.board[2][0]==2 and self.board[2][1]==2 and self.board[2][2]==2):
              return 2

          elif(self.board[0][0]==2 and self.board[1][0]==2 and self.board[2][0]==2):
              return 2          
          elif(self.board[0][1]==2 and self.board[1][1]==2 and self.board[2][1]==2):
              return 2
          elif(self.board[0][2]==2 and self.board[1][2]==2 and self.board[2][2]==2):
              return 2

          elif(self.board[0][0]==2 and self.board[1][1]==2 and self.board[2][2]==2):
              return 2
          elif(self.board[0][2]==2 and self.board[1][1]==2 and self.board[2][0]==2):
              return 2                  

          # Game has ended and its a draw
          blankPositions=np.where(self.board==0)
          # Checking the number of blank positions
          blankPositionIs=blankPositions[0]
          blankPositionJs=blankPositions[1]
          if(len(blankPositionIs)==0):
              return 0 # draw
          
          # Game is still going on
          return None

# # unit testing a node and its child generation
# testBoard=np.array([[1,0,0],
#             [0,2,0],
#             [0,0,0]])
# testNode=Node(testBoard)
# childrenList=testNode.makeChildren(2)
# for child in childrenList:
#     child.printBoard()

# # unit testing a node and its child generation :DRAW
# testBoard=np.array([[1,2,1],
#                     [2,1,2],
#                     [2,1,2]])
# testNode=Node(testBoard)
# print(testNode.terminalTest())
# print(testNode.utility())

# # unit testing a node and its child generation : PLAYER 1
# testBoard=np.array([[1,1,1],
#                     [2,1,0],
#                     [2,0,2]])
# testNode=Node(testBoard)
# print(testNode.terminalTest())
# print(testNode.utility())

# # unit testing a node and its child generation : PLAYER 2
# testBoard=np.array([[2,1,1],
#                     [2,1,0],
#                     [2,0,2]])
# testNode=Node(testBoard)
# print(testNode.terminalTest())
# print(testNode.utility())

# # unit testing a node and its child generation : PLAYER 2
# testBoard=np.array([[2,1,1],
#                     [0,1,0],
#                     [2,0,2]])
# testNode=Node(testBoard)
# print(testNode.terminalTest())
# print(testNode.utility())

def alpha_beta_search(node):
    alpha=-99999
    beta =+99999

    if(node.terminalTest()):
        return node.utility() 
    
    v=-99999
    childrenList=node.makeChildren(1)
    childValues=[]
    for child in childrenList:        
        valueFromChild=min_node_function(child,alpha,beta)
        childValues.append(valueFromChild)
        
        v=max(v,valueFromChild)      
        alpha=max(alpha,v)        
    
    return childrenList,childValues

def max_node_function(node,alpha,beta):    
    if(node.terminalTest()):
        return node.utility() 
    
    v=-99999
    childrenList=node.makeChildren(1)
    for child in childrenList:
        valueFromChild=min_node_function(child,alpha,beta)
        v=max(v,valueFromChild)
        
        # if(firstNode==True):
        #     print(v)
        #     child.printBoard()
        
        if(v>=beta):
            return v
        
        alpha=max(alpha,v)    

    return v
    

def min_node_function(node,alpha,beta):
    if(node.terminalTest()):
        return node.utility()    
    
    v=+99999    
    childrenList=node.makeChildren(2)
    for child in childrenList:
        valueFromChild=max_node_function(child,alpha,beta)
        v=min(v,valueFromChild)
        
        if(v<=alpha):
            return v
        
        beta=min(beta,v)    

    return v

# testBoard=np.array([[0,0,0],
#                     [0,0,0],
#                     [0,0,0]])
# testNode=Node(testBoard)
# children,values=alpha_beta_search(testNode)



# maxValue = max(values)
# maxChildIndex = values.index(maxValue)
# #print(values)
# children[maxChildIndex].printBoard()

playBoard=np.array([[0,0,0],
                    [0,0,0],
                    [0,0,0]])
playNode=Node(playBoard)



#print(values)
#children[maxChildIndex].printBoard()

while True:
     vals=alpha_beta_search(playNode)
     #print(vals)
     #print('vals')
     children,values=vals

     maxValue = max(values)
     maxChildIndex = values.index(maxValue)
     print('Computer has played, board condition:')
     children[maxChildIndex].printBoard()
     playNode=children[maxChildIndex]
     
     if(playNode.checkWinner()==1):
        print('AI agent is the winner')
        break
     
     if(playNode.checkWinner()==0):
        print('Draw')
        break

     
     x=input('Enter x:')
     y=input('Enter y:')

     print('You have played, board condition:')
     playNode.board[int(x)][int(y)]=2
     playNode.printBoard()  

     if(playNode.checkWinner()==2):
        print('You are the winner')
        break
     if(playNode.checkWinner()==0):
        print('Draw')
        break