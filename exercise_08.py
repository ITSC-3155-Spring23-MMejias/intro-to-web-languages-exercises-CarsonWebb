list=[]
list1=[]
x=0
unique=True
for i in range (10):
    num=int(input(f'Enter number {i+1}:'))
    list.append(num)
print(f'Original List: {list}')
for elem in list:
    if list.count(elem)==1:     #https://favtutor.com/blogs/python-count-occurrences-in-list
        list1.append(elem)      #used the .count in order to count occurances of an element in the list
print(f'Numbers that appear once: {list1}')