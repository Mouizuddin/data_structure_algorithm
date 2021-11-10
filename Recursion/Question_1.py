# Find the sum of digits of a positive integers numbers using recursion

def solution_1(number):
    if number == 0:
        return  0
    assert number >=0 and type(number) == int,'ERROR'
    remainder = number % 10
    quotient = number // 10
    print(remainder, quotient)
    return  remainder + solution_1(quotient)

'''Logic
    
    %  (modulus) --> gives remainder
    // (int division) --> gives quotient
    
    Relation : n % 10 + f( n // 10 )
    n % 10 > computers remainder's
    n // 10 > computes quotient's    
'''
print(solution_1(1078))
