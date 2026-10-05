# example - 1
print("1.Birany")
print("2.Chicken 65")
print("3.Veg Pulao")
print("4.Butter Chicken")
print("5.Paneer Tikka")
choice=4
choice=int(input())
print("Enter your choice",choice)
match(choice):
    case(1):
        print("Item " " :Birany")
        print("price " ":₹150/1pec")
        print("Description:Crispy and spicy  chicken pieces and birany rice")
    case(2):
         print("Item " " :Chicken 65")
         print("price " ":₹180")
         print("Description:Crispy and spicy deep-fried chicken pieces")
    case(3):
         print("Item " " :Veg Pulao")
         print("price " ":₹120")
         print("Description:spicy and tasty rice")
    case(4):
         print("Item " " :Butter Chicken")
         print("price " ":₹250")
         print("Description:Jusy and Tasty butter chicken")
    case(5):
         print("Item " " :Paneer Ticka")
         print("price " ":₹280")
         print("Description:Tasty paneer ticka item")
    case _:
        print("invalid operator")

# example-2

print("1.Check Balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")
choice=1
amount=3000
choice=int(input())
amount=int(input())
print("Enter your choice:",choice)
print("Enter withdraw amount:",amount)
match(choice):
    case(1):
        print("Withdraw successful")
        print("balance amount",amount)
        
    case(2):
         print("Withdraw successful")
         print("balance amount",amount)
    case(3):
         print("Withdraw successful")
         print("balance amount",amount)
    case(4):
        print("Withdraw successful")
        print("balance amount",amount)
    case(5):
        print("Withdraw successful")
        print("balance amount",amount)
    case _:
        print("invalid operator")

n=int(input("enter the value:"))
units=int(input("Enter the unit value:"))
if(units<=100):
    print("Total Bill: ₹",units*2)
elif(units>=101 and units<=200):
    print("Total Bill: ₹",units*4)
elif(units>=201 and units<=300):
    print("Total Bill: ₹",units*6)
elif(units>=301 and units<=400):
    print("Total Bill: ₹",units*8)    
else:
    print("Not matched")
