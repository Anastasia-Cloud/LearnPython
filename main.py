#система непересекающихся множеств
from random import random
diction={}
def makeSet(x): #добавление множества 
  diction[x]=x

def findRoot(x):
  if diction[x]==x:
    return x
  else:
    diction[x]=findRoot(diction[x])
    return diction[x]

def unite(x,y):
  x=findRoot(x)
  y=findRoot(y)
  if random.randint(0,1):
    diction[x]=y
  else:
    diction[y]=x
  

