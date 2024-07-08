numbers = [1,2,3,4,5,6,7,8,9];

evens = [];

for n in numbers:
    if(n%2 == 0):
        # print(n);
        evens.append(n);
    else:
        print("No !");
        
print("evens :", evens);
# print(len(numbers));