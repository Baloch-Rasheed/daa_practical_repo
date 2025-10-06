from sub_string_matching import sub_string_matching_algorithm
from floyd_warshall import floyd_warshall_algorithm

def main():
    # txt = 'My name is Kamal Khan, and they call me Kamal'
    # ptrn = 'Kamal Khan'

    # result = sub_string_matching_algorithm(text=txt, sub=ptrn)

    # print('results: ', result)

    inf = float('inf')
    graph = [
        [0, 5, 2, inf],
        [5, 0, 3, inf],
        [2, 3, 0, 2],
        [inf, inf, 2, 0]
    ]

    result = floyd_warshall_algorithm(graph=graph)

    for row in result:
        print(row)



if __name__ == "__main__":
    main()



