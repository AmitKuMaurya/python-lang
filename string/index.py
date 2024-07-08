# ech of the alphabet character of string is associated to a value of number.
# thats how computer understand them.
# a to z ---> 97 to 122
# A to Z ---> 65 to 90.

# the binding of character to a value is known as encoding.
# we have around 10 way of encoding characters.

# ord()

b = ord("b");  # to find the encoding value of "b";
# print(b);

# Z = ord("Z");
# print(Z);

# chr() is to know, what character is encoded with a particular value;

# nintySeven = chr(69);
# print(nintySeven);

# find length in string.


# from reverse;
str = 'Amit Maurya';
size = len(str);
# print(str[-size]);


# slice in string.

# [start:endLjump] -->in this manner spplice works.

splice = str[0:8:2];
# print(splice);

            #    start    till end
# lastIndex = str[   0   :    len(str)  ]
# print(lastIndex);


# by deafult start is 0th index and end is last-index of str.
# print(str[:-1])  # for accessing the last elemet.

print(str[:-(len(str)+1):-1])  # for reversting the string.
            # or
# print(str[-1:-(len(str)+1):-1])  # for reversting the string.
            # or
# print(str[::-1])  # for reversting the string.
