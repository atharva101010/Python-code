#OOP example

'''class Demo:
    pass          # we have skipped properties here 
ob1 = Demo()
ob2 = Demo() '''



'''class Demo:
    pass          # we have skipped properties here 
ob1=Demo()
ob2=Demo()
print(type(ob1))
print(type(ob2))   '''

#Accessing properties
''' 
class A:
    a=10
    b=20
o1=A()
o2=A()
o3=A()

print(A.a,A.b) #Accessing properties from class. Syntax : classname.propertyname
print(o1.a,o1.b)#Accessing properties from object. Syntax : objectname.propertyname
print(o2.a,o2.b)
print(o3.a,o3.b)  '''




'''class Bank:
    bname='SBI'
    loc='Mumbai'
c1=Bank()
c2=Bank()

print('Before Modification : ')
print(Bank.bname,Bank.loc) #Accessing properties from class. Syntax : classname.propertyname
print(c1.bname,c1.loc) #Accessing properties from class. Syntax : objectname.propertyname
print(c2.bname,c2.loc) 

#Syntax to modify class values :
Bank.loc='Banglore' #Syntax : cname.propertyname=new_value
print('After Modification in Class : ')
print(Bank.bname,Bank.loc)
print(c1.bname,c1.loc)
print(c2.bname,c2.loc)

#Syntax to modify class values :
c1.loc='Mumbai' #Syntax : objname.propertyname=new_value
print('After Modification in Object : ')
print(Bank.bname,Bank.loc)
print(c1.bname,c1.loc)
print(c2.bname,c2.loc) '''





#  __init__ Method
'''
Constructor/__init__/initialisation method:
1) It is a method which is used to initialize the members of object.
2) Name should be __init__ .
3) We can pass arguments either in function call/in class call/in object creation only it there exists __inti__ method .
4) According to industrial standard rule we need to use "Self" to store the address of object.
5) And "Self" should be the 1st argument
'''

#Syntax:
'''     class cname:


         def __init__(Self,var1,var2,var3,.....varn):
             self.var1=var1
             self.var2=var2
             self.var3=var3



             self.varn=varn
obj=cname(val1,val2,val3,......valn)    '''

'''Create a class called Bank with 4 class members, 10 objects consists of 7\
objects members each.

class Bank:
    bname='ICICI'
    loc='Mumbai'
    helpline=801234
    website='www.icici.com'

    def __init__(self,name,phno,addr,email): # __init__ acts as a constructor
        self.name=name
        self.phno=phno
        self.addr=addr
        self.email=email

#now to declare values for c1
c1=Bank('A',9876543210,'Marg','a@gmail.com')

#now to declare values for c2
c2=Bank('B',98745632120,'Mandir','b@gmail.com')

#now to declare values for c3
c3=Bank('C',686748096,'Bapat','c@gmail.com')

print(c1.name,c1.phno,c1.addr,c1.email)
print(c2.name,c2.phno,c2.addr,c2.email)
print(c3.name,c3.phno,c3.addr,c3.email) '''


'''Program to create a class called "Company" with 3 class members and 1 object with 4 object members

class Company:
    cname='TCS'
    loc='Mumbai'
    CEO='Kritivasan'
    def __init__(self,empname,eid,sal,desig):
        self.empname=empname
        self.eid=eid
        self.sal=sal
        self.desig=desig

e1=Company('Atharva',100,3700000,'Associate_DevOps_Engineer')
print(e1.empname,e1.eid,e1.sal,e1.desig)   '''




# Object Method:
'''
It is a method which is used to access and modfiy the members/properties of object.
And for all the object method it is compulsory to pass "Self"
'''

'''class Company:
    cname='ABC'
    loc='Mumbai'
    login_hours='9 hours'
    def __init__(self,name,eid,sal,desig,email):
        self.name=name
        self.eid=eid
        self.sal=sal
        self.desig=desig
        self.email=email
    def disp(self):
        print(self.name,self.eid,self.sal,self.desig,self.email)
    def ch_email(self,new):
        self.email=new
    def ch_sal(self,new):
        self.sal=new
    def ch_desig(self,new):
        self.desig=new
emp1=Company('A','abc12',76000,'SE','a@gmail.com')
emp2=Company('B','abc13',65000,'ASE','b@abc.com')
Company.disp(emp1)
Company.disp(emp2)
Company.ch_email(emp1,'a@abc.in')
Company.ch_sal(emp1,98000)
Company.ch_desig(emp1,'Developer')
Company.disp(emp1)
Company.ch_email(emp2,'b@gmail.com')
Company.ch_sal(emp2,75000)
Company.ch_desig(emp2,'SSE')
emp1.ch_desig('SSE')
emp2.ch_desig('DevOps')    '''




#Assignment:
'''Program to create a class called school with 5 object methods.

class school:
    sname='Antonio De Souza High School'
    loc='Mumbai'
    time='8 hrs'
    def __init__(self,name,sid,sclass,div,marks,certificate):
        self.name=name
        self.sid=sid
        self.sclass=sclass
        self.div=div
        self.marks=marks
        self.certificate=certificate
    def disp(self):
        print(self.name,self.sid,self.sclass,self.div,self.marks,self.certificate)
    def change_class(self,new):
        self.sclass=new
    def change_div(self,new):
        self.div=new
    def change_marks(self,new):
        self.marks=new
    def change_certificate(self,new):
        self.certificate=new
s1=school('A',100,'10th','A',98,'No')
s2=school('B',101,'10th','D',99,'No')
school.disp(s1)
school.disp(s2)
school.change_class(s1,'11th')
school.change_div(s1,'A')
school.disp(s1)
s2.change_class('12th')
s2.change_marks(97)
s2.change_certificate('Yes')
s2.disp() '''


#Assignment no 1: Object Method
'''1. Create a Student class with attributes name, age, and marks. Create an object and
use a method to display the details. 

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s1=Student('Atharva',21,98)
Student.display(s1)     '''


'''2. Create an Employee class with name and salary. Create a method to display
employee information. 

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name,self.salary)
e1=Employee('Isha',95000)
e2=Employee('Shetty',90000)
Employee.display(e1)
Employee.display(e2)     '''


'''3. Create a Car class with brand, model, and price. Create an object and a method to
show its details. 

class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print(self.brand,self.model,self.price)
c1=Car('Toyota','Fortuner',4000000)
Car.display(c1)    '''
    

'''4. Create a Rectangle class with length and width. Create a method to calculate the
area.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        print('Area:',self.length * self.width)
a1=Rectangle(12,14)
Rectangle.display(a1)   '''


'''5. Create a Circle class with a radius. Create methods to calculate the area and
circumference. 


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def display(self):
        print('Area:',3.14 * self.radius * self.radius)
        print('Circumference:',2 * 3.14 * self.radius)
c1=Circle(4)
c1.display()   '''


'''6. Create a Bank Account class with account_holder and balance. Create methods to
deposit and display the balance. 

class Bank_acc:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,new):
        self.balance=self.balance + new
    def display(self):
        print("Account Holder:",self.account_holder)
        print("Balance:",self.balance)
a1=Bank_acc('Atharva',40000)
Bank_acc.display(a1)
print("After deposit new Balance Value : ")
a1.deposit(20000)
a1.display()   '''
        

'''7. Create a Calculator class with methods for addition, subtraction, multiplication, and
division.

class Calculator:
    def addition(self,a,b):
        print("Addition:",a+b)
    def subtraction(self,a,b):
        print("Subtraction:",a-b)
    def multiplication(self,a,b):
        print("Multiplication:",a*b)
    def division(self,a,b):
        print("Division:",a/b)
c1=Calculator()
c1.addition(10,2)
c1.subtraction(10,2)
c1.multiplication(10,2)
c1.division(10,2)  '''


'''8. Create a Mobile class with brand, model, and price. Create a method to display all
mobile details. 

class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print(self.brand,self.model,self.price)
m1=Mobile('Samsung','S26 Ultra',150000)
m2=Mobile('Samsung','S26',90000)
m1.display()
m2.display()  '''


'''9. Create a Product class with product_name, price, and quantity. Create a method to
calculate the total price. 

class Product:
    def __init__(self,product_name,price,quantity):
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        print("Total Price:",self.quantity * self.price)
p1=Product('Laptop',90000,2)
p1.total_price()   '''


'''10. Create a Student class with marks. Create a method to check whether the student
has passed or failed. 

class Student:
    def __init__(self,marks):
        self.marks=marks
    def result(self):
        if self.marks>=35:
            print("Passed")
        else:
            print("Failed")
s1=Student(98)
s1.result()    '''


'''11. Create an Employee class with salary. Create a method to increase the salary by a
given percentage. 

class Employee:
    def __init__(self,salary):
        self.salary=salary
    def increase(self,percentage):
        self.salary=self.salary + (self.salary * percentage / 100)
        print("New salary:",self.salary)
e1=Employee(90000)
e1.increase(12)   '''
        

'''12. Create a Book class with title, author, and price. Create a method to display book
information. 

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
b1=Book('The power of your Subconscious mind','Dr Joseph Murphy', 250)
b1.display()   '''
        

'''13. Create a Person class with name and age. Create a method to check whether the
person is eligible to vote. 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eligibility(self):
        if self.age>=18:
            print("Eligible")
        else:
            print("Not eligible")
p1=Person("Atharva",21)
p1.eligibility()    '''


'''14. Create a ShoppingCart class with product price and quantity. Create a method to
calculate the total bill. 

class Shoppingcart:
    def __init__(self,product_price,quantity):
        self.product_price=product_price
        self.quantity=quantity
    def total(self):
        print("Total bill:", self.product_price * self.quantity)
p1=Shoppingcart(10000,5)
p1.total()    '''
        

'''15. Create a Movie class with movie_name and rating. Create a method to check
whether the movie rating is Good, Average, or Poor. 

class Movie:
    def __init__(self,movie_name,rating):
        self.movie_name=movie_name
        self.rating=rating
    def rating_movie(self):
        if self.rating>=8:
            result="Good"
        elif self.rating>=5:
            result="Average"
        else:
            result="Poor"
        print("Movie name:", self.movie_name)
        print("Rating:", result)
m1=Movie('Sitara', 4)
m1.rating_movie()   
m2=Movie('Tare Jameen Par', 9)
m2.rating_movie()   '''






# Class method :
''' It is used to Access & Modify the members and properties of Class. '''
''' In Class method we will be passing "cls" to store the address of class. '''
''' Whenever we want to create class method, we need to make use of decorator called "@classmethod". '''

# Syntax for create class method :
''' class cname:




    @classmethod
    def methodname(cls,args):
             #statement block

objname=classname(values)  #object creation
cname.methodname(values)
        OR
objname.methodname(values)     '''



'''Create a class called Hospital and create 5 object methods in it. 

class Hospital:
    Hname='Anand Clinic'
    loc='Mumbai'
    time='10-5'
    fees='500 rs'
    s_type='General'
    def __init__(self,name,pid,problem,phno):
        self.name=name
        self.pid=pid
        self.problem=problem
        self.phno=phno
    def disp(self):
        print(self.name,self.pid,self.problem,self.phno)
    def ch_phno(self,new):
        self.phno=new
    def ch_problem(self,new):
        self.problem=new
    @classmethod      # It is a decorator used to access or modify class members
    def display(cls):
        print(cls.Hname,cls.loc,cls.time,cls.fees,cls.s_type)
    @classmethod
    def ch_fees(cls,new):
        cls.fees=new
    @classmethod
    def ch_Hname(cls,new):
        cls.Hname=new
    @classmethod
    def ch_loc(cls,new):
        cls.loc=new

p1=Hospital('Anna',100,'Fever',9876543210)
p1.disp()   #display the object details = objectname.methodname()
Hospital.display()  #display the hospital details = cname.methodname()
Hospital.ch_fees('600 rs')
Hospital.display()    '''


#Assignment on class method:
'''1. Create a Student class where all the students belong to the same school\
Use a classmethod to change the school name. 

class Student:
    school = 'Xavier School'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def disp(self):
        print(self.name,self.rollno,self.school)
    @classmethod
    def change_school(cls,new):
        cls.school=new
s1=Student('Atharva',101)
s2=Student('Rahul',102)
s1.disp()
s2.disp()
Student.change_school('Public School')
s1.disp()
s2.disp()   '''


'''2. Create a Car class where all the cars have a common company name. Use a class method \
to change the company name. 

class Car:
    company='Toyota'
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def disp(self):
        print(self.model,self.price,self.company)
    @classmethod
    def change_company(cls,new):
        cls.company=new
c1=Car('Fortuner',4000000)
c2=Car('Innova',2500000)
c1.disp()
c2.disp()
Car.change_company('BMW')
c1.disp()
c2.disp()  '''


'''3. Create a Product class where all the products belong to the same store. Use a \
classmethod to change the store name. 

class Product:
    store='Reliance'
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def disp(self):
        print(self.name,self.price,self.store)
    @classmethod
    def change_store(cls,new):
        cls.store=new
p1=Product('Laptop',50000)
p2=Product('Mobile',20000)
p1.disp()
p2.disp()
Product.change_store('Croma')
p1.disp()
p2.disp()   '''
 






















