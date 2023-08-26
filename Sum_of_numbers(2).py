def sumOfNumbers(lst):
    return sum(lst)

lst = list(map(int, input().split()))
result = sumOfNumbers(lst)
print(result)
