print("Hello World!");

# python dividets data types into 2 category --> mutable or immutable

# mutable -> List, Dictionary, byte array.

# immutable --> Int, Float, Complex, Tuples, String, set

# Number --> Data Type.

a = 56;
# here type is a inbuilt function of python which tells the type of Data/value;
print(a, "Type of a", type(a))
a = 2.0;
print(a, "Type of a", type(a))
a = 1 + 2j;
print(a, "Type of a", type(a));


#  a string is a collections of one or more character put in a single quote, quote and triple quote.

# single or double quotes;

s = 'hey';
print('s: ', s, type(s));

s = 'hey there!';
print('s: ', s, type(s));

# triple quotes --> it will print in same format you define.

s= '''
Welocome
Home
Dear
''';
print("s :", s, type(s));

# List --> list is an ordered seqence of item.
# it's a mutale data Type.

l = [1,'pro',2,33];
print("l: ",l, type(l));


# tuples --> Tuples is an ordered sequence of items same as a list.
# it is defined as paranthesis () where items are seperated by commas.

# tuples should be more than one in paranthesis otherwise ot won't be defined as tuples.

t = (1, 3.3, 'production');
# l[1] = 4.4 --> can't mutate.
print("t :", type(t), t);

# dictionary
d ={
    'name' : "Amit",
    'age' : "21"
}; 

print("Print d ", d, type(d));

# set --> the data present in set are unique they can;t get repeated.

my_set = { 1,2,3,3};
print('my_set', my_set , type(my_set));

# boolean --> mutable data type.
b = True;
b = False
print("B :", b ,type(b))

