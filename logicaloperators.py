#logical AND operator ensures that all the conditions are true
#logical OR operator ensures that at least one of the condition is true
cond1=input ('Do you know how to use Python? (yes/no): ').strip().lower()
cond2= input ('Do you know how to use SQL? (yes/no): ').strip().lower()
if cond1 == 'yes' and cond2 =='yes':
     print ('You are eligible to become a data analyst')
elif cond1 =='yes' and cond2 == 'no':
     print('You can choose whichever path in programming sice python is huge')
elif cond1=='no' and cond2 == 'no':
     print('Maybe you can start learning programming')
elif cond1 =='no' and cond2 =='yes':
    print('you can be in databases')
else:
    print ('It is not the end of the world')