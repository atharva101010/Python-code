#OOP example

'''class Demo:
    pass
ob1 = Demo()
ob2 = Demo() '''



'''class Demo:
    pass
ob1=Demo()
ob2=Demo()
print(type(ob1))
print(type(ob2)) '''

#Accessing properties
''' 
class A:
    a=10
    b=20
o1=A()
o2=A()
o3=A()

print(A.a,A.b) #Accessing properties from class. Syntax : classname.propertyname
print(o1.a,o1.b)#Accessing properties from class. Syntax : objectname.propertyname
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
Constructor/__inti__/initialisation method:
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



          
