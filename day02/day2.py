# from collections import defaultdict
# 내장 모듈이 아니므로 수입해야 사용 가능
a = {'hi'}
# a = dict()

# 키에러 방지를 위해 defaultdict 를 사용함.
# 없는 키를 지정하면 그 키를 만들어 줌.
# () 에 value 의 형태로 하고 싶은 클래스 이름을 작성 int 작성하면 0 부터, list 를 넣으면 [] 이 나옴.
# b = defaultdict(int)

# b['key'] += 1
# print(b)

# set
a.add('hello')

print(a)

#회문 확인하는 법 (회문 앞으로 읽으나 뒤로 읽으나 같은 문자)
str = "hello"

if str == str[::-1]:
    print(True)
else :
    print(False)