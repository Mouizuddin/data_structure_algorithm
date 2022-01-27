queue_list = []
def add_element():
    queue_list.append()

def remove_element():
    if len(queue_list) == 0: # not queue_list
        print(f'{queue_list} is empty!')
    queue_list.pop(0)
    print(f'Element :  {queue_list}')

def top_element():
    print(queue_list[0])

def base_element():
    print(queue_list[-1])


while True:
    anything = int(input('1- to add'
                         '2 - to remove'
                         '3 for the top element '
                         '4 - the base element'
                         '0 - exit'))
    if anything == 1:
        add_element()
    elif anything == 2:
        remove_element()
    elif anything == 3 :
        top_element()
    elif anything == 4:
        base_element()
    elif anything == 0:
        break

