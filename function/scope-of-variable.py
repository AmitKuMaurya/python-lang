# there are two types of scopes are there : global and local scope
# global scope is something when you use anywhere in program.
# local variables are those, which uses internal program variables.


x= 21;

def num():
    # this is accessing value of local scope.
    y = 30;
    print(f'value of y in fn is {y}');
    # print(value);
    print(f'value of x in fn is {x}');

print(num());


# this is accessing value of global scope . and it can be used inside function also.
print(f'value of x global {x}');
# print(f'value of y global {y}');

# if a variable is inside a function it would be in local scope but, still we have to make it a global scope in that
print("Making A local variavle global");


a = 10;

def demo():
    global a;
    a = 20;
    print(a);

print(a);
demo();
print(a);

