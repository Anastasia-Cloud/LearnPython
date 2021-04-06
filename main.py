#декартово дерево

class DTree:

  def __init__(self,key,prior):
    #self.root=None
    self.key=key
    self.prior=prior
    self.left=None
    self.right=None
  
  def Merge(self,lTree,rTree):
    if lTree is None:
      return rTree
    if rTree is None:
      return lTree
    if lTree.prior>rTree.prior:
      lTree.right=self.Merge(lTree.right,rTree)
      return lTree
    else:
      rTree.left=self.Merge(rTree.left,lTree)
      return rTree

  def Split(self,x):
    if self.key>x:
      if self.left is None:
        rTree=DTree(self.key,self.prior)
        rTree.right=self.right
        rTree.left=None
        lTree=None
        return (lTree,rTree)
      else:
        rTree=DTree(self.key,self.prior)
        rTree.right=self.right
        lTree,rTree.left=self.Split(x)
    else:
      if self.right is None:
        lTree=DTree(self.key,self.prior)
        lTree.left=self.left
        lTree.right=None
        rTree=None
        return (lTree,rTree)
      else:
        lTree=DTree(self.key,self.prior)
        rTree.right=self.right
        lTree.right,rTree=self.Split(x)

  


