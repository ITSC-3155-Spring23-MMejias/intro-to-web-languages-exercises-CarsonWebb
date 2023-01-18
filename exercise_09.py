list=[]
for i in range(5):
    word=input('Enter a word:')
    list.append(word)
print('Words: [',end="")
for elem in list:
    print(f'{elem}, ',end="")
print(']')
print('One String: ',end="")
for elem in list:
    print(f'{elem} ',end="")
