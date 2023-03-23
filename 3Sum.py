# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.


# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Algorithm:
# Create an empty list to return the result
# Sort the array 
# Iterate over all elements of the sorted array
# For each element, first check if it is equal to the element before it. Continue if it is
# Otherwise, compute a TWO SUM
# Since the array is sorted, we can use two pointers instead of a hashmap
# So for each element, the left pointer is immediately after and the right pointer is at the end of the array
# Compute the Three Sum
# We shift the pointers based on whether the computed sum is less than zero or greater than zero
# if it is equal to zero, we add the three numbers to a list and append that to the result list
# We updated left by 1 because all other pointers are self updating
# We keep updating left while the element at left is a duplicate and while l < r
# Finally, we return the result list


# Code
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    
    for i,n in enumerate(nums):
        if i > 0 and n == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l < r:
            ourSum = n + nums[l] + nums[r]
            if ourSum > 0:
                r -=1
            elif ourSum < 0:
                l +=1
            else:
                res.append([n, nums[l], nums[r]])
                l +=1
                while nums[l] == nums[l-1] and l < r:
                    l +=1
    return res

print(threeSum([-1,0,1,2,-1,-4]))
