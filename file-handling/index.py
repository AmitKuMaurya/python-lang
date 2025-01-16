# In order to perform any kind of activity in file. we, first have to open a file.

# and later on we, can perform any kind of activity in this like [write, delete, upadte];

                                    # Chapter - 1

# f = open("./file-handling/data.txt");

# print(type(f));

# content = f.read();

# doClose = f.close();
# print(content);


                                    # Chapter - 2

# here, we will see, [how many modes are there to open a file]

# "r" : read mode only.
# "w" : write mode only.
# "a" : appending data at the end of file.
# "wt" : write text
# "wb" : write binary
# "rb" : read binary
# "rt" : read text

# f = open("./file-handling/data.txt", "w"); # this "w" and "wt" is used for similar operations.

# reading = f.read();

# writing = f.write("hanji hanji dedo mike pe light up, toh bolna bhot kucch toh pol ni kholte");
# print(writing);

# and, one more thing is there after writing text in file it [returns the length of text].

                                # Opening a file with [with open] keyword.
                        
# it automatically, close the file after performing the operations.

# by deaflyt it's in read mode. but, we can open it in wirte mode also by just passing second argument as "w".

# with open("./file-handling/data.txt") as f:
#     print(f.read());


                                # chapter - 3 
                                 
# we can write also using [open with]

# when we write anything in a file it reoakces the new text with the old text.

# with open("./file-handling/data.txt", "w") as f:
#     print(f.write("Tumse, Na ho paega !"));

# if we have to append any text using [with clause];

# with open("./file-handling/data.txt", "a") as f:
#     print(f.write("Humse, ho jeaga. tum apna dekho !"));

                                # chapter - 4

# with open("./file-handling/data.txt", "r") as f :
#     print(f.read(8));
#     # [tell] : helps to find out, where the pointer is pointing.
#     print(f.tell());
#     # and , in this read it will start pointing where we left last.
#     print(f.read(4));

#     print(f.tell());


#  we have one more method in read mode which is [seek]: with that we can reset the file handle.
# if we give [seek] and a index value to method it will start reading form there only.

# we, have another method in read mode in order to read the file line by line to basically
# [.readLines()] -->  it will return line in string of array which can be picked up by indexes.
# [.readLine()] -->  it will return teh first line of file. 

with open("./data.txt", "r") as f:
    print(f.readlines()) # it will return in array so, we can iterate also.



                            # Chapter - 5 [Reading and writing birnary data in file];
   

# with open("./file-handling/data.txt", "rb") as rb:
#     binaryData = rb.read();
#     print(binaryData);

#     # open some file and write the re
#     with open("./file-handling/data.txt", 'wb') as wb:
#         wb.write(binaryData);


                            #Chapter - 6 [ append mode in file]

# we, alraedy covered this method while working with write method in file.
