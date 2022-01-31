''' Bubble sort
 Is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.
 The average and worst-case time complexity - O(n2)
'''
def bubble_sort(array=None):
    # user_input = int(input("Enter num"))
    # array = [int(input('value : ')) for x in range(user_input)]

    for iteration in range(len(array)-1):
        for i in range(len(array)-1-iteration):
            if array[i] != array[i+1]:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    print(array)
            else:
                print(array)

    return array

print(bubble_sort([100,2,10,3,-1]))