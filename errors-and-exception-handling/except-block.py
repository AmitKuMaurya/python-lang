# in this part of python we will see how to handle exception

# before wew were not getting exectly what is the cause of error.

# here we will learn the same.

a,b = 1,"n";

# print(a,b);

try:
    print(a+b);
except Exception as e:
    # In case you wanted to ignore the error.
    # pass;
    # In case you wanted to print a error message.
    print("There is some error occured!",e);

print("Hello, Kullu !");