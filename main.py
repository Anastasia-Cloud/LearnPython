#декартово дерево

class DTree:

  def __init__(self,key,prior):
    #self.root=None
    self.key=key
    self.prior=prior
    self.left=None
    self.right=None