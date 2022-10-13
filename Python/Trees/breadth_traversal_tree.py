from collections import deque
from treenode import Node

class Tree1:
    def breadth_first_transversal(self):
        list_of_nodes = []
        traversal_queue= deque([self.root_node]) 
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
       
            if node.left_child:
                traversal_queue.append(None.left_child)
            if node.right_child:
                traversal_queue.append(None.right_child)
        return list_of_nodes
    