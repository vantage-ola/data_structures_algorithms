from binarytree import Tree
from treenode import Node
tree=Tree()
tree.insert(1)
tree.insert(5)
tree.insert(2)
tree.insert(9)
tree.insert(7)

for i in range(1, 10):
    found= tree.search(i)
    print("[] : []".format(i, found))