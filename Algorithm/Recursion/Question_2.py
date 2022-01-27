# Power of a number using recursion

def power(base,expo):
    if expo == 0:
        return 1
    if expo == 1:
        return base
    assert expo >= 0 and type(expo) == int,'ERROR'
    return base * power(base,expo-1)

def name():
    return "MOHAMMED MOUIZUDDIN"

print(power(16,2))
print(75%  2)