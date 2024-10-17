# Arguments and Parameters in Python.

def greet(name,message):
    print(f"Hey, {name}!, {message} ");

greet("amit","you will win a day !");



# normal way to pass and receive arguments.
# we can pass multiple arguments also there.

def test(params) :
    print(params)

test("hello");


# default arguments.
# first param ---->> Can never be default argument

def test(day,msg,end="Have, a good day !") :
    print(day,msg,end);

test("Friday",", ist aufregend!");



# arbitary aguments --> *args

# this is basically to accept/pass as arguments any type of data-structure instead of [key:value]

def hello(*args):
    print(args);

hello("gutan tag","guten aufregend","tchuss","bis spater!");

# keyword arguments --> **kwargs
# this accepts args/params in [key:value] pair.

def mutliArgs(**kwargs):
    print(kwargs);

mutliArgs(name="Alice", age=30, city="New York");