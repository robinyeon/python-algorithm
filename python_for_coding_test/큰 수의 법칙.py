n, m, k = map(int, input().split())
numbers1 = list(map(int, input().split()))
# print("numbers1:", numbers1)
max1 = max(numbers1)
# print("max1", max1)
numbers1.remove(max1)
max2 = max(numbers1)
# print("max2:", max2)

sum = ((max1*k)+(max2*1))*(m//k)

print(sum)