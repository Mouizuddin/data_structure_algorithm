''' Bubble sort
#  Is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.
#  The average and worst-case time complexity - O(n2)
# '''
def bubble_sort(array):
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

array = [12,4,2,10,0,90]
print(array)
bubble_sort(array)