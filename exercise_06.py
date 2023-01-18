row=int(input('Enter a row number from 1 to 5:'))
col=int(input('Enter a col number form 1 to 5:'))
for i in range(5):
    for j in range(5):
        if(i+1==row)and(j+1==col):
            print('1',end=" ")
        else:
            print('0',end=" ")
    print('')