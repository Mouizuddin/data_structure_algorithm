'''                 Stack
1) Is a linear collection of elements
2) linear data structures
3) LIFO (Last-In-First-Out) principle
4) insertion and deletion of item always take place at same end
'''

stack = []
def to_add(): # main
    element = input('Add element')
    stack.append(element)
    print(f'{stack}')

def to_remove(): # main
    if len(stack) == 0: # if not stack :
        print(f'Satack is empty {stack}')
    else:
        stack.pop()
        print(stack)

def to_modify_stack():
    pass

def top_element():
    print(stack[-1])

def base_element():
    print(stack[0])


def stack_implementation():
    while True:
        choose = int(input('1 - to add , '
                           '2 - to remove , '
                           '3 - for the top element , '
                           '4 - for base element'
                           '0 - to quit'))
        if choose == 1:
            to_add()
        elif choose == 2:
            to_remove()
        elif choose == 3:
            try:
                if not stack:
                    print(f'No element stack is empty{stack}')
                top_element()
            except IndexError as index:
                print(f'Error is {index}')

        elif choose == 4:
            try:
                if not stack:
                    print(f'No element stack is empty{stack}')
                if len(stack) >=2 :
                    base_element()
                else:
                    print(None,end=' ')
                    print(f'{stack} should have atleast 2 elements to print base')
            except IndexError as index:
                print(f'Error is {index}')
        elif choose == 0:
            print(f'Final stack is {stack}')
            break


stack_implementation()

# not handled ValueError in this implementation
# https://www.javatpoint.com/data-structure-stack

