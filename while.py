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
