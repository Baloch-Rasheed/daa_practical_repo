# from sub_string_matching import sub_string_matching_algorithm
# from floyd_warshall import floyd_warshall_algorithm
# from binary_search_tree import node
# from linked_list.linked_list import LinkedList
# from linked_list.node import Node
from binary_search_tree.search_tree import BST

def main():


    bst_al = BST()

    bst_al.init()

    bst_al.insert(6)
    bst_al.insert(5)
    bst_al.insert(2)
    bst_al.insert(5.5)
    bst_al.insert(6.5)
    bst_al.insert(8)
    bst_al.insert(7)

    bst_al.traverse()




    # linkedList = LinkedList()

    # node1 = Node(68)
    # node2 = Node(78)
    # node3 = Node(80)
    # node4 = Node(50)

    # linkedList.insert(node1)
    # linkedList.insert(node2)
    # linkedList.insert(node3)
    # linkedList.insert(node4)

    # linkedList

    # print("Treverse dafault")
    # linkedList.treverse()
    # # print("Deleting 78...")
    # # linkedList.delete(68)
    # # linkedList.treverse()
    # print('Modifying 68 -> 43')
    # linkedList.modify(50, 43)
    # linkedList.treverse()

    
    

    # txt = 'My name is Kamal Khan, and they call me Kamal'
    # ptrn = 'Kamal Khan'

    # result = sub_string_matching_algorithm(text=txt, sub=ptrn)

    # print('results: ', result)

    # inf = float('inf')
    # graph = [
    #     [0, 5, 2, inf],
    #     [5, 0, 3, inf],
    #     [2, 3, 0, 2],
    #     [inf, inf, 2, 0]
    # ]

    # result = floyd_warshall_algorithm(graph)

    # for row in result:
    #     print(row)



if __name__ == "__main__":
    main()



