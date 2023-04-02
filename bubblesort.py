
def bubbleSort(arr):
    swapHappened = True
    while swapHappened == True:
        swapHappened = False
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i-1]
                arr[i-1] =arr[i]
                arr[i] = temp
                swapHappened = True



arr = [1,2,3,4,5]

bubbleSort(arr)
print(arr)