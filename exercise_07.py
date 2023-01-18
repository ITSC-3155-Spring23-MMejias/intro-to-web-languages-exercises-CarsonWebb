num=0
list=[]
while num !="QUIT" or "Quit" or "quit":
    num=input('Enter a number or QUIT to quit:')
    list.append(num)
list.remove(num)
print(f'All nums: {list}')
even=[]
for elem in list:
    if(int(elem)%2==0):
        even.append(elem)
print(f'Even nums: {even}')