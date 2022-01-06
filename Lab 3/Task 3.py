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
printed = []


def DFS_VISIT(graph, node):
    visited[int(node) - 1] = 1
    printed.append(node)
    for l in graph[node]:
        if(l not in visited):
            DFS_VISIT(graph, l)


def DFS(graph, endPoint):
    for m in graph:
        if(m not in visited):
            DFS_VISIT(graph, m)
    for n in printed:
        print(n, end=' ')
        if(n == endPoint):
            break


DFS(new_dict, 12)
