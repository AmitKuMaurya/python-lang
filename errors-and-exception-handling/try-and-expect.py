# In this part will be understanding how to use try and expect.

a,b = 1,"n";

# print(a,b);

try:
    print(a+b);
except:
    # In case you wanted to ignore the error.
    # pass;
    # In case you wanted to print a error message.
    print("There is some error occured!");

print("Hello, Kullu !");