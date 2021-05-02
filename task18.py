#система непересекающихся множеств: задача 6.1

import random

diction={}
info={}
def makeSet(x): #добавление множества 
  diction[x]=x
  info[x]={'min':x,'count':1}

def findRoot(x):
  if diction[x]==x:
    return x
  else:
    diction[x]=findRoot(diction[x])
    return diction[x]

def unite(x,y):
  x=findRoot(x)
  y=findRoot(y)
  #print('x',info[x])
  #print('y',info[y])
  if x!=y:
    if random.randint(0,1):
      
      diction[x]=y 
      info[y]['min']=min(info[y]['min'],info[x]['min'])
      info[y]['count']+=info[x]['count']
      del info[x]
      return (info[y]['min'],info[y]['count'])
    else:
      diction[y]=x
      info[x]['min']=min(info[y]['min'],info[x]['min'])
      info[x]['count']+=info[y]['count']
      del info[y]
      return (info[x]['min'],info[x]['count'])
  return (0,0)

maxCount=1
minNode=1
for i in range(1,int(input())+1):
  makeSet(i)

for i in range(int(input())):
  x,y=[int(j) for j in input().split()]
  node,count=unite(x,y)
  if count>maxCount:
    maxCount=count
    minNode=node
  print(maxCount,minNode)
'''
Пример входа
4 
3
3 4
2 3
1 2
Пример выхода
2 3
3 2
4 1
'''