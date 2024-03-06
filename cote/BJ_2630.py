# 색종이 만들기 - 분할 정복 
# 검색범위 안에 있는 숫자가
    # 다 같으면 => 종료조건
    # 하나라도 다르면 => 재귀(4분할 하기)
import sys
input = sys.stdin.readline

# n 종이 한 변의 길이
def divide_conqure(r, c, n):
    global white, blue
    
    color = paper[r][c]
    
    for i in range(r, r + n):
        for j in range(c, c + n):
            
            if color != paper[i][j]:
                divide_conqure(r, c, n//2)
                divide_conqure(r, c+n//2, n//2)
                divide_conqure(r+n//2, c, n//2)
                divide_conqure(r+n//2, c+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input().rstrip()) # rstrip() 을 붙여야 바로 아래 빈칸이 안 생김.
paper = [list(map(int, input().split()))]




