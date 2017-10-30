import random
import collections

#a =random.sample(range(10), 10)    > unique values
a = [random.randrange(1, 10) for _ in range(0, 10)]
counter=collections.Counter(a)

print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(3))
# [(1, 4), (2, 4), (3, 2)]