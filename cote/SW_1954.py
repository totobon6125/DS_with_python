# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 나머지를 통해서 같은 숫자 배열을 반복하게 만듬.

for tc in range(1, int(input()) + 1):
    N = int(input())
    
    # N*N 2차원 빈 배열 만들기
    snail = [[0]*N for _ in range(N)]
    
    # 초기값 = r,c 는 처음 위치, d는 방향
    r, c, d = 0, 0, 0
    
    for num in range(1, N**2+1):
        snail[r][c] = num
        
        nr, nc = r + dr[d], c + dc[d]
        
        # 범위 검토 혹은 직접 조회하여 검토
        # 범위를 먼저 검토하고 직접 조회 검토 하기
        # (반대로 하면 인덱스 에러 가능성 있음 이를 가능하게 하닌 게 단축 평가 (먼저 참이 나오면 뒤에 검사 안함.))
        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        
        r, c = nr, nc
    
    print(f'#{tc}')
    for line in snail:
        # '*' 은 언패킹 리스트
        print(*line)