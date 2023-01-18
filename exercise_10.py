list=[]
list1=[]
x=0
string=input('Enter a string:')
for letter in string:
    list.append(letter)
    x=x+1
    if x==3:
        list1.append(list)
        list=[]
        x=0
list1.append(list)
print(list1)