class state:
  def __init__(self,j1,j2,j3,parent):
    self.j1=j1
    self.j2=j2
    self.j3=j3
    self.parent=None

  def s1rr(self):
    if self.j3==7:
     pass
    else:
     u=self.j2
     self.j2=self.j3
     self.j3=7-self.j3
     self.j1=u
     



  def s1rl(self):
    if self.j1==7:
     pass 
    else: 
     u=self.j2
     self.j2=self.j1
     self.j3=u
     self.j1=7-self.j1

  def s2rr(self):
    if self.j3==5:
     pass 
    else: 
     u=self.j2
     self.j2=self.j3
     self.j1=u
     self.j3=5-self.j3


  def s2rl(self):
     if self.j1==5:
      pass
     else: 
      u=self.j2
      self.j2=self.j1
      self.j3=u
      self.j1=5-self.j1
      
      

  
  
  
  def __eq__(self,other):
    if other==None:
      return False
    if other.j1==self.j1 and other.j2==self.j2 and other.j3==self.j3:  
      return True
    else:
      return False  

  def __hash__(self):
    return self.j1+self.j2+self.j3
  

  def __str__(self):
    return f'({self.j1},{self.j2},{self.j3})' 

def goaltest(node):
  if node.j1==1 or node.j2==1 or node.j3==1:
    return True
  else:
    return False

import copy

def bfs():
  initial=state(7,0,5,None)
  if goaltest(initial)==True:
    return initial
  frontier=[]
  frontier.append(initial)
  explored=set()

  while True:
    if len(frontier)==0:
      return state(-1,-1,-1,None)
    node=frontier.pop(0)
    explored.add(node)

    child1=copy.deepcopy(node)
    child1.s1rr()

    child2=copy.deepcopy(node)
    child2.s1rl()

    child3=copy.deepcopy(node)
    child3.s2rr()

    child4=copy.deepcopy(node)
    child4.s2rl()

    

    childlist=[child1,child2,child3,child4]

    for child in childlist:
      if (child not in frontier) and (child not in explored):
        child.parent=node
        if goaltest(child)==True:
          return child
        frontier.append(child)


x=bfs()
#print(x)

  
def printpath(x):
  sequence=[]
  while True:
    if x.parent==None:
      sequence.append(x)
      break 
    else: 
      sequence.append(x)
      x=x.parent
  return sequence

sequence=printpath(x)
sequence.reverse()
for node in sequence:
  print(node)