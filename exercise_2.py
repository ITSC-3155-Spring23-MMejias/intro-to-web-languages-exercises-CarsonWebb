list=[]
string=input('Enter a string:')
for letter in string:
    if letter.islower():
        list.append(letter)
for letter in string:
    if letter.isupper():
        list.append(letter)
for elem in list:
    print(elem,end="")