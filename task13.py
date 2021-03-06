#декартово дерево
from random import random
class DTree:

  def __init__(self,key,prior=random(),l=None,r=None):
    self.key=key
    self.prior=prior
    self.left=l
    self.right=r

  @staticmethod
  def Merge(lTree,rTree):
    if lTree is None:
      return rTree
    if rTree is None:
      return lTree
    if lTree.prior>rTree.prior:
      newTree=DTree.Merge(lTree.right,rTree)
      return DTree(lTree.key,lTree.prior,lTree.left,newTree)
    else:
      newTree=DTree.Merge(lTree,rTree.left)
      return DTree(rTree.key,rTree.prior,newTree,rTree.right)

  

  def Split(self,x):
    if self.key>x:
      if self.left is None:
        return (None,self)
      else:
        rTree=DTree(self.key,self.prior,None,self.right)
        lTree,rTree.left=self.left.Split(x)
        return (lTree,rTree)
    else:
      if self.right is None:
        return (self,None)
      else:
        lTree=DTree(self.key,self.prior,self.left,None)
        lTree.right,rTree=self.right.Split(x)
        return (lTree,rTree)

  def Add(self,key,p=random()):
    lTree,rTree=self.Split(key)
    newTree=DTree(key,p)

    '''print('left')
    DTree.showTree(lTree)
    print('right')
    DTree.showTree(rTree)
    print('new')
    DTree.showTree(newTree)'''

    #res=DTree.Merge(lTree,newTree)
    #print('...result')
    #res.show()
    res=DTree.Merge(DTree.Merge(lTree,newTree),rTree)
    #print('...........result')
    #res.show()
    return res

  def delete(self,key):
    l,r=self.Split(key-1)
    m,r=r.Split(key)
    return DTree.Merge(l,r)


  @staticmethod
  def showTree(tree):
    if tree is None:
      print('None')
    else:
      tree.show()

  def show(self):
    if self.left is not None:
      print('left child of ',self.key,self.prior,':',end=' ')
      print(self.left.key,self.left.prior)
      self.left.show()
    else:
      print('left child of ',self.key,self.prior,': None')
    if self.right is not None:
      print('right child of ',self.key,self.prior,':',end=' ')
      print(self.right.key,self.right.prior)
      self.right.show()
    else:
      print('right child of ',self.key,self.prior,': None')
    

tree=DTree(7,7)
tree=tree.Add(1,1)
tree=tree.Add(4,5)
tree=tree.Add(4,2)
tree=tree.Add(8,3)
tree=tree.Add(9,5)
tree=tree.Add(10,3)
tree=tree.delete(4)
tree.show()



