from binary_search_tree.node import Node

class BST:

    def insert(self, node : Node):
        current_node = self._root
        if current_node == None:
            current_node = node
        else:
            while current_node:
                if node.key < current_node.key:
                    if current_node.left_side == None:
                        current_node.left_side = node
                    else:
                        current_node = current_node.left_side

                elif node.key > current_node.key:
                    if current_node.right_side == None:
                        current_node.right_side = node
                    else:
                        current_node = current_node.right_side
                else:
                    # when node is equal to parent node then
                    print("The Node is equal to Parent")
