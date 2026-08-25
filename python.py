#simple if:
'''Program to check weather the given integer is even.
num=int(input("Enter the number : "))
if num % 2==0:
    print("Number is even")'''


'''Program to check weather the given string has exactly 5 characters.
str=input("Enter the string : ")
if len(str)==5:
    print("String has exactly 5 characters")'''


'''Program to check weather the given integer is greater than 200.
no=int(input("Enter the number : "))
if no>200:
       print("Given integer is greater than 200")'''


'''Program to find the square of the number only if it is mutiple of 3.
no=int(input("Enter the number : "))
if no % 3==0:
    print("The square of the no is : ", no ** 2)'''


'''Program to check weather the given integer is multiple of 5 and divisible by 3.
no=int(input("Enter the number : "))
if no % 5==0 and no % 3==0:
    print("The given integer is multiple of both 5 and 3")'''


'''Program to check weather the given integer is two digit number.
no=int(input("Enter the number : "))
if 10<= no <=99:
    print("The number is two digit")'''


'''Program to check weather the given character is uppercase.
char=input("Enter the character : ")
if 'A'<= char <='Z':
    print("The character is uppercase")'''



#if - else:
'''Program to check weather the given data is float or not.
no=eval(input("Enter the number : "))
if type(no)==float:
       print("The entered data is a float data")
else:
    print("The entered data is Not a float data")'''


'''Program to check weather the given string is palindrome or not.
str=input("Enter the string : ")
if str==str[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")'''


'''Program to check weather the given character is vowel or not.
char=input("Enter the character : ")
if char in "AEIOUaeiou":
    print("The character is a Vowel")
else:
    print("The character is not a Vowel")'''


'''Program to check weather the given data is single value or collection.
data=eval(input("Enter the data : "))
if type(data) in [int,float,complex,bool]:
    print("The entered data is Single value data type")
else:
    print("The entered data is a Collection data type")'''


'''Program to check weather the given integer is 3 digit number.
no=int(input("Enter the number : "))
if 100 <= no <= 999:
    print("It is a 3 digit number")
else:
    print("It is not a 3 digit number")'''


'''Program to check weather the given integer is positive or negative.
no=int(input("Enter the number : "))
if no >= 0:
    print("The entered Number is Positive")
else:
    print("The entered Number is Negative")'''


'''Program to check weather the given list has middle value.
list=eval(input("Enter the value in list : "))
if len(list) % 2==0:
    print("It has no middle value")
else:
    print("It has a middle value")'''


'''Consider a tuple consists of only two values and check weather that tuple is homogenous or heterogenous.
tup=eval(input("Enter the tuple value : "))
if type(tup[0])==type(tup[1]):
    print("The values in the tuple are Homogenous")
else:
    print("The value in tuple is Heterogenous")'''


'''For values more than 2.
t=eval(input("Enter the tuple values : "))

for i in t:
    if type(i)!=type(t[0]):
        print("The value in the tuple is Heterogenous")
        break
else:
    print("The value in the tuple is Homogenous")'''



#elif:
'''WAP to find the relation between two numbers.
n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
if n1>n2:
    print("1st number is greater")
elif n2>n1:
    print("2nd number is greater")
else:
    print("Both the numbers are equal")'''


'''Consider two coordinates i.e., x and y and check in which quadrant the data\points are present.
x=int(input("Enter the value for X co-ordinate : "))
y=int(input("Enter the value for Y co-ordinate : "))
if x>0 and y>0:
    print("The two co-ordinates lies in the 1st Quadrant")
elif x>0 and y<0:
    print("The two co-ordinates lies in the 2nd Quadrant")
elif x<0 and y<0:
    print("The two co-ordinates lies in the 3rd Quadrant")
else:
    print("The two co-ordinates lies in the 4th Quadrant")'''


'''Program to check weather the given character is uppercase or lowercase\or digit or special character.
char=input("Enter the character : ")
if 'A' <= char <= 'Z':
    print("The entered character is Upper case")
elif 'a' <= char <= 'z':
    print("The entered character is Lower case")
elif '0' <= char <= '9':
    print("The entered character is a Digit")
else:
    print("The entered character is a Special character")'''


'''Program to check weather the given integer is single digit or two digit\
or three digit or more than 3 digit.
n=int(input("Enter the number : "))

if 0 <= n <= 9:
    print("The number is single digit")
elif 10 <= n <= 99:
    print("The number is double digit")
elif 100 <= n <= 999:
    print("The number is three digit")
else:
    print("The number is more than 3 digit  ")'''


'''Program to find greater among 4 numbers.
n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
n3=int(input("Enter the 3rd number : "))
n4=int(input("Enter the 4th number : "))

if n1>n2 and n1>n3 and n1>n4:
       print("The 1st number is greater")
elif n2>n3 and n2>n4:
    print("The 2nd number is greater")
elif n3>n4:
    print("The 3rd number is greater")
else:
    print("The 4th number is greater")'''


'''Consider int input ,print FIZZ if number is divisible by 3 ,print BUZZ if number\
is divisible by 5,print FIZZBUZZ if number is divisible by both 3 and 5.
n=int(input("Enter the number : "))

if n % 3==0 and n % 5==0:
    print("FIZZBUZZ")
elif n % 3==0:
    print("FIZZ")
elif n % 5==0:
    print("BUZZ")
else:
    print("Not divisible by 3 and 5 both")'''



#Nested if:
'''WAP to check weather the given character vowel or consonant.
ch=input("Enter the character : ") #'@','1','#'.....
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    if ch in 'AEIOUaeiou':
        print("It is a Vowel")
    else:
        print("It is a consonant")
else:
    print("Other alphabet")'''

'''Program to login to instagram by entering the proper username and password.
oun='atharva10'
opw='1234'
un=input("Enter the username : ")
pw=input("Enter the password : ")
if un==oun:
    if pw==opw:
        print("Logged in!")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")'''

'''Program to check weather the given data is special symbol
data=eval(input("Enter the data : "))
if type(data)==str:
    if len(data)==1:
        if not('A'<=data<='Z' or 'a'<=data<='z' or '0'<=data<='9'):
            print("Special data")
        else:
            print("Not a special character")
    else:
        print("Length is not 1")
else:
    print("Not a string data")'''

#this similar code can also work as. While entering the input specify it inside '' 
'''char=eval(input("Enter the character : "))

if len(char)==1:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9':
        print("Not a special character")
    else:
        print("Special character")
else:
    print("Please enter a single character")'''


'''WAP to print reverse of the string only if it is starting with uppercase aplhabet and ending with digit
s=input("Enter the string : ")
if 'A'<=s[0]<='Z':
    if '0'<=s[-1]<='9':
        print("Reverse string is : ",s[::-1])
    else:
        print("The ending character is not a digit")
else:
    print("The starting aplhabet is not a Upper case")'''


'''WAP to find the greatest among 3 numbers using nested if
no1=int(input("Enter the 1st no : "))
no2=int(input("Enter the 2nd no : "))
no3=int(input("Enter the 3rd no : "))
if no1 > no2:
        if no1 > no3:
              print("1st no is greater")
        else:
            print("C is greater")
else:
    if no2 > no3:
         print("B is greater")
    else:
        print("C is greater")'''

#Assignment Questions.
'''1. WAP to find smallest among 5 numbers using elif.
2. WAP to find greatest among 4 numbers using nested if.
3. WAP to find lesser among 5 numbers using nested if.
4. WAP to find the second greater among 4 numbers using all conditional statements.'''

'''1. Program:
a=int(input("Enter the 1st no : "))
b=int(input("Enter the 2nd no : "))
c=int(input("Enter the 3rd no : "))
d=int(input("Enter the 4th no : "))
e=int(input("Enter the 5th no : "))

if a<b and a<c and a<d and a<e:
    print("1st no is smaller")
elif b<c and b<d and b<e:
    print("2nd no is smaller")
elif c<d and c<e:
    print("3rd no is smaller")
elif d<e:
    print("4th no is smaller")
else:
    print("5th no is smaller")'''


'''2. Program:
a=int(input("Enter the 1st no : "))
b=int(input("Enter the 2nd no : "))
c=int(input("Enter the 3rd no : "))
d=int(input("Enter the 4th no : "))
if a>b:
    if a>c:
        if a>d:
            print("1st is greater")
        else:
            print("4th is greater")
    else:
        if c>d:
            print("3rd is greater")
        else:
            print("4th is greater")
else:
    if b>c:
        if b>d:
            print("2nd is greater")
        else:
            print("4th is greater")
    else:
        if c>d:
            print("3rd is greater")
        else:
            print("4th is greater")'''


'''3. Program :
a=int(input("Enter the 1st no : "))
b=int(input("Enter the 2nd no : "))
c=int(input("Enter the 3rd no : "))
d=int(input("Enter the 4th no : "))
e=int(input("Enter the 5th no : "))

if a<b:
    if a<c:
        if a<d:
            if a<e:
                print("1st is smaller")
            else:
                print("5th is smaller")
        else:
            if d<e:
                print("4th is smaller")
            else:
                print("5th is smaller")
    else:
        if c<d:
            if c<e:
                print("3rd is smaller")
            else:
                print("5th is smaller")
        else:
            if d<e:
                print("4th is smaller")
            else:
                print("5th is smaller")
else:
    if b<c:
        if b<d:
            if b<e:
                print("2nd is smaller")
            else:
                print("5th is smaller")
        else:
            if d<e:
                print("4th is smaller")
            else:
                print("5th is smaller")
    else:
        if c<d:
            if c<e:
                print("3rd is smaller")
            else:
                print("5th is smaller")
        else:
            if d<e:
                print("4th is smaller")
            else:
                print("5th is smaller")'''


'''4.Program
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))

if a >= b and a >= c and a >= d:
    if b >= c and b >= d:
        print("Second greatest number is :", b)
    elif c >= b and c >= d:
        print("Second greatest number is :", c)
    else:
        print("Second greatest number is :", d)

elif b >= a and b >= c and b >= d:
    if a >= c and a >= d:
        print("Second greatest number is :", a)
    elif c >= a and c >= d:
        print("Second greatest number is :", c)
    else:
        print("Second greatest number is :", d)

elif c >= a and c >= b and c >= d:
    if a >= b and a >= d:
        print("Second greatest number is :", a)
    elif b >= a and b >= d:
        print("Second greatest number is :", b)
    else:
        print("Second greatest number is :", d)
        
else:
    if a >= b and a >= c:
        print("Second greatest number is :", a)
    elif b >= a and b >= c:
        print("Second greatest number is :", b)
    else:
        print("Second greatest number is :", c)'''













#while loop
'''Program to print python for 5 times.
i=1
while i<=5:
    print("Python")
    i+=1'''


'''WAP to print n natural numbers.
n=int(input("Enter the value for n : "))
i=1
while i <= n:
    print(i)
    i+=1'''


'''WAP to print all the even numbers between 1 to 50.
i=2
while i <= 50:
    print(i)
    i+=2
We can also use i=1
i=1
while i<=50:
    if i % 2==0:
        print(i)
    i+=1'''


'''WAP to print all the numbers which are multiple of 5 between 1 to n.
n=int(input("Enter the value of n : "))
i=1
while i<=n:
    if i % 5==0:
        print(i)
    i+=1'''
    

'''WAP to print the multiplication table for n.
n=2
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
.
.
.
.
2 X 10 = 20
n=int(input("Enter the value of n : "))
i=1
while i<=10:
    print(n, 'X', i, '=', n*i)
    i+=1'''


'''WAP to print the numbers from n to 1.
EX:n=10-->10,9,8,7,6,5,4,3,2,1.
5-->5,4,3,2,1
n=int(input("Enter the value of n : "))
i=n
while i>0:
    print(i,end=' ')#end will print all the values in single line.
    i-=1'''


'''WAP to reverse the given number without using typecasting and slicing
n=int(input("Enter the number : "))
rev=0
while n!=0:
    ld=n%10
    rev=rev*10+ld
    n=n//10
print(rev)'''


'''WAP to find the sum of individual numbers.
n=int(input("Enter the number : "))
sum=0
while n!=0:
    ld=n%10
    sum+=ld
    n=n//10
print(sum)'''


'''Program to find the product of even individual digits.
n=int(input("Enter the number : "))
prod=1
while n!=0:
    ld=n%10
    if ld % 2==0:
        prod = prod*ld
    n=n//10
print(prod)'''


'''Program to find the sum of n natural numbers.
n=int(input("Enter the number : "))
res=0
i=1
while i<=n:
    res+=i
    i+=1
print(res)'''

        
'''Program to find the factorial of a given integer or to find the product of n natural numbers.'''

#factorial
'''n=int(input("Enter the number : "))
prod=1
i=n
while i>0:
    prod*=i
    i-=1
print(prod)'''

#Product
'''n=int(input("Enter the number : "))
prod=1
i=1
while i<=n:
    prod*=i
    i+=1
print(prod)'''


'''Program to print every character from the given string.
s=input("Enter the string : ")
i=0
while i<len(s):
    print(s[i])
    i+=1'''


'''Program to extract lower case characters from the given string.
s=input("Enter the string : ")
res=''
i=0
while i<len(s):
    if 'a' <= s[i] <= 'z':
        res+=s[i]
    i+=1
print(res)'''    


'''Program to extract integers from the given list.
l=eval(input("Enter a list : "))
out=[]
i=0
while i<len(l):
    if type(l[i])==int:
        out+=[l[i]]
    i+=1
print(out)'''


'''Program to find the product of all the float numbers at the odd index in a given tuple
t=eval(input("Enter the tuple : "))
prod=1
i=0
while i<len(t):
    if type(t[i])==float and i%2!=0:
        prod*=t[i]
    i+=1
print(prod)'''


'''Program to convert all the lowercase characters from string to upper case characters.
s=input("Enter the string : ")
out=''
i=0
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    i+=1
print(out)'''


'''Program to convert upper to lower and lower to upper characters in given string.
s=input("Enter the string : ")
out=''
i=0
while i<len(s):
    if 'A' <= s[i] <= 'Z':
        out+=chr(ord(s[i])+32)
    elif 'a' <= s[i] <= 'z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    i+=1
print(out)'''


#Assignment Questions:
'''1.Program to extract uppercase characters from string.
2.Program to extract uppercase,lowercase,digits and special characters separately into four different output strings.
for ex:- out1=all upper case characters
out2= all lower case characters
out3= all digits value
out4= all special characters
3.Program to find the sum of integers in a given list.'''

'''1.Program
s = input("Enter the string : ")
out = ''
i = 0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        out += s[i]
    i += 1

print(out)'''

'''2.Program
s = input("Enter the string : ")
upper = ''
lower = ''
digit = ''
special = ''
i = 0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        upper += s[i]
    elif 'a' <= s[i] <= 'z':
        lower += s[i]
    elif '0' <= s[i] <= '9':
        digit += s[i]
    else:
        special += s[i]
    i += 1
print("Uppercase :", upper)
print("Lowercase :", lower)
print("Digits :", digit)
print("Special Characters :", special)'''


'''3.Program
l = eval(input("Enter a list : "))

sum = 0
i = 0

while i < len(l):
    if type(l[i]) == int:
        sum += l[i]
    i += 1

print(sum)'''




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



#Pattern programming
''' * * * 
for i in range(1,4):
    print('*',end = ' ')'''


''' * * *
    * * *
    * * * 
for i in range(1,4):
    for j in range(1,4):
        print('*', end = ' ')
    print()'''


''' * * *
    * * *
    * * *
    * * *
    * * * 
for i in range(1,6):
    for j in range(1,4):
        print('*', end = ' ')
    print()'''



''' * * * * *
    * * * * * 
for i in range(1,3): #no of rows
    for j in range(1,6): #no of columns
        print('*', end = ' ')
    print()'''


''' *
     *
      *
       *
        * 
n=int(input("Enter the val for n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()'''


''' @
    * @
    * * @
    * * * @
    * * * * @ 

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('@', end = ' ')
        elif i>j:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()'''


''' # # # # $
    # # # $ &
    # # $ & &
    # $ & & &
    $ & & & &
    
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('$', end = ' ')
        elif i+j>n+1:
            print('&', end = ' ')
        else:
            print('#', end = ' ')
    print()'''


'''1 0 0 0 0
   0 1 0 0 0
   0 0 1 0 0
   0 0 0 1 0
   0 0 0 0 1 

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('1', end = ' ')
        else:
            print('0', end = ' ')
    print()'''


''' * * * * *
    *       *
    *       *
    *       *
    * * * * * 

n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()'''



''' *
    * *
    * * *
    * * * *
    * * * * * 

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()'''


''' *       *
      *   *
        *
      *   *
    *       * 
n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()'''

'''           *
              *
         *  * * *  *
              *
              * 

n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n//2+1 or j==n//2+1:
            print("*", end = ' ')
        else:
            print(' ', end = ' ')
    print()'''


'''        * * * * * * * * *
           * *     *     * *
           *   *   *   *   *
           *     * * *     *
           * * * * * * * * *           
           *     * * *     *
           *   *   *   *   *
           * *     *     * *
           * * * * * * * * *           '

n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1 or i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()'''


'''        *
         *   *
       *       *
     *           *
   * * * * * * * * *   

n=5
c=9
for i in range(1,n+1):
    for j in range(1,c+1):
        if i==n or i+j==n+1 or j-i==n-1:
            print("*", end = ' ')
        else:
            print(' ', end = ' ')
    print()'''


''' *       
   * * 
  * * * 
 * * * * 
* * * * * 

n=5
for i in range(1,n+1):
    for s in range(1,n+1-i):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end=' ')
    print()'''


''' 1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5 

n=int(input("Enter the value for n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end = ' ')
    print()'''


''' 1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5 

n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end = ' ')
    print()'''


''' 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5 

n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(j, end = ' ')
        else:
            print(' ', end = ' ')
    print()'''

#or
'''n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    k=1
    for j in range(1,n+1):
        if i>=j:
            print(k,end= ' ')
        else:
            print(' ',end= ' ')
    print()'''
        

'''           5
            5 4
          5 4 3
        5 4 3 2
      5 4 3 2 1 

n=int(input("Enter the value of n : "))
for i in range(1,n+1):
    k=5
    for j in range(1,n+1):
        if i+j>=n+1:
            print(k,end =' ')
            k-=1
        else:
            print(' ',end= ' ')
    print()'''


''' A B C D E
      A B C D
        A B C
          A B
            A 

n=int(input("Eneter the value of n : "))
for i in range(1,n+1):
    k=ord('A') #65
    for j in range(1,n+1):
        if i<=j:
            print(chr(k),end= ' ')
            k+=1
        else:
            print(' ',end= ' ')
    print()'''


''' 1              34
    2 3            35 36
    3 4 5          36 37 38
    4 5 6 7        37 38 39 40
    5 6 7 8 9      38 39 40 41 42  '''

#use k=sv+1-1

'''n=5
for i in range(1,n+1):
    k=1+i-1
    for j in range(1,n+1):
        if i>=j:
            print(k,end= ' ')
            k+=1
        else:
            print(' ',end= ' ')
    print()'''
#or
'''n=5
for i in range(1,n+1):
    k=34+i-1
    for j in range(1,n+1):
        if i>=j:
            print(k,end= ' ')
            k+=1
        else:
            print(' ',end= ' ')
    print()'''


''' L M N O P
      M N O P
        N O P
          O P
            P 

n=5
for i in range(1,n+1):
    k=ord('L')+i-1
    for j in range(1,n+1):
        if i<=j:
            print(chr(k),end= ' ')
            k+=1
        else:
            print(' ',end= ' ')
    print()'''


''' 1
    4  9
    3  4  5
    16 25 36
    5   6  7  8  9'''

'''n = 5
for i in range(1,n+1):
    for j in range(i,2*i):
        if i%2 == 0:
            print(j*j,end=' ')
        else:
            print(j,end=' ')
    print()'''

#or
'''n=5
for i in range(1,n+1):
    k=1+i-1
    for j in range(1,n+1):
        if i>=j:
            if i%2 == 0:
                print(k**2,end= ' ')
            else:
                print(k,end= ' ')
            k+=1
        else:
            print(' ',end= ' ')
    print()'''
        
        
#termination statement
'''WAP to check whether a number is prime or not.'''
#without using break.
'''n=int(input("Enter the number : "))
count=0
for i in range(1,n+1):
      if n%i==0:
             count+=1
if count==2:
      print("Prime")
else:
    print("Not prime")'''
#using break
'''
n=int(input("Enter the number : "))
count=0
for i in range(2,n):
    if n%i==0:
       print("Not prime")
       break
else:
    print("Prime number")'''


''' Program to print the initial index of a given character present in a given string. 
ch=input("Enter the character : ")
s=input("Enter the string : ")
for i in range(0,len(s)):
    if s[i]==ch:
        print(i)
        break
else:
    print("Char is not present")'''


'''WAP to check whether the given string has only lower case characters in it or not.
s=input("Enter the string : ")
for i in s:
    if not('a' <=i<= 'z'):
        print("It has no lowercase characters")
        break
else:
    print("Only lowercase characters")'''


#continue
'''for i in range(0,11):
    if i==3:
        break
    print(i)'''

'''for i in range(0,11):
    if i==3:
        continue
    print(i)'''


'''for i in range(1,11):
    if i==6 or i==2:
        continue
    print(i)'''


'''Program to extract all the integers from the given list.
l=eval(input("Enter the list : "))
out=[]
for i in l:
    if type(i)!=int:
        continue
    out.append(i)
print(out)'''


'''Program to extract all the special characters from the given string.
s=input("Enter the string : ")
res=''
for i in s:
    if 'A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9':
        continue
    res+=i
print(res)'''


'''Program to print 1 to 10 numbers using while loop by skipping 3 and 8 iteration.
i=1
while i<=10:
    if i==3 or i==8:
        i+=1
        continue
    print(i)
    i+=1'''
        

#pass = It is a keyword which is used to make any empty block as "Valid Block".



























#Assignment No-1:
'''1) Variables
Q1 Store your name and print it
name='Atharva_Patil'
print(name)'''

'''Q2 Store two numbers and print their sum
n1=10
n2=7
print("The sum of two numbers is :",n1+n2)'''

'''Q3 Find the area of Rectangle
l=int(input("Enter the length : "))
w=int(input("Enter the width : "))
print("The area of rectangle is :",l*w)'''

'''2) Data types
Q1) Display the data type of different variables
n=12
f=67.98
b=True
s='Holaa'
l=['Hii','guys']
t=('hola','amigo')
st={1,2,3,4}
d={'Atharva':10,'Barca':100}
print(type(n))
print(type(f))
print(type(b))
print(type(s))
print(type(l))
print(type(t))
print(type(st))
print(type(d)) '''

'''Q2) Convert an int to float 
n=189
f=float(n)

print(type(f))'''

'''Q3) Convert an str to int
s='1234'
n=int(s)

print(type(n))'''

'''3) Input from user
Q1) Read a name and print a greeting
n=input("Enter your name : ")
print("Hello",n)'''

'''Q2) Read two numbers and print their sum
n1=int(input("Enter the 1st number :"))
n2=int(input("Enter the 2nd number :"))
sum=n1+n2
print("The sum of two numbers is :",sum)'''

'''Q3) Read the radius and find the area of the circle
r=int(input("Enter the radius of circle : "))
radius=3.14*r*r
print("The area of circle is :", radius)'''

'''4) Operators
Q1) Find quotient and remainder
n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
quotient=n1 // n2
remainder=n1 % n2
print("The quotient is :", quotient)
print("The remainder is : ", remainder)'''

'''Q2) Check whether one number is greater than another
n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
if n1>n2:
    print("1st number is greater")
else:
    print("2nd number is greater")'''

'''Q3) Check whether the number is divisible by 5
num=int(input("Enter the number : "))
if num % 5==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")'''

'''5) Conditional statements(if)
Q1) Find the greater of two number
n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
if n1 > n2:
    print("1st number is greater than 2nd")
else:
    print("2nd number is greater than 1st")'''

'''Q2) Find the greatest of three numbers
n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
n3=int(input("Enter the 3rd number : "))
if n1 > n2 and n1 > n3:
    print("1st number is greater")
elif n2 > n3:
    print("2nd number is greater")
else:
    print("3rd number is greater")'''
    
'''Q3) Check whether a person is eligible to vote
age=int(input("Enter your age : "))
if age>=18:
    print("You are eligible to vote")
else:
    print("Not eligible to vote")'''

'''6) if-else
Q1) Check whether a year is leap year
year=int(input("Enter the year : "))
if year % 4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")'''

'''Q2) Check whether a number is multiple of 10
num=int(input("Enter the number : "))
if num % 10==0:
    print("The given number is multiple of 10")
else:
    print("The given number is not a multiple of 10")'''

'''Q3) Check whether a student passed (marks>=35)
marks=int(input("Enter the marks : "))
if marks>=35:
    print("Student passed")
else:
    print("Student failed")'''

'''7) Nested if
Q1) Calculate grade based on marks
marks=int(input("Enter the marks : "))
if marks >= 55:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 65:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Failed")'''

'''Q2) Check whether a person is eligible for a driving license(age and eyesight condition)
age=int(input("Enter the age : "))
eyesight=input("Is your eyesight Good? (Yes or NO)? : ")
if age>=18:
    if eyesight == "yes":
        print("Eligible for driving license")
    else:
        print("Not eligible due to eyesight")
else:
    print("Under age")'''

'''elif
Q1) Display the day of the week using number(1-7)
day=int(input("Enter the day between (1-7): "))
if day == 1:
    print("Monday")
elif day ==2:
    print("Tuesday")
elif day ==3:
    print("Wednesday")
elif day ==4:
    print("Thursday")
elif day ==5:
    print("Friday")
elif day ==6:
    print("Saturday")
else:
    print("Sunday")'''

'''Q2) Asign grades(A,B,C,D,F)
marks=int(input("Enter the marks : "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 55:
    print("Grade D")
else:
    print("Grade F")'''

'''9) For loop
Q1) Print odd numbers from 1 to 50
for i in range(1,50):
    if i%2!=0:
        print(i)'''

'''Q2) Print the multiplication table of given number

n=int(input("Enter the number : "))
for i in range(1,11):
    print(n, 'X', i, '=', n*i)'''

'''10) While loop
Q1) Find the sum of first n natural numbers
n=int(input("Enter the number : "))
i=1
result=0
while i<=n:
    result+=i
    i+=1
print(result)'''
    
'''Q2) Reverse a number
num=int(input("Enter the number : "))
rev=0
while num!=0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)'''

'''Q3) Count the digit in number
n=int(input("Enter the number : "))
count=0
while n!=0:
    n=n//10
    count+=1
print(count)'''

'''11) Pattern 
Q1) Print numbers in triangle pattern
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

'''Q2) Print an inverted triangle
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

'''12) Nested loops
Q1) Print a multiplication table from 1 to 5
for i in range(1, 6):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()'''

'''Q2) Print a recatngle using stars
rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(columns):
        print("*",end=" ")
    print()'''

'''13) Termination statement
Q1) Keep asking for input until the user enters 0
while True:
    n=int(input("Enter a number: "))
    if n==0:
        break
    print("You entered:", n)'''

'''Q2) Find the first number divisible by both 7 and 9
for i in range(1, 1000):
    if i % 7 == 0 and i % 9 == 0:
        print("First number:", i)
        break'''

'''Q3) Stop printing numbers when a negative number is encountered
while True:
    n = int(input("Enter a number: "))
    if n < 0:
        break
    print(n)'''

'''Continue
Q1) Print numbers from 1 to 20, skipping multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)'''

'''Q2) Print only odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)'''

'''Q3) Skip vowels while printing characters
s = input("Enter the string: ")
for i in s:
    if i in 'aeiouAEIOU':
        continue
    print(i)'''

'''Pass
Q1) Write an empty if block using pass
n=int(input("Enter the number"))
if n > 5:
    pass
else:
    print("Lesser than 5")'''

'''Q2) Write an empty for loop using pass
for i in range(1, 6):
    pass'''








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






#Recursion.
'''Program to find factorial of a given number.
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(5)) '''


'''Program to find sum of n natural numbers.
def sum_int(n):
    if n==1:
        return 1
    return n+sum_int(n-1)
print(sum_int(4)) '''


'''Program to print :
     3 2 1 2 3  
def sam(n):
    print(n,end=' ')
    if n==1:
        return
    sam(n-1)
    print(n,end=' ')
sam(10) '''


'''Program to extract lowercase characters from the given string.'''
#using while loop
'''s=input("Enter the string : ")
out=''
i=0
while i<len(s):
    if 'a' <= s[i] <= 'z':
        out+=s[i]
    i+=1
print(out) '''

#using Recursion
'''def ex_low(s,out='',i=0):
    if i >= len(s):
        return out
    if 'a' <= s[i] <= 'z':
        out+=s[i]
    return ex_low(s,out,i+1)
print(ex_low('RecURsiON')) '''


'''Program to find the sum of all the integers present in a given list.
l=[10,12,3.4,[4,9+9+4j]] 

def sum_int(l,sum=0,i=0):
    if i >= len(l):
        return sum
    if type(l[i]) == int:
        sum+=l[i]
    elif type(l[i]) in[list,set,tuple]:
        sum+=sum_int(list(l[i]))
    return sum_int(l,sum,i+1)
print(sum_int([10,12,3.4,[4,9+9+4j]])) '''


'''Program to get the following output.
l=['hai',56,7+8j,8.7,'data']
out=['iahhai',56,7+8j,45,8.7,'atddata'] '''

#using while loop
'''l=eval(input("Enter a list : "))
out=[]
i=0
while i<len(l):
    if type(l[i])==str:
        out.append(l[i][::-1]+l[i])
    else:
        out.append(l[i])
    i+=1
print(out) '''

#using recursion
'''def get(l,out=[],i=0):
    if i >= len(l):
        return out
    if type(l[i])==str:
        out.append(l[i][::-1]+l[i])
    else:
        out.append(l[i])
    return get(l,out,i+1)
print(get(['hai',56,7+8j,8.7,'data'])) '''









#Extract integers from the given list
#using While loop
'''l=eval(input("Enter a list : "))
out=[]
i=0
while i<len(l):
    if type(l[i])==int:
        out+=[l[i]]
    i+=1
print(out)'''

#using recursion
'''l=eval(input("Enter a list : "))

def get(l,out=[],i=0):
    if i >= len(l):
        return out
    if type(l[i])==int:
        out.append(l[i])
    return get(l,out,i+1)

print(get([10,2.5,'hai',20,7+8j,30]))'''



# Product of all float numbers at odd index in a tuple
#using while loop
'''t=eval(input("Enter the tuple : "))
prod=1
i=0
while i<len(t):
    if type(t[i])==float and i%2!=0:
        prod*=t[i]
    i+=1
print(prod)'''

#using recursion
'''t=eval(input("Enter the tuple : "))

def get(t,prod=1,i=0):
    if i >= len(t):
        return prod
    if type(t[i])==float and i%2!=0:
        prod*=t[i]
    return get(t,prod,i+1)

print(get((10,2.5,5,3.5,7,4.5)))'''




#Convert lowercase characters to uppercase
#using while loop
'''s=input("Enter the string : ")
out=''
i=0
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    i+=1
print(out)'''

#using recursion
'''s=input("Enter the string : ")

def get(s,out='',i=0):
    if i >= len(s):
        return out
    if 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    return get(s,out,i+1)

print(get('Hello World'))'''

#Convert uppercase to lowercase and lowercase to uppercase
#using while loop
'''s=input("Enter the string : ")
out=''
i=0
while i<len(s):
    if 'A' <= s[i] <= 'Z':
        out+=chr(ord(s[i])+32)
    elif 'a' <= s[i] <= 'z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    i+=1
print(out) '''

#using recursion
'''s=input("Enter the string : ")

def get(s,out='',i=0):
    if i >= len(s):
        return out
    if 'A'<=s[i]<='Z':
        out+=chr(ord(s[i])+32)
    elif 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    return get(s,out,i+1)

print(get('Hello WORLD 123'))'''














#Functions Assignment
'''1.Create a function calculate_area() that calculates the area of a circle, rectangle, or triangle based on a parameter specifying the shape.
def calculate_area(shape):
    if shape == 'circle':
        r=float(input("Enter the radius of circle : "))
        return 3.12*r*r
    elif shape == 'rectangle':
        length=float(input("Enter the value of length : "))
        width=float(input("Enter the value of width : "))
        return length*width
    elif shape == 'triangle':
        base=float(input("Enter the value of base : "))
        height=float(input("Enter the value of height : "))
        return 0.5*base*height
    else:
        return 'Invalid shape'
print(calculate_area('circle')) '''


'''2. Write a function that accepts a number and returns all its factors. Example: 12 → [1, 2, 3, 4, 6, 12].
def factors(num):
    result = []
    for i in range(1,num+1):
        if num % i ==0:
            result.append(i)
    return result
print(factors(12)) '''


'''3. Create a function to determine whether a number is prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True
print(is_prime(7)) '''


'''4. Write a function that accepts two lists and returns the common elements between them.
Example: [1,2,3,4] and [3,4,5,6] → [3,4]  

def common_elements(list1, list2):
    common=[]
    for i in list1:
        if i in list2 and i not in common:
            common.append(i)
    return common
print(common_elements([1,2,3,4],[3,4,5,6])) '''


'''5.Create a function that accepts a sentence and returns the number of words in it.
def count_words(sentence):
    words=sentence.split()
    return len(words)
print(count_words('Hello guys')) '''


'''6.Write a function that accepts a list of strings and returns the longest string.
def longest_string(strings):
    longest=strings[0]
    for i in strings:
        if len(i) > len(longest):
            longest=i
    return longest
print(longest_string(['cat', 'elephant', 'dog', 'tiger'])) '''


'''7.Write a function using *args that accepts any number of numbers and returns their average.
def average(*args):
    return sum(args)/len(args)
print(average(10,20,30,40))  '''


'''8.Create a function using **kwargs that accepts student information such as name, age, course, and marks and displays the information.
def student_info(**kwargs):
    for x in kwargs:
        print(x, ":", kwargs[x])
student_info(name='Atharva', age=21, course="IT", marks=85) '''


'''9.  Write a function that accepts any number of arguments and separates them into even and odd numbers.
Example: Input: 10, 15, 20, 25, 30
Output:
Even: [10, 20, 30]
Odd: [15, 25]

def even_odd(*args):
    even=[]
    odd=[]
    for num in args:
        if num % 2 ==0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
even,odd=even_odd(10,15,20,25,30)
print('Even:',even)
print('Odd:',odd) '''


'''10. Create a function with a default parameter.
Write a function greet() where the name is optional. If no name is provided, it should display "Hello, Guest!".

def greet(name='Guest'):
    print('Hello,',name)
greet()
greet('Atharva') '''


'''11.  Write a function that demonstrates the difference between a local variable and a global variable.
x=10
def display():
    y=20
    print('Global variable : ',x)
    print('Local variable : ',y)
display() '''


'''12.Write a recursive function to calculate the sum of numbers from 1 to n.
Example: n = 5 → 15 
def sum_n(n):
     if n == 0:
         return 0
     else:
        return n + sum_n(n-1)
print(sum_n(5)) '''


'''13.Write a function that accepts a list of numbers and returns a dictionary containing:
1)Maximum value
2)Minimum value
3)Average
4)Total number of elements 

def number_data(numbers):
    result = {
        "Maximum":max(numbers),
        "Minimum":min(numbers),
        "Average":sum(numbers)/len(numbers),
        "Total Elements":len(numbers)
    }
    return result
print(number_data([10, 20, 30, 40, 50])) '''


'''14.Create a function to remove duplicate elements from a list without using set().
def remove_duplicate(numbers):
    result=[]
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
print(remove_duplicate([1,2,2,3,4,4,5])) '''


'''15.Write a function that accepts a sentence and returns a dictionary containing the frequency of each word.
def words_frequency(sentence):
    words=sentence.lower().split()
    frequency={}
    for i in words:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency
print(words_frequency('Python is easy and python is powerful')) '''


'''16.Create a function that accepts a list of numbers and returns the numbers that occur more than once.
def duplicate_numbers(numbers):
    duplicates = []
    for i in numbers:
        if numbers.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
print(duplicate_numbers([1, 2, 3, 2, 4, 5, 3, 6])) '''


'''17.Write a function that accepts a string and returns the first non-repeating character.
Example:
Input: "swiss"
Output: "w" 
def first_non_repeating(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return None
print(first_non_repeating("swiss")) '''


'''18.Write a function greet(name="Guest") that prints a greeting. Test it both with and without an argument.
def greet(name="Guest"):
    print("Hello,",name + "!")
greet()
greet("Atharva") '''


'''19.Write a function calculate_power(number, power=2) that calculates the power of a number.
Example:
calculate_power(5) → 25
calculate_power(5, 3) → 125 

def calculate_power(number, power=2):
    return number ** power
print(calculate_power(5))
print(calculate_power(5,3)) '''


'''20.Write a function student(name, course="Biotechnology") that displays the student's name and course.
def student(name,course="Biotechnology"):
    print("Name:",name)
    print("Course:",course)
student("Leo")
student("Atharva", "Computer Science") '''


'''21.Create a function student_details(name, age, course) and call it using keyword arguments.
def student_details(name, age, course):
    print("Name:",name)
    print("Age:",age)
    print("Course:",course)
student_details(name="Atharva", age=21, course="Information Technology") '''


'''22.Create a function employee(name, department, salary) and call it by providing the arguments in a diAerent order using keyword arguments.
def employee(name, department, salary):
    print("Name:",name)
    print("Department:",department)
    print("Salary:",salary)
employee(salary=50000, name="Atharva", department="IT") '''


'''23.Write a function product(name, price, quantity) that calculates and returns the total price. Call the function using keyword arguments.
def product(name, price, quantity):
    total = price * quantity
    print("Product:",name)
    print("Total Price:",total)
product(quantity=3, name="Notebook", price=50) '''
