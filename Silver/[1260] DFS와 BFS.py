from collections import deque

N,M,V = map(int,input().split()) #N은 정점개수, M은 간선개수, V는 탐색시작할 정점 번호
graph = [[0]*(N+1) for _ in range(N+1)]

visited_dfs=[0]*(N+1)
visited_bfs=[0]*(N+1)
visited_dfs[V]=1
visited_bfs[V]=1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

def bfs(V):
    queue = deque([V])
    while queue:
        v=queue.popleft()
        print(v, end=" ")
        for i in range(1,N+1):
            if not visited_bfs[i] and graph[i][v]:
                queue.append(i)
                visited_bfs[i]=1

def dfs(V):
    print(V, end=" ")
    visited_dfs[V]=1
    for i in range(1,N+1):
        if not visited_dfs[i] and graph[i][V]:
            dfs(i)
    
dfs(V)
print()
bfs(V)
