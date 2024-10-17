    ############################# add, update delete in sets ####################################


# Updating  a set

set = { 1, 1, 2,2, 3, 3, 4, 4, 5, 5, 6, 6};

print(set);
set.add(10);
print(f"sets are here : {set}");

# that is how we upadte an element into set. 
name = "amit";
set.update(name);
# set.update(name);
print(set);

# that is how we remove an element foom set.   
    # actually the elements removes randomly from the set.


set.pop();

print(set);

# in the case, if we wanted to remove particular element.

set.remove("a")

print(set);


# Inetrsection in python.

java = { "Iron Man", "Spidy","Hulk" }
python = { "Thor", "Loki", "Hulk"}

# with the help of intersection we can find out, what is common between two sets.

# print(java.intersection(python));

# print(python.intersection(java));

# Union in python. --> this method actually combines the sets and moves the duplicasy.

print(python.union(java));

print(java.union(python));

# difference() method in python --> this method is used to ignore the common elements of a set.

print(f" difference : {java.difference(python)}");


#Yes, in Python sets, the add() method is used to insert a single element into the set. If you want to insert multiple elements, you need to use the update() method.


