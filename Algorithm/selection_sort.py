'''
 selection sort is an in-place comparison sorting algorithm.
 It has an O(n2) time complexity
'''
def selection_sort_1(array):
    count = 0
    for i in range(len(array)-1):
        min_value = min(array[i:]) # max(array[i:) for sorting in Descending Order
        index_of_min_value = array.index(min_value,i) # i is the start from value
        if array[i] != array[index_of_min_value]:
            count += 1
            array[i] , array[index_of_min_value] = array[index_of_min_value],array[i]
            print(f'({count}) Sorting  >> {array}')
    print("===="*10)
    print(f'Final sorted array >> {array}')
array = [1, 6, 4, 7, 90, 9, 2, 5, 8,-1]
selection_sort_1(array)

# without using min() and max()
def selection_sort_2(array):
    for i in range(len(array)-1):
        min_value = array[i] # selection the first element
        for j in range(i+1,len(array)):
            if array[j] < min_value: # min() assending order
                #  if array[j] > min_value: max() decending order
                min_value = array[j]
    min_index = array.index(min_value,i)
    if min_value != min_index:
        array[i],array[min_index] = array[min_index],array[i]
    print(f'Final without (min) array {array}')

selection_sort_2(array)