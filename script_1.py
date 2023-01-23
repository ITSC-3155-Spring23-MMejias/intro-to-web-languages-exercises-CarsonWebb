unique_list=[]
my_list = [9,1, 2, 3, 2, 1, 4,5,5,6,8,7,9,8]
for elem in my_list:
    if (elem not in unique_list):
        unique_list.append(elem)
print(unique_list)