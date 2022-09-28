n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인하는 법 
for i in range(n):
    data = list(map(int, input().split()))
    minimum = min(data)
    result = max(result, minimum)

print(result)