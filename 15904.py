alpha = input()

target = ''

for i in alpha:
    if target == '':
        if i == 'U':
            target+=i
    elif target == 'U':
        if i == 'C':
            target += i
    elif target == 'UC':
        if i == 'P':
            target +=i
    elif target =="UCP":
        if i =='C':
            target += i
if target == "UCPC":
    print('I love UCPC')
else:
    print('I hate UCPC')