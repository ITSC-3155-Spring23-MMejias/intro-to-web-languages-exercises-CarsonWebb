list=[]
sum=0
size=int(input('Enter a number:'))
for i in range(size):
    num=int(input(f'Enter number {i+1}: '))
    list.append(num)
    sum=sum+num
print( 'List: {list}')
avg=sum/size
print(f'Average: {avg}')