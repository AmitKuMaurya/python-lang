# inheritence in class;

    # when a class derives every attributes and method from other class.
    # it gets access to all its method and attributes.
    #


# we have to create a method,
# which can identify that if a person is dead.
# then decrement the population count.

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


# a1 = Human("A1",22);
# # print(a1.dead());
# e1 = Human("E1",25);
# # print(e1.dead());
# l1 = Human("L1",37);
# # print(l1.dead());
# m1 = Human("M1",38);
# # print(m1.dead());

# karira = Human("Karira", 35);
# karira.child(5)
# print(f"Alive count of human is: {Human.population}");

class Employee(Human):
    pass;

person = Employee("Amit",25);

print(person.age);

print(person.name);

print(person.alive);

print(f"Before Dead : {person.population}");

print(person.dead())

print(f"After Dead : {person.population}");

# inherited class is also known as inherited class.

#  Human is a base class;
#  Employee is derived class;





