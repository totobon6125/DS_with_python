from itertools import permutations, combinations

# 순열 과 조합
nums = [1,2,3]
perm = permutations(nums, 2)
combi = combinations(nums, 2)

print(list(perm))
print(list(combi))

