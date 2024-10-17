# we have to write a python program where, you have to return only unique elements from that list/array;

# input [1,3,7,2,3,4,5,2,6,1,7];
# output [1,2,3,4,5,6,7];

list = [1,3,7,2,3,4,5,2,6,1,7];
print(len(list))
newList = [];
def test(array):
    # print(array);
    for l in list:
        # print("hello");
        if l not in newList :
            newList.append(l);
    # if(list)

print(test(list));
print(f'values inside newList {newList}');
