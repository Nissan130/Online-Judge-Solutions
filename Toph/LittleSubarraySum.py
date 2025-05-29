n, a, b = map(int, input().split())
numbers = list(map(int, input().split()))

sum = 0
for i in range(a,b+1):
    sum  = sum + numbers[i]
print(sum)