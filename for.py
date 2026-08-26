#For loop
'''Program to find the length of a given collection without using len function.
Enter the collection value in "" commas or in any collection datatype like (),[],{},etc
c=eval(input("Enter the collection : "))
count=0
for i in c:
        count=count+1
print(count)'''


'''Program to replace space by an underscore in a given string.
s=input("Enter the string : ")
res=''
for i in s:
    if i==' ':
        res+='_'
    else:
        res+=i
print(res)'''


'''Program to check whether the given string is palindrome or not without using slicing
s=input("Enter the value : ")
rev=''
for i in s:
    rev=i+rev
if s==rev:
    print("It is a palindrome")
else:
    print("Not a palindrome")'''


'''WAP to extract all the integers which are multiple of 5 and has three digits in it from the given list.
l=eval(input("Enter the list : "))
out=[]
for i in l:
    if type(i)==int and i%5==0 and 100 <= i <=999:
        out+=[i]
print(out)'''


'''WAP to remove duplicate values from the list.
l=[12,34,12,56,78,12,78,34]
out=[]
for i in l:
    if i not in out:
        out.append(i)
print(out)'''


'''WAP to get the following output.
t=(12,3.4,'hai',8+8j,'python','ab',8+3j)
out={'hai':3,'python':6,'ab':2}

t=eval(input("Enter the collection : "))
out={}
for i in t:
    if type(i)==str:
        out[i]=len(i)
print(out)'''


'''WAP to get the following output
s='aPPlE#23'
out={'a':'A','P':'p','l':'L','E':'e'}

s=input("Enter the string : ")
out={}
for i in s:
    if 'a' <= i <= 'z':
        out[i]=chr(ord(i)-32)
    if 'A' <= i <= 'Z':
        out[i]=chr(ord(i)+32)
print(out)'''


'''WAP to create a string with uppercase characters from A to z.
upper=''
for i in range(ord('A'),ord('Z')+1):
    upper+=chr(i)
print(upper)'''



'''WAP to get the following output.
s='hai hello how are you'
out={'hai':3,'hello':5,'how':3,'are':3,'you':3}

s=input("Enter the value : ")
words=s.split()
out{}
for i in words:
    out[i]=len(i)
print(out)'''


'''WAP to get the following output.
l=['python.py','prol.html','pro3.py','google.com']
out=['py','html','py','com']

l=eval(input("Enter a list : "))
out=[]
for i in l:
    r=i.split('.')
    out+=[r[-1]]
print(out)'''


'''WAP to get the following output.
l=['pro1.html','pro2.py','file1.txt','yahoo.in']
out{'html':'pro1','py':'pro2','txt':'file1','in':'yahoo'}

l=eval(input("Enter the list : "))
out={}
for i in l: #i='pro1.html'
    r=i.split('.') #['prol','html']
    out[r[-1]]= r[0]
print(out)'''


'''WAP to get the following output.
s='hai hello how'
out='iah olleh woh'

s=input("Enter a string : ").split()
out=[]
for i in s:
    out.append(i[::-1])
print(' '.join(out))'''


'''WAP to get the following output.
s='example on for loop'
out='ee on fr lp' 

s=input("Enter a string : ").split() #['example','on','for','loop']
out=[]
for i in s:
    out.append(i[0]+i[-1])
print(' '.join(out))'''


'''WAP to get the following output.
s='abcabacbcc'
out='a3b3c4' 
#use count function
Syntax: var.count('character', start_index, end_index)

s=input("Enter the string : ")
out=''
for i in s:
    if i not in out:
         c=s.count(i)
         out+=i+str(c)
print(out)'''


'''WAP to extarct only the unique values from the given list; here the unique values\
refers to the value which got repeated only for once.
l=[12,34,12,56,78,34]
out=[56,78]

l=eval(input("Enter a list : "))
out=[]
for i in l:
    if l.count(i)==1:
        out.append(i)
print(out)'''


'''WAP to get the following output.
s='abcaabccbbb'
out={'a':3,'b':5,'c':3} without using count function. 

l=input("Enter the string : ")
out={}
for i in l:
    if i in out:
        out[i] = out[i] + 1
    else:
        out[i] = 1
print(out)'''


'''WAP to get the following output.
l=['p1.py','file2.txt','file1.py','google.com','data.txt']
out={'py':['p1'],'txt':['file2','data'],'com':['google']} 


l=eval(input("Enter the list : "))
out={}
for i in l:
    r=i.split('.')
    if r[-1] in out:
        out[r[-1]].append(r[0])
    else:
        out[r[-1]]=[r[0]]
print(out)'''


'''WAP to check whether the given number is armstrong number or not
n=int(input("Enter the number : "))
sum=0
for i in str(n):
    sum+=int(i)**len(str(n))
if n==sum:
    print("It is Armstrong number")
else:
    print("It is not Armstrong number")'''


'''Comsider a dictionary consists of student name with result and extract key\
value pair from the dictionary only if student scored more than 80

d={'akash':89,'prasanth':67,'anitha':79,'renu':99}
out={}
for i in d: #i='akash','prasanth','anitha','renu'
    if d[i]>80:
        out[i]=d[i]
print(out)'''


'''Extract key value pairs from the dictionary only if key is of string type.

d=eval(input("Enter the dictionary :"))
out={}
for i in d:
    if type(i)==str:
        out[i]=d[i]
print(out)'''


'''WAP to get the following output.
d={'Taj':'T5','Pallavi':'T4','Vishwa':'T23'}
out={'T5':'Taj','T4':'Pallavi','T23':'Vishwa'}

d=eval(input("Enter the dictionary : "))
out={}
for i in d:
    out[d[i]]=i
print(out)'''


#Nested for loop
'''for i in range(1,5):
    for j in range(1,9,3):
        print(i,j)'''
        
'''Program to check whether the given no is strong number or not.
Strong number = If a given no is exactly equal to the/
sum of factorial of individual digits.
EX: n=12
    =1!+2!
    =1+2
    =3 which is not equal to 12 so not a strong no

EX: n=145
    =1!+4!+5!
    =1+24+120
    =145 which is equal to 145 then it is strong number'''

'''n=int(input("Enter the number : "))
sum_fact=0
for i in str(n):
    num=int(i)
    fact=1
    for j in range(num,0,-1):
        fact*=j
    sum_fact+=fact
if n==sum_fact:
    print("It is a strong number")
else:
    print("It is not a strong number")'''


'''WAP to get the following output.
l=[12,'program',6+78j,4.5,'break',9]
out={'program':'oa','break':'ea'}

l=eval(input("Enter the list : "))
out={}
for i in l:
    if type(i)==str:
        vow=''
        for j in i:
            if j in 'AEIOUaeiou':
                vow+=j
        out[i]=vow
print(out)'''


#Assignment Question
'''WAP to get the following output.
l=[12,'program',6+78j,4.5,'break',9]
out1={'program':'prgrm','break':'brk'}
out2={'program':'PROGRAM','break':'BREAK'}

l=eval(input("Enter the list : "))
out1={}
out2={}
for i in l:
    if type(i)==str:
        const=''
        for j in i:
            if j not in 'AEIOUaeiou':
                const+=j
        out1[i]=const
        upper=''
        for j in i:
            if 'a' <= j <= 'z':
                upper+=chr(ord(j)-32)
            else:
                upper+=j
        out2[i]=upper
print(out1)
print(out2)'''


'''WAP to get the following output.
l=[10,13,4,6]
out[23,20,29,27]
so logic to get the output is like when considering i=10 ignore 10\
and then add the other remaining values.
for i=13 ignore 13 and add the other values.

l=eval(input("Enter the list : "))
out=[]
for i in range(0,len(l)):
    sum=0
    for j in range(0,len(l)):
        if i!=j:
            sum+=l[j]
    out.append(sum)
print(out)'''


'''WAP to get the following output.
l=[1000,700,100,300,900,200]
n=1000
out=[[1000],[700,300],[100,900]]

l=eval(input("Enter the list : "))
n=1000
out=[]
for i in range(0,len(l)):
    if l[i]==n:
        out.append([l[i]])
    else:
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
                out.append([l[i],l[j]])
print(out)'''


'''WAP to where a list is given and from that list check by adding which two numbers\
we get the desired output.
ex:- l=[10,15,20,5,20,10,50]
out=35
and then at last also return by adding which numbers we got the desired output'''
