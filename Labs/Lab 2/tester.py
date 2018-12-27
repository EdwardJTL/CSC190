from tree import *
from binary_tree import *
from queue import queue

#create tree
a = tree(1)
b = tree(2)
c = tree(3)
d = tree(4)
e = tree(5)
f = tree(6)
g = tree(7)
h = tree(8)

a.AddSuccessor(b)
a.AddSuccessor(c)
a.AddSuccessor(d)
c.AddSuccessor(e)
d.AddSuccessor(f)
d.AddSuccessor(g)
a.AddSuccessor(h)

#create equivalent binary tree
ba = binary_tree(1)
bb = binary_tree(2)
bc = binary_tree(3)
bd = binary_tree(4)
be = binary_tree(5)
bf = binary_tree(6)
bg = binary_tree(7)
bh = binary_tree(8)

ba.AddLeft(bb)
bb.AddRight(bc)
bc.AddRight(bd)
bc.AddLeft(be)
bd.AddLeft(bf)
bf.AddRight(bg)
bd.AddRight(bh)

#print tree
a.Print_DepthFirst()
#print level order
print (a.Get_LevelOrder())
#print equivalent binary tree
ba.print_tree(0)
#print level order
print (ba.Get_LevelOrder())

# <editor-fold desc="Description">
out = a.ConvertToBinaryTree()
out.print_tree(0)
print (out.Get_LevelOrder())
#test binary tree to general tree conversion
new = ba.ConvertToTree()
new[1].Print_DepthFirst()
print (new[1].Get_LevelOrder())