#import numpy
def multiply(nums):
    total=1
    for x in nums:
        total *= x
    return total
inp=input()
nums=list(map(int, inp.split(" ")))
print(multiply(nums))
