#сплей-дерево 

class Node:
  def __init__(self, data):
     self.data=data
     self.left=None
     self.right=None
     self.pred=None
  def string(self):
    if self.left is not None:
      l=str(self.left.data)
    else:
      l='None'
    if self.right is not None:
      r=str(self.right.data)
    else:
      r='None'
    if self.pred is not None:
      p=str(self.pred.data)
    else:
      p='None'
    return 'data='+str(self.data)+', l='+l+', r='+r+', p='+p





class Tree:

  def __init__(self):
    self.root=None
    
  def insert(self,data):
    node=Node(data)
    if self.root is None:
      self.root=node
      print('node added in root!')
      return
    x=self.root
    y=None
    while x is not None:
      y=x
      if x.data<data:
        print(x.data,'<',data)
        x=x.right
      elif x.data>data:
        print(x.data,'>',data)
        x=x.left
      else:
        print(x.data,data)
        print('this node already exists')
        return
    node.pred=y
    if data>y.data:
      y.right=node
    else:
      y.left=node
    self.splayNode(node)
    print('node added!')
    return

  def inorderTraverse(self,node):
    if node.left is not None:
      self.inorderTraverse(node.left)
    print(node.string())
    if node.right is not None:
      self.inorderTraverse(node.right)
  
  def printTree(self):
    self.inorderTraverse(self.root)

  def search(self,data):
    key=self.root
    while key is not None:
      if data<key.data:
        key=key.left
      elif data>key.data:
        key=key.right
      else:
        return key.string()
    return 'no such node exists'

  def searchNode(self,data):
    key=self.root
    while key is not None:
      if data<key.data:
        key=key.left
      elif data>key.data:
        key=key.right
      else:
        self.splayNode(key)
        return key
    return None 

  def findRightNode(self,node):
    res=node
    predRes=None
    while res is not None:
      predRes=res
      res=res.right
    return predRes

  def delete(self,data):
    node=self.searchNode(data)
    print(node.string())
    if node is None:
      return 'no such node exists'
    if node.left is None and node.right is None:
      pred=node.pred
      if pred.left is not None and pred.left.data==data:
        pred.left=None
        return 'node deleted successfully!'
      elif pred.right is not None and pred.right.data==data:
        pred.right=None
        return 'node deleted successfully!'
    elif node.left is None:
      right=node.right
      pred=node.pred
      right.pred=pred
      if pred.left == node:
        pred.left=right
        return 'node deleted successfully!'
      elif pred.right == node:
        pred.right=right
        return 'node deleted successfully!'
    elif node.right is None:
      left=node.right
      pred=node.pred
      left.pred=pred
      if pred.left == node:
        pred.left=left
        return 'node deleted successfully!'
      elif pred.right == node:
        pred.right=left
        return 'node deleted successfully!'
    else:
      res=self.findRightNode(node.left)
      print(res.string())
      node.data=res.data
      pred=res.pred
      if pred.left is not None and pred.left.data==res.data:
        pred.left=None
      elif pred.right is not None and pred.right.data==res.data:
        pred.right=None
      return 'node deleted successfully!'
    return 'error('
    
  def splayNode(self,node):
    while node.pred is not None:
      pred=node.pred #y
      if pred.left==node:
        self.zig(pred,node)
      else:
        self.zag(pred,node)
    self.root=node

  def splay(self,data):
    node=self.searchNode(data)
    if node is not None:
      self.splayNode(node)
      print('success')
    else:
      print('no such node exists')
  
  def zig(self,nodeY,node):
    b=node.right
    pred=nodeY.pred
    if pred is not None:
      if pred.left==nodeY:
        pred.left=node
      else:
        pred.right=node
    node.pred=pred
    node.right=nodeY
    nodeY.pred=node
    nodeY.left=b
    if b is not None:
      b.pred=nodeY
    
  
  def zag(self,nodeY,node):
    b=node.left
    pred=nodeY.pred
    if pred is not None:
      if pred.left==nodeY:
        pred.left=node
      else:
        pred.right=node
    node.pred=pred
    node.left=nodeY
    nodeY.pred=node
    nodeY.right=b
    if b is not None:
      b.pred=nodeY
    
    
'''

tree = Tree()
tree.insert(33)
tree.insert(44)
tree.insert(67)
tree.insert(5)
tree.insert(89)
tree.insert(41)
tree.insert(98)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.insert(9)
tree.insert(89)
tree.printTree()
tree.splay(9)
tree.printTree()
print(tree.search(4))
print(tree.delete(33))
#tree.printTree()
'''
