from queue import PriorityQueue
import math

finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 4\\input2.txt", "r")
foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 4\\output2.txt", "w")


def Dijkstra(adj, source):
    q = PriorityQueue()
    visited = [False] * len(adj)
    dist = [math.inf] * len(adj)
    prev = [-1] * len(adj)
    dist[source] = 0
    q.put((dist[source], source))
    while not q.empty():
        u = q.get()[1]
        if visited[u]:
            continue
        visited[u] = True

        for v in adj[u]:
            alt = dist[u] + v[1]
            if(alt < dist[v[0]]):
                dist[v[0]] = alt
                prev[v[0]] = u
                q.put((dist[v[0]], v[0]))

    cur = len(adj)-1
    path = []
    while(cur != 1):
        path.append(cur)
        cur = prev[cur]
    path.append(1)
    path.reverse()
    foutput.write(str(path) + "\n")


for i in range(int(finput.readline())):
    N, M = map(int, finput.readline().split())
    adj = [[] for x in range(N + 1)]
    for j in range(M):
        u, v, w = map(int, finput.readline().split())
        adj[u].append((v, w))

    Dijkstra(adj, 1)
