list=[]
string=input('Enter a string:')
for letter in string:
    list.append(letter)
for elem in reversed(list):
    print(elem,end="")