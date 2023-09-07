
lst = list(map(int,input().split()))
triple_function = lambda num : num * 3
result = list(map(triple_function,lst))
print(result)