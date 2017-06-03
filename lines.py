def compare(a,b):
    if a == b:
        return 1
    elif len(a) > len(b):
        return 2
    elif b =='learn': 
        return 3


line1 = str(input('Напиши слово:  '))
line2 = str(input('И еще одно:  '))
print(compare(line1,line2))