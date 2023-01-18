list1=[]
list2=[]
clist=[]
same=False
for i in range (5):
    num=int(input('Enter a number for the first list:'))
    list1.append(num)
for i in range (5):
    num=int(input('Enter a number for the second list:'))
    list2.append(num)
for elem in list1:
    if (elem in list2) and (elem not in clist):
        clist.append(elem)
print(f'First list: {list1}')
print(f'Second list: {list2}')
print(f'Common list: {clist}')
