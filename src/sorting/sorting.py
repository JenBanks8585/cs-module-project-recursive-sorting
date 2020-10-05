# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1

    result += left[i:]
    result += right[j:]
    return result

arr1 = [2,5,6,3,6,3,8,10,0,1]
arr2 = [3, 4,5,7,3,8,9]

print(merge(arr1,arr2))





#def merge(arrA, arrB):
#    elements = len(arrA) + len(arrB)
#    merged_arr = [0] * elements
#
#    # Your code here
#
#
#    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <=1:
        return arr

    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left , right)

print(merge_sort(arr1))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
