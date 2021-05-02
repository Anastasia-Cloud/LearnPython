#система непересекающихся множеств
#источник: https://habr.com/ru/post/104772/

import random

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
  if x!=y:
    if random.randint(0,1):
      diction[x]=y
    else:
      diction[y]=x
  
makeSet(1)
makeSet(2)
makeSet(3)
makeSet(4)
makeSet(5)
print(findRoot(4))
print(diction)

unite(1,4)
unite(3,5)
unite(3,1)
unite(5,1)

print(diction)
