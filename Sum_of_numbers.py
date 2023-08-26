def sumOfNumbers(lst):
    total_sum = 0
    for number in lst:
        total_sum += number
    return total_sum

lst = list(map(int,input().split()))
result = sumOfNumbers(lst)
print(result)