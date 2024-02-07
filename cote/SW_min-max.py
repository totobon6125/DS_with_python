# [입력]
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# input 을 받으면 항상 str 로 받아짐. 따라서 형변환이 필요한 경우가 있음
T = int(input())

# 변수를 for문 안에서 안 쓴다면 _ 를 입력함.
# T 번 반복한다는 뜻 range(T) = range(0,T,0)
for tc in range(1, T+1) :
    N = int(input())
    nums = list(map(int, input().split()))
    # min 은 1000001 max 는 0 을 초기값으로 두고 시작
    max_num = 0
    min_num = 1000001
    
    # 이 문제의 경우 N 을 통해 nums 의 길이를 줌. 따라서 nums.length 를 안 써도 됨.
    for i in range(N) :
        if nums[i] > max_num :
            max_num = nums[i]
        if nums[i] < min_num :
            min_num = nums[i]            
        
    ans = max_num - min_num
    # f string = f'문자열 입력, {변수}'
    print(f'#{tc} {ans}')