# 유기농 배추

import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0 ,0]
dc = [0, 0, 1, -1]

def DFS(r, c):
    # 방문 표시 (0 만들기)
    field[r][c] = 0
        
    # 탐색
    for d in range(4):
        # 지금 좌표(r,c) => 이동할 좌표(r+dr[d], c+dc[d])
        nr, nc = r + dr[d], c + dc[d]
        # 방문이 가능한 범위
        if 0 <= nr < N and 0<= nc < M and field[nr][nc] == 1:
            DFS(nr, nc)

def BFS(r, c):
    #세팅 (queue 만들기)
    queue = deque([(r,c)])
    #방문 (필요 없음)
    #탐색
    while queue:
        r, c = queue.popleft()
    #방문 체크
        field[r][c]=0
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            
            if 0 <= nr < N and 0<= nc < M and field[nr][nc] == 1:
                #큐에 넣기
                queue.append((nr, nc))
    

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    visited = set()
    # 빈 판 만들기
    field = [[0]*M for _ in range(N)]
    # print(field)
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
        # print(field)
    ans = 0

    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                ans += 1
            BFS(r,c)
    print(ans)