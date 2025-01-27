# There is a problem in which you have to find out which one is the maximum in the list.

# basically find, maximum number in an array.

marks = [90,80,100,101,50,40,20,44];

def findMaximumMarks(marks):
    # print(marks);
    min = 0;
    pad = None;
    for m in range(len(marks)) :
        # print("min :",min, "pad :",pad, marks);
        if(min < marks[m]):
            min = marks[m];
            pad = min;
        else:
            continue;
    return pad;

print(findMaximumMarks(marks));