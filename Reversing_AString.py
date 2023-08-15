string = input()
reversed_string = ''
for letter in range(len(string)-1, -1, -1):
    reversed_string = reversed_string + string[letter]
print(reversed_string)
