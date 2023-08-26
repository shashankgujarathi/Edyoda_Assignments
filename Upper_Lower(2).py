def upperLowerLetters(string):
    upper = 0
    lower = 0
    for letter in string:
        if ord(letter)>=65 and ord(letter)<=90:
            upper += 1
        elif ord(letter)>=97 and ord(letter)<=122:
            lower += 1
    return upper, lower


string = input()
upper, lower = upperLowerLetters(string)
print('No. of Upper case characters :', upper)
print('No. of Lower case characters :', lower)
