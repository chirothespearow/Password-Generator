import random
questions=['What is your first name?','What is your surname?','What is the first word in the name of the first school you attended?','What is your father\'s first name?','What is your mother\'s first name?','What is the first name of your favorite actor?','What is your favorite sport?']
numbers=['What is your date of birth? (DD/MM/YY)','What is your apartment/house number?']
keywords=[]
answers=[]
answersN=['']
leeted=[]
print('You will now be asked various questions, enter na if you wish to skip that question.')
for i in questions:
    ans=input(i)
    if ans!='na':
        answers.append(ans)
for j in numbers:
    ans=input(j)
    if ans=='':
        answersN.append('')
    elif ans!='na':
        answersN.append(ans)
        
leet={'a':'@','b':'8','e':'3','h':'#','i':'!','o':'0','s':'$','z':'2'}
      
for k in answers:
    for l in leet:
        if l in k.lower():
            s=(k.replace(l,leet[l]))
            x=s.replace(l.upper(),leet[l])
            k=x
    leeted.append(k)        

if answersN[1]!='' or 'na':
    if '/' in answersN[1]:
        answersN[1]=answersN[1].replace('/','')
passwords=[]
count=0
while count<9:
    dec=random.randint(0,1)
    if dec==1:
        no=random.randint(0,len(leeted)-1)
        temp=''
        temp+=leeted[no]
        no2=random.randint(0,len(answersN)-1)
        temp+=str(answersN[no2])
        if temp not in passwords:
            passwords.append(temp)
            count+=1
        else:
            continue
    else:
        no2=random.randint(0,len(answersN)-1)
        temp+=str(answersN[no2])
        no=random.randint(0,len(leeted)-1)
        temp=''
        temp+=leeted[no]
        no2=random.randint(0,len(answersN)-1)
        temp+=str(answersN[no2])
        if temp not in passwords:
            passwords.append(temp)
            count+=1
        else:
            continue
    
print('\nSome possible passwords are:\n ')
for z in passwords:
    print(z)
    
    
        
    
    
    