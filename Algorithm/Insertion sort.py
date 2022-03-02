'''Insertion sort
It can also be useful when input array is almost sorted,only few elements are misplaced in complete big array.
The average, best-case, and worst-case time complexity of Selection Sort is: O(n2)
'''
import sys
array = [5,4,3,2,1,100 ]
print(array)
def insertion_sort(array):
    for index in range(1,len(array)):
        unsorted_part = array[index]
        position = index # index are -> 1,2,3,4....
        while unsorted_part < array[position-1] and position > 0:
            array[position] = array[position-1]
            position -= 1
        array[position] = unsorted_part
    return array


print(insertion_sort(array))
print(sys.getsizeof(insertion_sort(array)))