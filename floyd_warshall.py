def floyd_warshall_algorithm(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                distance = graph[j][i] + graph[i][k]
                if distance < graph[j][k]:
                    graph[j][k] = distance
    return graph


