x, y = map(int, input().split())

if y%x == 0:
    additional_chocolet = 0
else:
    q = int(y / x)
    additional_chocolet = (q+1)*x - y
    
print(additional_chocolet)