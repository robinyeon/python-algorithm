import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sum_list = []

max = 0
for x in itertools.combinations(cards, 3):
    if max < sum(x) <= m:
        max = sum(x)

print(max)