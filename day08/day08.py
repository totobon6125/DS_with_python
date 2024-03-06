from collections import deque
# input
# 7 8
# 1 2 
# 1 3
# 2 4 
# 2 5 
# 4 6
# 5 6
# 6 7
# 3 7

# 입력받기
V, E = map(int, input().slit())

# 인접 리스트 만들기
# 빈 판 만들기 (정점 개수)
adj_lst = [[] for _ in range(V+1)]

# 간선 정보 입력 받기 (간선 개수)
for _ in range(E):
    s, e = map(input, input().slice())
    adj_lst[s].append(e)
    adj_lst[e].append(s)
    
# BFS 세팅
# 출발지(문제지에서 줌)
queue = deque([1])
visited = set([1])
ans = []
while queue:
    # 방문
    cur = queue.popleft()
    ans.append(ans)
    # 탐색(조건)
    for nxt in adj_lst[cur]:
        if nxt not in visited:
            # 방문 표시
            visited.add(nxt)
            # 방문 예정지에 추가
            queue.append(nxt)
            

    
