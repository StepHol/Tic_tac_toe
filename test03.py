A = 414
B = 49


def my_gcd(A, B):
    remainder = A % B
    while remainder != 0:
        A = B
        B = remainder
        remainder = A % B
    else:
        return B

print(my_gcd(A, B))

