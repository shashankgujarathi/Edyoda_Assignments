def  upperLowerLetters(string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower +=1
    return upper,lower


string = input()
upper , lower = upperLowerLetters(string)
print('No. of Upper case characters :',upper)
print('No. of Lower case characters :',lower)