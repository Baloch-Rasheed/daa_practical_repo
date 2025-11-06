# from sub_string_matching import sub_string_matching_algorithm
# from floyd_warshall import floyd_warshall_algorithm
from binary_search_tree import node

def main():
    node1 = node.Node(434)
    node2 = node.Node(300)
    node3 = node.Node(500)

    node1.left_side = node2
    node1.right_side = node3
    temp = node1
    for i in range(2):
        print(temp.key)
        temp = temp.right_side



    

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



