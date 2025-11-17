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
    
    def delete(self, data):
        current_node = self.root

        if current_node == None:
            print('Its Empty')
        else:
            if current_node.data == data:
                self.root = current_node.next_node
            while current_node.next_node != None:
                if current_node.next_node.data == data:
                    # deleting mechanism
                    current_node.next_node = current_node.next_node.next_node
                    return
                else:
                    current_node = current_node.next_node
            print("Data not found in list")

    def modify(self,data, new_data):
        current_node = self.root

        while current_node:
            if current_node.data == data:
                current_node.data = new_data
                return
            else:
                current_node = current_node.next_node
        print("Data not found to be modified")

        
            

