end_number = int(input())
first_number = 1
second_number = 1
lst = []
lst.append(first_number)
lst.append(second_number)
while second_number < end_number:
    temp = first_number
    first_number = second_number
    second_number = temp+first_number
    lst.append(second_number)
print(lst[:-1])
