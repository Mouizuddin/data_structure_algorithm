# Find the sum of digits of a positive integers numbers using recursion
import Question_2
def solution_1(number):
    if number == 0:
        return  0
    assert number >=0 and type(number) == int,'ERROR'
    remainder = number % 10
    quotient = number // 10
    print(remainder, quotient)
    return  remainder + solution_1(quotient)
# Question_2.n

'''Logic
    
    %  (modulus) --> gives remainder
    // (int division) --> gives quotient
    
    Relation : n % 10 + f( n // 10 )
    n % 10 > computers remainder's
    n // 10 > computes quotient's    
'''
print(solution_1(1078))
print(__name__)
if __name__ == '__main__':
    print(Question_2.name())