#двоичное дерево поиска
tree={5:[3,8,None],3:[1,4,5],8:[6,11,5],1:[None,None,3],4:[None,None,3],6:[None,None,8],11:[None,None,8]}

def inorderTraverse(tree,r):
  if tree[r][0] in tree:
    inorderTraverse(tree,tree[r][0])
  print(r)
  if tree[r][1] in tree:
    inorderTraverse(tree,tree[r][1])

