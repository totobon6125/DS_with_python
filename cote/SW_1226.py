from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

# 재귀
# def DFS(r,c):
#     global ans
#     # 방문
#         # 종료조건
#     if maze[r][c] == 3:
#         ans = 1
#         return
    
#     # 탐색(조건)
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if 0 > nr or nr >= 16 or 0 > nc or nc >= 16:
#             continue
#         if (nr, nc) in visited:
#             continue
    
#     # 방문표시
#         visited.add((nr, nc))
#     # 재귀
#         DFS(nr, nc)
    
    
# for tc in range(1, 11):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     visited = set()
#     ans = 0
    
#     for i in range(16):
#         for j in range(16):
#             if maze[i][j] == 2:
#                 visited.add((i,j))
#                 DFS(i, j)
                
#     print(f'#{tc} {ans}')
    

# BFS


def BFS(r,c):
    global ans
    queue = deque([(r, c)])
    
    while queue:
    # 방문
        r, c = queue.popleft()
        if maze[r][c] == 3:
            ans = 1
            return
    # 탐색(조건)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16 and (nr, nc) not in visited:
    # 방문표시
                visited.add((nr, nc))
    # 큐
                queue.append((nr, nc))
    
    
for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = set()
    ans = 0
    
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                visited.add((i,j))
                BFS(i, j)
                
    print(f'#{tc} {ans}')