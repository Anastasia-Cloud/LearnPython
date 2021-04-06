#декартово дерево
from random import random
class DTree:

  def __init__(self,key,prior=random()):
    self.key=key
    self.prior=prior
    self.left=None
    self.right=None

  @staticmethod
  def Merge(lTree,rTree):
    if lTree is None:
      return rTree
    if rTree is None:
      return lTree
    if lTree.prior>rTree.prior:
      lTree.right=DTree.Merge(lTree.right,rTree)
      return lTree
    else:
      rTree.left=DTree.Merge(rTree.left,lTree)
      return rTree

  def Split(self,x):
    if self.key>x:
      if self.left is None:
        print('self.left is None')
        rTree=DTree(self.key,self.prior)
        rTree.right=self.right
        rTree.left=None
        lTree=None
        rTree.show()
        return (lTree,rTree)
      else:
        rTree=DTree(self.key,self.prior)
        rTree.right=self.right
        lTree,rTree.left=self.Split(x)
    else:
      if self.right is None:
        print('self.right is None')
        lTree=DTree(self.key,self.prior)
        lTree.left=self.left
        lTree.right=None
        rTree=None
        return (lTree,rTree)
      else:
        lTree=DTree(self.key,self.prior)
        rTree.right=self.right
        lTree.right,rTree=self.Split(x)

  def Add(self,key):
    lTree,rTree=self.Split(key)
    self=DTree.Merge(DTree.Merge(lTree,DTree(key,random())),rTree)
    print('item added!')

  def show(self):
    if self.left is not None:
      print('left child of :',self.key,self.prior)
      self.left.show()
    print(self.key,self.prior)
    if self.right is not None:
      print('right child of :',self.key,self.prior)
      self.right.show()
    pass

tree=DTree(15)
tree.Add(3)
tree.Add(33)
tree.Add(1)
tree.Add(45)
tree.Add(67)
tree.Add(111)
tree.Add(0)
tree.show()
print(tree)



