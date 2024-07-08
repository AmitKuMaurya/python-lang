# range is
# range(start, end, jump/skip);
# by default start is 0 and end is 1, and jump do not have any vlue by default.


# print(range(1));

print(list(range(1,10)));

# to jump/skip forward.
print(list(range(1,10,2)));


# to jump/skip backward.

# here we are moving from 10 to 1 but, we can't 1 doesn't exist forward.
print(list(range(10,1)));  # []

# for that we do jump negatively
print(list(range(10,1,-1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]


