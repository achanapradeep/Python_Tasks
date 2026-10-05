# 1)Single Inheritance without constructor
class India:
    def country(self):
        print("Name of the country")
class State(India):
    def state(self):
        print("country name and state name")
object=State()
object.country()
object.state()

# 2)Single Inheritance with constructor
class collage:
    def __init__(self,Branch,Subbranch):
        self.Branch=Branch
        self.Subbranch=Subbranch
        print(self.Branch)
        print(self.Subbranch)
    def display(self):
        print(self.Branch)
        print(self.Subbranch)
       
class Department(collage):
    def course(self):
       pass 
obj=Department("cse","AIML")
obj.course()
obj.display()

# 3)Single Inheritance with constructor + super()
class Hotel:
    def __init__(self,hotel,location):
        self.hotel=hotel
        self.location=location
    def display1(self):
        print(self.hotel)
        print(self.location)
class Order(Hotel):
    def __init__(self,hotel,location,type,name,price):
        super().__init__(hotel,location)
        self.type=type 
        self.name=name
        self.price=price 
    def display2(self):
        super().display1()
        print(self.type,self.name,self.price)
        print(self.name)
        print(self.price)
obj=Order("Paradise","Kukatpally","Nonveg","Shaverma",130)
obj.display2()

# 5)Multiple Inheritance without constructor 
class Animals:
    def Based_0n_Eating_type_1(self):
        print("Herbivores: plants (cow, elephant)")
class Type(Animals):
    def birds(self):
            print("Birds:(pecock, penguin, parrot)")
class food(Type):
     def seed_eaters(self):
            print("parrots,finches,pigeions")
obj=food()
obj.seed_eaters()
obj.birds()
obj.Based_0n_Eating_type_1()

# 6)Multiple Inheritance with constructor
class State():
    def __init__(self,name):
        self.name=name 
    def display_state(self):
        print("My state name is",self.name)
class Mandal(State):
    def display_mandai(self):
        print("My mandal name is Mulakalapalli")
class Village(Mandal):
    def display_village(self):
        print("My village name is Ramanchandrapuram")
obj=Village("Telangana")
obj.display_village()
obj.display_mandai()
obj.display_state()

# 8)Multiple Inheritance with constructor + super() using a different real-world example
class Camera:
    def __init__(self, megapixels, ):
        super().__init__(self)
        self.megapixels = megapixels

class Phone:
    def __init__(self, number):
        super().__init__(self)
        self.number = number

class Smartphone(Camera, Phone):
    def __init__(self, brand, megapixels, number):
        super().__init__(megapixels=megapixels, number=number)
        self.brand = brand

s = Smartphone("Samsung", 108, "9876543210")
print(s.brand, s.megapixels, s.number)
print(Smartphone.__mro__)

# example-9

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def display_father(self):
        print("My father name is", self.father_name)

class Mother:
    def __init__(self, mother_name):
        super().__init__(self,Father.father_name)
        self.mother_name = mother_name

    def display_mother(self):
        print("My mother name is", self.mother_name)

class Child(Father, Mother):
    def __init__(self, child_name, father_name, mother_name):
        super().__init__(father_name=father_name, mother_name=mother_name)
        self.child_name = child_name

    def display_child(self):
        print("My name is", self.child_name)

obj = Child("Pradeep", "Ramesh", "Lakshmi")
obj.display_child()
obj.display_father()
obj.display_mother()
