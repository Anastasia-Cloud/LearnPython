#система непересекающихся множеств
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
  pass

