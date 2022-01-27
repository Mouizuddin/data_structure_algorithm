'''                 Queue
1) Is a linear collection of elements.
2) linear data structures.
3) First In First Out (FIFO) principle.
4) Unlike stacks, a queue is open at both its ends.
5) One end is always used to insert data (enqueue) and the other is used to remove data (dequeue).
6) Insertion and deletion happnes on differenet end's

'''
print('=========== Queue implementation using list ===========\n')
queue = []

def to_add(): # main
    element = int(input('Add element'))
    queue.append(element)
    print(f'{queue}')

def to_remove(): # main
    if not queue : # if len(queue) == 0
        print(f'Satack is empty {queue}')
    else:
        queue.pop(0)
        print(queue)

def to_modify_queue():
    pass

def top_element():
    print(queue[0])

def base_element():
    print(queue[-1])

def selction_sort():
    count = 0
    for i in range(len(queue) - 1):
        count += 1
        min_val = min(queue[i:])  # min value
        index_of_min_val = queue.index(min_val, i)  # this will give the index of min_val
        # print(min_val)
        # print(index_of_min_val)
        queue[i], queue[index_of_min_val] = queue[index_of_min_val], queue[i]
        print(f'iteration number -> {count} and sorted array made is > {queue}')

def queue_implementation():

    while True:
        try:
            choose = int(input('1 - to add\n '
                               '2 - to remove\n '
                               '3 - for the top element\n'
                               '4 - for base element\n'
                               '5 - to sort(selection sort) the Queue\n'
                               '0 - to quit\n'))

            # if choose !>=4:
            if choose >5 :
                print('in range only (0-5)')
            else:
                if choose == 1:
                    to_add()
                elif choose == 2:
                    to_remove()
                elif choose == 3:
                    try:
                        if not queue:
                            print(f'No element queue is empty{queue}')
                        top_element()
                    except IndexError as index:
                        print(f'Error is {index}')

                elif choose == 4:
                    try:
                        if not queue:
                            print(f'No element queue is empty{queue}')
                        if len(queue) >= 2:
                            base_element()
                        else:
                            print(None, end=' ')
                            print(f'{queue} should have atleast 2 elements to print base')
                    except IndexError as index:
                        print(f'Error is {index}')
                elif choose == 5:
                    selction_sort()
                elif choose == 0:
                    print(f'Final queue is {queue}')
                    break
        except ValueError as value:
            print('Only interegrs')
            print(value)

if __name__ == '__main__':
    queue_implementation()
