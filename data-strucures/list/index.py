# A data structure is a specialised format for storing, retreving and processing and organsing data.

# * list.

# two way to decalre list.

list = [12,3,4,5]
# print(type(list),list, len(list));

# list are iterable means --> we can run loops in it.

# slicing in list;

numbers = [1,2,3,4,5];

forward = numbers[0:len(numbers)]
# print(forward);

backward = numbers[len(numbers):0:-1];
# backward = numbers[len(numbers)::-1];
# print(backward);


# list inbuilt metthods to perform.

# count

# index

# pop --> this method pops out the last item of list.

# pop = numbers.pop()
# print(pop);
# print(numbers);

# remove --> this method removes out the given index or value of item.

# remove = numbers.remove(3)
# print(numbers);



# sort --> sort the item of list in asc or desc order

# sort = numbers.sort(reverse=True);
# print(numbers);

# insert ---> add the value to given index;

# insert = numbers.insert(2,74);
# print(numbers);

# append. its pushes the item to the last index as it is.

haldiram_savory = ['chana chur','navratan','punjabi tadka','nut crackers','aalu bhujia'];
append = numbers.append(20);
# append1 = numbers.append(haldiram_savory);
# print(numbers);


# extends --> it interates the list one by one i.e. un-wraps the item and pushed.

numbers.extend(haldiram_savory);
# print(numbers);

# hetorgenious list --> lists which stores multiple types of data type.

hetro_list = [1,"amit",1.3,{ "age" : 21}, True];

# 2D-list.

twoDList = [
    [1 ,2, 3],
    [4 ,5, 6],
    [7 ,8, 9]
];

# this is how we print 2d array in for loop.

array = [];
for i in range(len(twoDList)) :
    # print(twoDList[i],i);
    for j in range(len(twoDList[i])):
        # print("Yes!");
        # print(twoDList[i][j]);
        array.append(twoDList[i][j]);

# print(array);

# list comprehension --> 

# normal way to add nnumbers from 0 to 9;

# listy = [];
# for i in range(20):
#     listy.append(i);
# print(listy);

# using list comprehension;
l = [ k for k in range(0,30,3) ];
print(l);


