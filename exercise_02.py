string1 =input('Enter a String:')
string2 =input('Enter another String:')
suffix=False
if string1 in string2:      #https://www.learndatasci.com/solutions/python-string-contains/#:~:text=The%20easiest%20and%20most%20effective,can't%20find%20the%20substring.
    suffix=True             #code just checks if one string is in another string and changes suffix to true if it is
if string2 in string1:
    suffix=True
print(f'{suffix}')