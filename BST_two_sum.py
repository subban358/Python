class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
def traverse(root, l):
  if root:
    l.append(root.val)
    traverse(root.left, l)
    traverse(root.right, l)
  return l  

def twoSumFromBST(root,l, s, target):
  l1 = traverse(root, l)
  for i in range(len(l)):
    if target-l[i] in s:
      return True
    else:
      s.add(l[i]) 
  return False     


root =  Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)  
s = set()
l = []
print(twoSumFromBST(root,l, s, 121))     