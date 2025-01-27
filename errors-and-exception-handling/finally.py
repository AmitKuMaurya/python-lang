# finally block.

a = 5
b = 0;

# don't use this.
try :
    print("open file");
    print(a/b);
    print("close file");
except Exception as e :
    print("Error !", e);
finally :
    print("Inside finally !");

# Use this.
try :
    print("open file");
    print(a/b);
except Exception as e :
    print("Error !", e);
finally :
    # print("Inside finally !");
    print("close file");


# we are using {finally block} because, 

# let's suppose we are opeining a file in try block and then we got an error will be thrown in except block so after printing a/b
# the file is not closed which should not happen.

# that's why we have finally block which will execute the file closing method.

# after reading the file or without reading file.
# 
# finally method executes always. 
