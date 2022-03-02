''' Linear search
Linear search is also called as sequential search algorithm. It is the simplest searching algorithm.
In Linear search, we simply traverse the list completely and match each element of the list with the item whose location is to be found.
If the match is found, then the location of the item is returned; otherwise, the algorithm returns NULL
It is widely used to search an element from the unordered list.

The worst-case time complexity >> O(n).
'''
def linear_search(array,key):
    for i in range(len(array)):
        if key == array[i]:
            print(f'Key found at index {array.index(key)}')
            break
    else:
        print('Key not found')
linear_search([12,32,4,54,5,0],0)
