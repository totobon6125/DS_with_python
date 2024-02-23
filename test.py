def recursion_func():
    i = 0
    print('i=>', i)
    i = i + 1
    if (i == 3):
      return "재귀함수 끝"
    recursion_func()

recursion_func()