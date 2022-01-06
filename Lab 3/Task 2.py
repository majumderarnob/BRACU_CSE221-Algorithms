finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 3\\input.txt")

given_inp = finput.read().split('\n')
new_dict = {}

for i in range(1, len(given_inp)):
    store = given_inp[i]
    x = store.split()
    y = int(x[0])
    lst = []
    for j in range(1, len(x)):
        lst.append(int(x[j]))
    new_dict[y] = lst

# for k in new_dict:
#     print(str(k) + "-->" + str(new_dict[k]))

visited = [0] * 12
queue = []


def BFS(visited, graph, node, endPoint):
    visited[int(node) - 1] = 1
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(str(m), end=' ')
        if(m == endPoint):
            break
        for neighbour in graph[m]:
            if(visited[int(neighbour) - 1] == 0):
                visited[int(neighbour) - 1] = 1
                queue.append(neighbour)


BFS(visited, new_dict, 1, 12)
