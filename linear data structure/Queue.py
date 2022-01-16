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
    element = input('Add element')
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


def queue_implementation():

    while True:
        choose = int(input('1 - to add , '
                           '2 - to remove , '
                           '3 - for the top element , '
                           '4 - for base element'
                           '0 - to quit'))
        ''''
        if 1,2,3,4,0  100 > else False
        print(__docs__)
        '''
        # if choose !>=4:

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
                if len(queue) >=2 :
                    base_element()
                else:
                    print(None,end=' ')
                    print(f'{queue} should have atleast 2 elements to print base')
            except IndexError as index:
                print(f'Error is {index}')
        elif choose == 0:
            print(f'Final queue is {queue}')
            break


queue_implementation()

# not handled ValueError in this implementation


