def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = calculateTotal(nums)
        for pivot_i in range(len(nums)):
            right_sum -= nums[pivot_i]
            if left_sum == right_sum:
                return pivot_i
            left_sum += nums[pivot_i]
        return -1 


def calculateTotal(nums):
    total = 0 
    for num in nums:
        total += num
    return total



nums = [2,1,-1]


print("the return is: ",pivotIndex(nums))
alist = []
for i in range(24):
    alist.append(i+1)

print(alist)