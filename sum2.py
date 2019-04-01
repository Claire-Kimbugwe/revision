# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
# Example:
#
# Given nums = 2, 7, 11, 15, target = 9,
# 
# Because nums0 + nums1 = 2 + 7 = 9, return 0, 1.

def sum2(nums,t):
    # todo: fill the bpdy of the function
    my_dict = {}
    for i,value in enumerate(nums):
        needed = t - value
        if needed in my_dict:
            result = (my_dict[needed],i)
            return result
        else:
            my_dict[value]= i



sum2([2,7,11,15],9)
