
import time
# TO-DO: Implement a recursive implementation of binary search

start_time2 = time.time()
#recursive Binary search
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr, target, mid + 1, high)
    return -1

data = [2, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 21, 23, 24, 25, 28, 29, 30, 32]
target = 1


print(binary_search(data, target, 2, 32))
end_time2 = time.time()
print (f"runtime: {end_time2 - start_time2} seconds")

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

