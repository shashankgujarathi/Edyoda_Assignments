numbers = list(map(int, input().split(',')))
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even = even+1
    else:
        odd = odd+1
print(f'Number of even numbers : {even}')
print(f'Number of odd numbers : {odd}')
