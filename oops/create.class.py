# class

# it's a blue-print of creating objets.
# the class kkeyword used to create class.

class Car :
    pass;

# object 

# objects are instances or entities of a class.
# 


honda = Car;
# print(type(honda));

# constructor 

    # constructor is a spetial method used to create and innitialise an object of a class.
    # methods are frfined in th class.
    # the constructor is executed automatically at the time of object creation.

class Human :
    # I want some properties to be with every human objects.
    # Dunder is duble underscore __
    # Dunder is usto create spetial method llke constructor, which called automatically.

    # constructor method. and : they will be common for all human objects.
    def __init__ (self, name, age, gender, hobby) :
        # pass
        self.name = name;
        self.age = age;
        self.gender = gender;
        self.hobby = hobby;
        print("This will always get printed");

amit = Human("Amit Maurya",20,"Male","Film Making");
print(amit);
emma = Human("Emma",25,"Female","Film Making");


# methods in class.