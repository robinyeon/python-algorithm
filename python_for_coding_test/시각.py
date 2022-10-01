n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h)+str(m)+str(s):
                count += 1

print(count)

# N:59:59 까지 포함해야하기때문에 hour부분을 담당하는 h의 범위를 n+1로 설정하는것 주의