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
