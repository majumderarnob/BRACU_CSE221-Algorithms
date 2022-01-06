from queue import PriorityQueue
import math

finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 4\\input4.txt", "r")
foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 4\\output4.txt", "w")


def Network(adj, source):
    Q = PriorityQueue()
    visited = [False] * len(adj)
    dist = [-math.inf] * len(adj)
    dist[source] = math.inf
    Q.put((-1 * dist[source], source))
    while not Q.empty():
        u = Q.get()[1]
        if visited[u]:
            continue
        visited[u] = True
        for v in adj[u]:
            alt = min(dist[u], v[1])
            if(alt > dist[v[0]]):
                dist[v[0]] = alt
                Q.put((-1 * dist[v[0]], v[0]))
    for i in range(len(dist)):
        if(dist[i] == math.inf):
            dist[i] = 0
        if(dist[i] == -math.inf):
            dist[i] = -1
    foutput.write(str(dist[1:]) + "\n")


for item in range(int(finput.readline())):
    N, M = map(int, finput.readline().split())
    adj = [[] for x in range(N + 1)]
    for j in range(M):
        u, v, w = map(int, finput.readline().split())
        adj[u].append((v, w))
    sourse = int(finput.readline())
    Network(adj, sourse)
