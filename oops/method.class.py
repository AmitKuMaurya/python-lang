# methods in class.

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

    def greet(self, message) :
        print(f"I'm {self.name}. {message} boss.");

amit = Human("Amit Maurya",20,"Male","Film Making");

# create attribute manually.
# amit.nationality = "Indian";
print(amit);


amit = amit.greet("Good Morning");


emma = Human("Emma Maurya",20,"Female","Social Services");
emma = emma.greet("Hey morning");
