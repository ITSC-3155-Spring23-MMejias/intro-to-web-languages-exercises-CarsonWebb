sum=0
i=0
while i<5:
    num=input(f'Enter integer #{i+1}: ')
    if num.isdigit() ==True:
        i=i+1
        sum=sum+int(num)
    if num.isdigit() ==False:
        print('Invalid input. Enter Integer')
print(f'the sum is:{sum}')
