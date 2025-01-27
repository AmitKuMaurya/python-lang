#  The word "polymorphism" means having many forms.
#  Same class method can work differently for different work.



    # functional level polymorphism.
    # where, a function behaves diffferently for different kinds of objects.

l = [1,2,3,4];
print(len(l));

print(len("amit"));

# the same function is working different on different case.
# print(len(234))

# inbuilt function.
print(sum(l));

# the same function is working different on different case.
# print(sum(234));

def mul(*args) :
    total = 1;
    for s in args:
        total *= s;

    return total;

print(mul(1,2,3))





        # A function makeSoun() could work differently for cow and cat.

    # operater level polymorphism. -- it works on operaters.

        # if we see operater like arthematic operater.
        # It behaves differently with different kinds of operaters.

print('sum :' ,2 + 2);

print('concat :',"2" + "2");

# the same operater is working different on different case.
# print(2-"2");