# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로 => sorted (key=lamda)
# 단, 중복된 단어는 하나만 남기고 제거해야 한다. => set()

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000)
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.

import sys
input = sys.stdin.readline

# 개수가 들어옴.
N = int(input())

# 단어를 입력 받음.
words = [input().rstrip() for _ in range(N)]
# print("1", words)

# 중복제거
words = list(set(words))
# print("2", words)

# 정렬(단어의 길이, 사전순)
words = sorted(words, key=lambda x : (len(x), x))
# key 는 정렬의 기준, x 는 words의 원소, len(x) - 길이순으로 정렬, x - 사전순으로 정렬 
# print("3", words)

# 형식에 맞게 출력
for word in words:
    print(word)


#-----------------------
# 트러블 슈팅
    # N = map(int, input()) >>> N = int(input())
    # N 값이 하나만 받기 때문에 map 을 사용할 필요가 없다!!!