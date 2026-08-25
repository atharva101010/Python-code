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
