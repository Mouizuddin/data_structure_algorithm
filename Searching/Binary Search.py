''' Binary search
A binary search algorithm works on the idea of neglecting half of the list on every iteration.
It keeps on splitting the list until it finds the value it is looking for in a given list.
A binary search algorithm is a quick when compared to a simple linear search algorithm.

 Worst Case Time Complexity  O(logN).
 Average Case Time Complexity O(logN).
 Best Case Time Complexity  O(1).
'''

# Iterative method
def binary_search(array,key):
    low = 0
    high = len(array)-1
    key_found = False

    while low <= high and not key_found:
        mid_value = (low + high) // 2
        if key == array[mid_value]:
            key_found = True
        if key > array[mid_value]:
            low = mid_value + 1
        else:
            high = mid_value - 1
    if key_found == True:
        print(f'Key found at index {array.index(key)}')
    else:
        print(f'Key not found')


if __name__ == '__main__':
    array = [132, 43, 65, 68, 89, 24, 13, 6]
    array.sort()
    print(array)
    binary_search(array, 12126) # False >> key not found
    binary_search(array,6) # True >> Key found at index 0