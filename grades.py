kid = [{'school_class': '4a', 'scores':[3,4,4,5,2]},
       {'school_class': '4b', 'scores':[5,4,5,5,3]},
       {'school_class': '4c', 'scores':[1,1,1,1,1]}]
summ = 0
summ1 = 0
summ2 = 0
summ3 = 0
q = 0
q1 = 0
q2 = 0
for k in kid:
    for s in k.get("scores"):
        summ = summ + s
        if k['school_class'] == '4a':
            summ1 = summ1 + s
            q = q+1
        if k['school_class'] == '4b':
            summ2 = summ2 + s
            q1 = q1+1    
        if k['school_class'] == '4c':
            summ3 = summ3 + s
            q2 = q2+1           
print('Средняя оценка учеников в классе 4a составляет  ',summ1/q)
print('Средняя оценка учеников в классе 4b составляет  ',summ2/q1)
print('Средняя оценка учеников в классе 4c составляет  ',summ3/q2)
print('Средняя оценка всех учеников:  ', summ/(5*len(kid)))