import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 재귀함수 구현
# def recursion_func(depth):
#     if depth == 10:
#         print('발굴 완료')
#         return
    
#     print(f'내려가는 중.. 현재 깊이는 {depth}')
#     recursion_func(depth+1)
#     print(f'올라가는 중.. 현재 깊이는 {depth}')
# recursion_func(0)
#-------------------------------------------------------

# 메모리제이션 => DP
# def fibo(n):
#     if n <= 1:
#         return n
    
#     return fibo(n-1) + fibo(n-2)

# N = int(input())

# print(fibo(N))



# 그래프 구조화 방법 => 인접 행렬 / 리스트

# V, E = map(int, input().split())

# # 인접 행렬
# #1 빈 판 만들기
# adj_martix = [[0]*(V+1) for _ in range(V+1)]

# #2 입력 받기
# for _ in range(E):
#    v1, v2, d = map(int, input().split()) 
#    adj_martix[v1][v2] = 1
#    # 무방향 그래프인 경우 아래 코드도 들어가야 함.
#    adj_martix[v2][v1] = 1

     # 가중치 d 를 입력함 
#    adj_martix[v1][v2] = d
#    # 무방향 그래프인 경우 아래 코드도 들어가야 함.
#    adj_martix[v2][v1] = d

# print(adj_martix)

# 인접 리스트 만들기
# V, E = map(int, input().split())
# adj_list = [[] for _ in range(V+1)]
# print(adj_list)

# for _ in range(E):
#    v1, v2, d = map(int, input().split()) 

#    adj_list[v1].append((v2,d))
#    adj_list[v2].append((v1,d))

from collections import deque

# deque 는 양 끝에서만 자료를 넣고 뺄 수 있음

queue = deque()
queue2 = deque([1,2])
queue3 = deque((3,4))
# 뒤에서 넣는 거=> queue.append()
# 뒤에서 빼는 거=> queue.pop()
# 앞에서 빼는 거=> queue.popleft()

queue.append(0) #deque([0])
queue.append(1) #deque([0, 1])
queue.append([1,2,3]) #deque([0,1,[1,2,3]])
queue.popleft()  #deque([1,[1,2,3]])
queue.pop()  #deque([1])
print(queue)
print(queue2)
print(queue3)