from binary_search_tree.node import Node

class BST:
    
    def init(self):
        self._root = None

    # def insert(self, key: int):
    #     incoming_node = Node(key)
    #     if self._root is None:
    #         self._root = incoming_node
    #     else:
    #         current_node = self._root
    #         while current_node:
    #             if key < current_node.key:
    #                 # The incomming value should in left side
    #                 if current_node.left_side is None:
    #                     current_node.left_side = incoming_node
    #                     return
    #                 else:
    #                     current_node = current_node.left_side
    #             else:
    #                 # the equalant values should be in right
    #                 if current_node.right_side is None:
    #                     current_node.right_side = incoming_node
    #                     return
    #                 else:
    #                     current_node = current_node.right_side
    
    def insert(self, key):
        incoming_node = Node(key)
        if self._root is None:
            self._root = incoming_node
        else:
            self.__add_recursive(self._root, incoming_node)

        
    def __add_recursive(self, parent: Node, incoming_node: Node):

        if incoming_node.key < parent.key:
            if parent.left_side is None:
                parent.left_side = incoming_node
            else:
                self.__add_recursive(parent.left_side, incoming_node)
        else:
            if parent.right_side is None:
                parent.right_side = incoming_node
            else:
                self.__add_recursive(parent.right_side, incoming_node)
    
    def traverse(self):
        self.__treverse_recursive(self._root, 0)

    def __treverse_recursive(self, parent: Node, layer: int):

        if parent is None:
            return

        self.__treverse_recursive(parent.left_side, layer+1)
        print(f"Key: {parent.key}, Layer: {layer}")
        self.__treverse_recursive(parent.right_side, layer+1)


    

