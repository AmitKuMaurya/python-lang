class Human :

    # class varables. 
    population = 0;
    data = [];
    #  constructor 
    def __init__(self, name, age,alive = True):    
        # These are are known as attributes of an objects. 
        self.name = name;
        self.age = age;
        self.alive = True
        Human.population += 1;
        Human.data.append(self.name)

    # method
    def greet(self):
        print(f"I'm {self.name}. Good Morning to you !");

    def dead(self): 
        if self.alive :
            print(self.name,"Is no more with us");
            Human.population -= 1;
            self.alive = False;
        else :
            print("The Human is also removed from population count.");
    

    def child(self,num):
        Human.population += num;



# inherited class is also known as inherited class.

#  Human is a base class;
#  Employee is derived class;

class Employee(Human):
    # creating Employees constructor.
        # re-initating constructor.
    
    def __init__(self, name, age ,company_name, post):
        # super keyword is used to inherit arrtibutes from their parent class, which is Human.
        super().__init__(name, age)

        # attributes for employee class.
        self.company_name = company_name;
        self.post = post;

    def hire (self, person):
        print(f"{person} is onboarded to XYZ lmt.");
        Human.data.append(person);
        Human.population += 1;

         

# ,
# here we are inheriting the properties of HUman class.

# human class only takes 2 arguments
# amit = Human("Amit",21);
# emma = Human("Emma",25);

# derived from human class so this have human and employee all attribues and method. 
amit = Employee("Amit",21,"CreateBytes","SDE Intern");
emma = Employee("Emma",25,"Meta","Software Engineer");
charu = Employee("Charu",20,"CVS","NCC Coach");
temp = Employee("Temp",85,"Meta","Software Engineer");

# print(amit.name);
# print(emma.company_name);

print(charu.hire("Carry"));
print(Human.data);
print(f"Total Population:{Human.population}");



# use Human class from Employee in order to delete an emplyee.

print(temp.dead())

print(f"Total Population:{Human.population}");

# creating a method to hire from Employee class, and store him to data of Human Class and inheir a method from Human to deete him.



