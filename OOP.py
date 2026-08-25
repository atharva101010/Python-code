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




class Bank:
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
print(c2.bname,c2.loc)
