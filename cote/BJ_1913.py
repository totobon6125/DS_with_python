# 문제
# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

import sys
input = sys.stdin.readline

    # 하, 우, 상, 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N = int(input())
T = int(input())

snail = [[0]*N for _ in range(N)]

r, c, d = 0, 0, 0

for num in range(N**2, 0, -1) :
    if T == num:
        ar, ac = r + 1, c + 1
        
    snail[r][c] = num
    
    nr, nc = r + dr[d], c + dc[d]
    print("not if=>", nr, nc)
    if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
            print("if=> ", nr, nc)
        
    r, c = nr, nc

for line in snail:
    print(*line)
print(ar, ac)