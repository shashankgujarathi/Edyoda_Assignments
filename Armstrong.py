
number = int(input())
number = str(number)
total = 0
for i in number:
    total += int(i)**3
if total == int(number):
    print('Yes')
else:
    print('No')