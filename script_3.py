dict={}
string=input('Enter a string:').lower()
for letter in string:
    if letter != " ":
        dict.update({letter:string.count(letter)})
print(dict)