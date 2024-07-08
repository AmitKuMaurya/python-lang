# like list tuples are also ordered collection of data.
# tuples are unchangable.
# hetrogenious.
# iterable.

t = (22,33,88,44,"Hii","Hello",True);

# indexing in tuples 
# t[0]

# slicing
# slice = t[0:4];
# print(slice);

# print(t);

t2 = (1);  # it is considered as an int because only single arg is present;
print(type(t2));
t3 = (2,); # here metoining , after 2 will be saying that it is going to add more value to tuple
print(type(t3));

t4 = tuple("Amit"); # this only takes one arg, and   
print(t4, type(t4));

# tuple inside tuple
t5 = ((3,4),(5,7));
print(t5, len(t5), type(t5[0]));

# list inside tuple
t6 = ([3,4],[5,7]);
print(t6, len(t6), type(t6[0]));


# Mutability in Tuples.

t = ([4,5,6,7],"Amit");
# here we have changed the first index of list inside tuple but actually
#  we are not changing the tuple,
#  we are just accessing list and manipulating that.

t[0][0] = 99;
print(t, type(t[0]));

# use this to get rid of mulability in tuples.

tu1 = ((2,3,4,5),"Hey Amit!");
# tu1[0][0] = 0; # here you get error.
print(tu1,len(tu1),type(tu1[0]));

# unpacking in tuples.

# a,b,c = 1,2,3; # thats how we define multiple variable in single line.

tu2 = (1,2,3,4);
a,b,c,d = tu2;
print(type(a), type(b), tu2);
# print(type(tu2), tu2, len(tu2))


# methods in tuple.

# we have most of the tuples
    # count, index, concatination, 
        # possible to covert tuple to list and list to tuple.





