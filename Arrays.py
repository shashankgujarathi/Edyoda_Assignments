
length = int(input())
lst = list(map(int,input().split()))

duplicate = []
for i in lst:
    if lst.count(i)>1:
        duplicate.append(i)
duplicate = list(set(duplicate))
if len(duplicate)>=1:
    duplicate.sort()
    print(duplicate)
else:
    print(-1)