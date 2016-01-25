__author__ = 'vikram'


def vikgcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    :rtype : int
    """
    i = 0
    assert isinstance(b, int)
    print(a, b)
    while b:
        a, b = b, a % b
        print(a, b)
        i += 1
    print("Done")
    return a, i

print(vikgcd(35, 25))

