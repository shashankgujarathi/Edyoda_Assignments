
length = int(input())
lst = []
for i in range(length):
    tup = tuple(input().split())
    lst.append(tup)

for i in range(length):
    for j in range(length-1):
        if lst[j][len(lst[0])-1] > lst[j+1][len(lst[0])-1]:
            lst[j+1],lst[j]=lst[j],lst[j+1]
            
print(lst)
