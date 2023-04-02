def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    i = 0 
    finalArray = []
    while i < m+n and j < n:
        if nums1[i] == 0:
            finalArray.append(nums2[j])
            i += 1
            j += 1

        if nums1[i] != 0 and nums1[i] < nums2[j]:  
            finalArray.append(nums1[i])
            i += 1
        else:
            finalArray.append(nums2[j])
            j += 1
    
    for i in range(n+m):
        nums1[i] = finalArray[i]

first= [1,2,3,0,0,0]
second = [2,5,6]

merge(first, 3, second, 3)
print(first)