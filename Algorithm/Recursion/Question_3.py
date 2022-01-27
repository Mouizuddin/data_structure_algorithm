# Convert Decimal to binary with Recursion

def decimal_to_binary(decimal):
    assert type(decimal) == int, 'ERROR'
    if decimal == 0:
        print(0)
    else:
        decimal_to_binary(decimal // 2)
        print(decimal % 2,end="")


# print(bin(9))
# print(oct(9))
# print(hex(9))
