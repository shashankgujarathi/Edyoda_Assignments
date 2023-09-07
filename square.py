
lst = list(map(int,input().split()))
square_function = lambda num : num ** 2
result = list(map(square_function,lst))
print(result)