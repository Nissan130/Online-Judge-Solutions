n,d = map(int, input().split())

q = int(n / d)
r = n%d 
print(f"{q} {r} {d}")