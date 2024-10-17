# Return in Python.

# here, we wil learn about how return method works in python.

def sum(a,b):
    c =a+b;
    return c;

print(sum(3,3));

# if, we will not return any kind of value from the function then, it return the value none.


# if we wanted to return more than one value then we can do that.
# it's just that it will be returned in the form of tuples.

def intro(name, age, profession) :
    return name, age, profession

funcName = intro("amit",22,"problem solver")

print(funcName, type(funcName));
#  it's returning in that way : ('amit', 22, 'problem solver') <class 'tuple'>

# if you wanted to access the value of returned tuples then, access them by indexes.


# Lambda Function

# without variables.

# print((lambda a,b : a +b )(9,9));

sum = (lambda a,b : a +b )(9,9);
print(f'sum : {sum}');

# with variable 

func = lambda a,b : a+b;
print(func(2,9));

# Problem.
# with normal function

def findGreater(a,b) :
    if a > b :
        return a
    elif b > a :
        return b
    else :
        return "Nothing"
    
print(findGreater(11,11));

# same operation using lambda function.


greater = (lambda x,y : x if x>y  else (y if y > x else False ) )(8,8)

print(f"Greater : {greater}");


# print((lambda a,b : a if a > b else ( b if b> a else "Nothing"))(33,44));

# sorting a list;

nums  =  [(10,11),(12,13),(14,15),(16,17),(18,19),(20,10)];
print(f'nums : {type(nums)}');

num = [9,8,7,77,88,66,9,0]
# print(nums, type(nums[5]));

# that sort in built function is sorting inside list of tuples on the basis of it's first index.
num.sort()
print(num);
print(nums);

# Although we can do it on the basis of second index of typle inside list.

# here is how?
    # for this we have to pass a function to sort method which will define the index.

# normal function.
# def k (x) :
#     return x[-1];

# lambda function

nums.sort(key=(lambda x : x[1]));
print(nums);