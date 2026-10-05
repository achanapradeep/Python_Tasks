# Example_1
class Bank:
    BankName="SBI"
    Brach="KUKATPALLY"
    def __init__(self,employ_name,age,role,salary):
        self.employ=employ_name
        self.age=age 
        self.role=role 
        self.salary=salary 
    def display(self):
        print("Bank employ name is ",Bank.BankName)
        print("Bank employ name is ",Bank.Brach)
        print("Bank employ name is ",self.employ)
        print("Bank employ name is ",self.age)
        print("Bank employ name is ",self.role)
        print("Bank employ name is ",self.salary)
emp1=Bank("Sundhar",34,"Accountent",40000) 
print("Employ one")
emp1.display();
emp2=Bank("Kavaya",36,"Assistant_manager",60000)
print("Employ two")
emp2.display();
emp3=Bank("Pradeep",28,"Manager",90000)  
print("Employ three")
emp3.display();

# Example-2

class Restrant:
    RestrantName="Paradise"
    Location="KBHP"
    def __init__(self,customer,type,item,bill):
        self.customer=customer
        self.type=type
        self.item=item 
        self.bill=bill
    def display(self):
        print("customer details",Restrant.RestrantName)
        print("customer details ",Restrant.Location)
        print("customer details ",self.customer)
        print("customer details ",self.type)
        print("customer details ",self.item)
        print("customer details ",self.bill)
cust1=Restrant("Sagar","Veg","Palav",250) 
print("customer one")
cust1.display();
cust2=Restrant("sukanya","Veg","Veg Panner",350)
print("customer two")
cust2.display();
cust3=Restrant("Harikrishna","Non Veg","Birany",500)  
print("customer three")
cust3.display();


