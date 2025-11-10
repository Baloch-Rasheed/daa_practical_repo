from linked_list.node import Node

class LinkedList:

    def __init__(self):
        self.root = None

    def insert(self, node : Node):
        current_node = self.root
        if current_node == None:
            self.root = node
        else:
            while current_node:
                if current_node.next_node == None:
                    current_node.next_node = node
                    return
                else:
                    current_node = current_node.next_node
    
    def treverse(self):
        current_node = self.root
        while current_node is not None:
            print (f'[Node: {current_node.data}]')
            current_node = current_node.next_node