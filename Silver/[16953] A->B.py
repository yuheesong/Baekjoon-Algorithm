from collections import deque

A,B = map(int, input().split()) #A는 초기값, B는 목표값
queue=deque([])
queue.append([A,0])
def bfs(A):
    while queue:
        num,cnt=queue.popleft()
        if num > B:
            continue
        elif num == B:
            print(cnt+1)
            break
        queue.append([int(str(num)+"1"),cnt+1])
        queue.append([num*2,cnt+1])
    else:
        print(-1)

bfs(A)
