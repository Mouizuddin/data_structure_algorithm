''' Merge Sort
The time complexity of MergeSort is O(n*Log n) in all the 3 cases (worst, average and best)
as the mergesort always divides the array into two halves and takes linear time to merge two halves.
'''

def merge_sort(array):
    if len(array)> 1:
        mid = len(array) // 2 # finding the mid of the array
        left_array = array[:mid] # left partition
        right_array = array[mid:] # right partition
        # recursive call

        merge_sort(left_array)
        merge_sort(right_array)

        left = right = indexs = 0
        #  data to temp arrays left [] and right []

        while left < len(left_array) and right < len(right_array):
            if left_array[left] < right_array[right]:
                array[indexs] = left_array[left]
                left += 1
                indexs += 1
            else:
                array[indexs] = right_array[right]
                right += 1
                indexs += 1
        while left < len(left_array):
            array[indexs] = left_array[left]
            left += 1
            indexs += 1
        while right < len(right_array):
            array[indexs] = right_array[right]
            right += 1
            indexs += 1
    return array

print(merge_sort([1078,3,34,546,0]))