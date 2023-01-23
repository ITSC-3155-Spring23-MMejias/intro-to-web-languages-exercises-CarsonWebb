my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
temp=0
combined_dict={}
for x in my_dict_1:
    for y in my_dict_2:
        if x==y:
            temp=my_dict_1.get(x)+my_dict_2.get(y)
            combined_dict.update({x:temp})
print(combined_dict)
