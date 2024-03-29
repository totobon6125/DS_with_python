# 문제
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
# 이 수열의 i번째 수부터 j번째 수까지의 합
# A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다.
# 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다.
# 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 경우의 수를 출력한다.

# 시간제한 = 0.5 연산이 5천만을 넘으면 안됨
# N = 10000 이고 시간복잡도가 N^2 이므로 1억이 됨. 따라서 시간초과가 나옴.

# 시스템 모듈을 import 해 와서 input 이 readline 을 대체하겠다.
# 백준 문제 풀 때 고정 코드로 두고 시작하기.
import sys
input = sys.stdin.readline

# 공백을 기준으로 숫자를 나누고 숫자형으로 변경하여 N과 M에 할당함.
N, M = map(int, input().split())

# 수열을 입력 받음
nums = list(map(int, input().split()))

# 시간 복잡도는 1/2 * N^2 이지만 상수 빼니까 N^2

# 5를 넘으면 볼 필요가 없음... 왜??

# 투포인터 알고리즘
l,r = 0,0
tmp = 0
ans = 0

while True:
    # 반복문 종료 조건
    if tmp < M:
        if r == N:
            break
        
        else:
            tmp += nums[r]
            r += 1
    
    elif tmp > M:
        tmp -= nums[l]
        l += 1
    # tmp == M
    else:
        ans += 1
        tmp -= nums[l]
        l += 1

print(ans)