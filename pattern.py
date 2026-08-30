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


