# drive a car problem.

# age = int(input('Please Enter You Age! :'));

# if age > 18 : 
#     if age >= 60:
#         print("Take care, Somebody will be driving it for you.");
#     else : 
#         print("You are eligible enough to drive.");
#         print("Please drive safely.");
# else : 
#     print("Fuck Off!");


number = int(input('Please Enter a number.'));

# if number > 0 :
#     print("Number is Positive Integer");
# if number == 0 :
#     print("Number is Zero")
#     # we prefer to not use if condition twice because it will execute all if.
#     # and in last if not gets true the esle gets printed even if the first if compared.
# else : 
#     print("Number Is Negative Integer");

# output.
# Number is Positive Integer
# Number Is Negative Integer

if number > 0 :
    print("Number is Positive Integer");
elif number == 0 :
    print("Number is Zero")
else : 
    print("Number Is Negative Integer");