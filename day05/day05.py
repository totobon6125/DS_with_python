# 2중 배열의 회전
matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# n = 3
# rotated_matrix = [[0] * n for _ in range(n)] # 초기화

# for i in range(n):
#     for j in range(n):
#         rotated_matrix[i][j] = matrix[n-j-1][i]
# # rotated_matrix 결과

# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]

r, c = 1, 1

# 델타 세팅
    # 4방향(상, 하, 좌, 우)    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

    # 8방향(상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
# dr = [-1, 1, 0, 0, -1, -1, 1, 1]
# dc = [0, 0, -1, 1, -1, 1, -1 ,1]

for d in range(4):
   nr, nc = r + dr[d], c + dc[d]
   # 인덱스 에러 방지용
   if 0 <= nr < 3 and 0 <= nc < 3:
    print(matrix[nr][nc])   