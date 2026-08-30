#Function = It is a name given to memory block where the instructions are stored & which are capable of performing some specific tasks.
#NOTE: Once we create a function we can use that particular function for n number of times
'''1)Function without using argument, and without return values'''
'''Program to find sum of 2 numbers'''
#normal program
'''a=int(input(""))
b=int(input(""))
print(a+b)'''

#using function
'''def add():
    a=int(input("Enter the 1st number : "))
    b=int(input("Enter the 2nd number : "))
    print(a+b)
add()'''





'''Program to convert String to uppercase'''
#without using function
'''s=input("Enter the string : ")
out=''
for i in s :
    if 'a' <= i <= 'z':
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''

#using functions
'''def con_up():
    s=input("Enter the string : ")
    out=''
    for i in s:
        if 'a' <= i <= 'z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
con_up()'''





'''Program to count the number of occurence of a given character in a given string\n
without using count function'''

#without using function
'''s='Holaaa'
ch='a'

count=0
for i in s:
    if i==ch:
        count+=1
print(count)'''

#using function
'''def count_char():
    s='Collection'
    ch='l'

    count=0
    for i in s:
        if i==ch:
            count+=1
    print(count)
count_char()'''




#functions with argument, and without return values
'''WAP to extract strings from the list  which are palindrome
l=[10,'aba',17,'hai','nayan',3+4j]
out['aba', 'nayan']'''

'''def ex_pali(l):
    out=[]
    for i in l:
        if type(i)==str:
            if i==i[::-1]:
                out.append(i)
    print(out)
ex_pali([10,'aba',17,'hai','nayan',3+4j])'''



#OR


'''def ex_pali(l):
    out=[]
    for i in l:
        if type(i)==str:
            if i==i[::-1]:
                out.append(i)
    print(out)

l=eval(input("Enter the list values : "))

ex_pali(l)''' #function called here





'''Program to find greatest among 3 numbers'''
#using functions

'''def ga3(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("1st no is greater")
    elif n2>n3:
        print("2nd no is greater")
    else:
        print("3rd no is greater")
ga3(12,34,56)'''




'''Program to concatenate two list collections without using + operator.'''
#using function

'''def con_list(l1,l2):
    out=l1
    for i in l2:
        out.append(i)
    print(out)
con_list([10,20,30],[40,50,60])'''







#function without arguments and with return values.

'''def get():
    a=int(input("Enter the value : "))
    b=int(input("Enter the value : "))
    return a,b
m,n=get()
print(m,n)'''


'''Program to find the sum of integers present in a given set.'''
#s={10,7.9,3+4j,7}

'''def sum_int():
    s=eval(input("Enter a set value : "))
    sum=0
    for i in s:
        if type(i)==int:
            sum+=i
    return sum
print(sum_int())'''








#function with arguments with return values.
'''Program to print initial index of a char in a given string.
s='programming'
ch='m' '''

'''def get_in(s,ch):
    for i in range(0,len(s)):
        if s[i]==ch:
            return i
    return 'not present'


print(get_in('programming','m'))'''
            

#OR

'''def get_in(s,ch):
    for i in range(0,len(s)):
        if s[i]==ch:
            return i
    return 'not present'

s='programming'
ch='m'

print(get_in(s,ch))'''
            

#OR

'''def get_in(s,ch):
    for i in range(0,len(s)):
        if s[i]==ch:
            return i
    return 'not present'

s=input("Enter the string : ")
ch=input("Enter the character : ")

print(get_in(s,ch))'''
            

'''Program to map two list collections in the form of dictionary.
l1=['a','b','c']
l2=[10,20,30]
out={'a':10,'b':20,'c':30} '''

'''def map_li(l1,l2):
    out={}
    if len(l1)==len(l2):
        for i in range(0,len(l1)):
            out[l1[i]]=l2[i]
        return out
    else:
        return 'both list has different lengths'
print(map_li(['a','b','c'],[10,20,30]))'''


'''Program to extract all the negative numbers from the list.'''

'''def ex_neg(l):
    neg_list=[]
    for i in l:
        if type(i)==int and i<0:
            neg_list.append(i)
    return neg_list
print(ex_neg([12,3.4,-8,'hello',90,6+7j,-3]))'''


#OR
            
'''def ex_neg(l):
    neg_list=[]
    for i in l:
        if type(i)==int and i<0:
            neg_list.append(i)
    return neg_list

l=eval(input("Enter the list value : "))

print(ex_neg(l)) '''





#Global Variable
'''a=10
b=20
def sam():
    global a,b
    print(a,b)
    a=1000
    b=1234
    print(a+b)
print('before mod:',a,b)
sam()
print(b+10)
b=2000
print('after mod:',a,b) '''


#Local Variable
'''a,b=10,20
def outer():
    m=1000
    n=1234
    print(m,n)
    def inner():
        nonlocal n
        print(m,n)
        n=234
    inner()
    m=250
    print(m,n)
print(a,b)
outer()'''


'''def local_fun():
    a=10
    b=20
    print(a,b)
    print(a+b)
local_fun()
print(a,b)'''





#Passing Default arguments:
'''def reg(name,phno,email,altphno=None,altemail=''):
    print('name is:',name)
    print('phno is:',phno)
    print('email is:',email)
    print('altphno is:',altphno)
    print('altemail is:',altemail)
reg('A',9876543210,'a@gmail.com') '''


'''Program to add min 2 values and max 5 values
def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e
print(add(10,20))'''


'''Program to find product of min 3 number and max 4.
def prod(a,b,c,d=1):
    return a*b*c*d

print(prod(2,2,2))'''


'''Program to extract float numbers from tuple.
def ex_tuple(t,out=()):
    for i in t:
        if type(i)==float:
            out+=(i,)
    return out
print(ex_tuple((12,3.4,5,7.8,7,9)))'''


'''Program to find sum of individual digits in a given integer.
def sod(num,sum=0):
    while num>0:
        ld=num%10
        sum+=ld
        num=num//10
    return sum
print(sod(123))'''






