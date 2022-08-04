'''Recursion
1) Recursive case
2) Base Case (to stop)
3) Un-intentional Case -  the constrain

'''
def recursion_method(num):
    if num  <=0:
        return False
    return f'{num} _{recursion_method(num-1)}'

# print(recursion_method(10))

# Factorial -> n! = n * (n-1)!

def factorial(num):
    assert num >= 0 and type(num) == int,"number should be positive and integers only"
    if num in [0,1]:
        return  1
    return num * factorial(num-1)

# print(factorial(3))
def pan(name):
    if name[:] == name[::-1]:
        print('its palimdrome')
    print('its not a palimdrome')

