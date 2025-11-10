class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def next_node_is(self, next_node):
        self.next_node = next_node