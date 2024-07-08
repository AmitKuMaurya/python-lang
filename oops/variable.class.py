# Class Variables

class Human :

    # class varables. 

    # class Variables are used to update the class and using
    #  cunstructor at this place will only allow us to update that particular instance/ object
    population = 0;
    data = [];
    
    #  constructor 
    def __init__(self, name, age):
        
        # These are are known as attributes of an objects. 
        self.name = name;
        self.age = age;
        Human.population += 1;
        Human.data.append(self.name);

    # method
    def greet(self) :
        pass;

amit = Human("Amit",21)
print(amit);

emma = Human("Emma",25)
print(emma);

print("P:",Human.population);
print("D: ",Human.data);

