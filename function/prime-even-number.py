# Here is the prime even problem.
# print(tuple(range(1,21)));

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

def findPrimeEven(nums):
    for i in nums:
        if i%2 == 0 :
            print(i, end=" ");
            



print(findPrimeEven(numbers));
